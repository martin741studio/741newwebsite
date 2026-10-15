-- 741 Studio — Migration 002: GBP Daily Actions, Client Goals & Weekly Rollup Views
-- Author: Martin Drendel & AI Assistant
-- Date: 2026-10-16
-- Purpose:
--   1. Create public.gbp_daily_actions to store native GBP conversion actions (calls, messages, directions).
--   2. Create public.client_goals to store target values and warning thresholds for error signal calculations.
--   3. Create public.v_gsc_weekly_performance rollup view to shield LLM token budgets (99% reduction).
--   4. Create public.v_gbp_weekly_actions rollup view for the client portal and Morning Grill.

-- ============================================================================
-- 1. Table: public.gbp_daily_actions
-- ============================================================================
CREATE TABLE IF NOT EXISTS public.gbp_daily_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    call_clicks INTEGER NOT NULL DEFAULT 0,
    website_clicks INTEGER NOT NULL DEFAULT 0,
    direction_requests INTEGER NOT NULL DEFAULT 0,
    message_conversations INTEGER NOT NULL DEFAULT 0,
    bookings INTEGER NOT NULL DEFAULT 0,
    raw_payload JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(client_id, date)
);

CREATE INDEX IF NOT EXISTS idx_gbp_actions_client_date ON public.gbp_daily_actions(client_id, date DESC);

-- Enable RLS
ALTER TABLE public.gbp_daily_actions ENABLE ROW LEVEL SECURITY;

DO $$ BEGIN
    DROP POLICY IF EXISTS "Allow read access to authenticated users" ON public.gbp_daily_actions;
    CREATE POLICY "Allow read access to authenticated users" 
        ON public.gbp_daily_actions FOR SELECT 
        TO authenticated 
        USING (true);
EXCEPTION WHEN OTHERS THEN NULL;
END $$;

-- ============================================================================
-- 2. Table: public.client_goals (Feedback Sensor)
-- ============================================================================
CREATE TABLE IF NOT EXISTS public.client_goals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    metric_name TEXT NOT NULL,         -- e.g. 'monthly_leads', 'cpa_ceiling', 'target_rank_top3'
    channel TEXT NOT NULL,             -- e.g. 'all', 'google_ads', 'local_falcon', 'gbp_actions'
    target_value NUMERIC NOT NULL,     -- e.g. 20 (leads), 2.50 (CPA)
    warning_threshold NUMERIC NOT NULL,-- delta triggering alert (e.g. 0.30 = 30% drop)
    period TEXT NOT NULL DEFAULT 'monthly', -- 'weekly' or 'monthly'
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(client_id, metric_name, channel, period)
);

CREATE INDEX IF NOT EXISTS idx_client_goals_client ON public.client_goals(client_id);

-- Enable RLS
ALTER TABLE public.client_goals ENABLE ROW LEVEL SECURITY;

DO $$ BEGIN
    DROP POLICY IF EXISTS "Allow read access to authenticated users" ON public.client_goals;
    CREATE POLICY "Allow read access to authenticated users" 
        ON public.client_goals FOR SELECT 
        TO authenticated 
        USING (true);
EXCEPTION WHEN OTHERS THEN NULL;
END $$;

-- ============================================================================
-- 3. Token Shield: Weekly Rollup Views
-- ============================================================================

-- GSC Weekly Rollup View
CREATE OR REPLACE VIEW public.v_gsc_weekly_performance AS
SELECT 
    client_id,
    date_trunc('week', date)::date AS week_start,
    SUM(clicks) AS total_clicks,
    SUM(impressions) AS total_impressions,
    ROUND(AVG(position)::numeric, 2) AS avg_position,
    ROUND((CASE WHEN SUM(impressions) > 0 THEN (SUM(clicks)::numeric / SUM(impressions)::numeric) * 100 ELSE 0 END), 2) AS avg_ctr
FROM public.gsc_daily_performance
GROUP BY client_id, date_trunc('week', date)::date
ORDER BY client_id, week_start DESC;

-- GBP Weekly Actions View
CREATE OR REPLACE VIEW public.v_gbp_weekly_actions AS
SELECT 
    client_id,
    date_trunc('week', date)::date AS week_start,
    SUM(call_clicks) AS total_call_clicks,
    SUM(website_clicks) AS total_website_clicks,
    SUM(direction_requests) AS total_direction_requests,
    SUM(message_conversations) AS total_messages,
    SUM(bookings) AS total_bookings,
    SUM(call_clicks + website_clicks + direction_requests + message_conversations + bookings) AS total_actions
FROM public.gbp_daily_actions
GROUP BY client_id, date_trunc('week', date)::date
ORDER BY client_id, week_start DESC;

-- ============================================================================
-- 4. Initial Goals Seed (Praxis Suriya Pilot)
-- ============================================================================
INSERT INTO public.client_goals (client_id, metric_name, channel, target_value, warning_threshold, period)
VALUES 
    ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649', 'monthly_leads', 'all', 20, 5, 'monthly'),
    ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649', 'weekly_contact_actions', 'gbp_actions', 10, 3, 'weekly'),
    ('d0519d13-0bfc-4dfb-b512-57bf550387e6', 'cpa_ceiling', 'google_ads', 2.50, 0.50, 'monthly'),
    ('d0519d13-0bfc-4dfb-b512-57bf550387e6', 'monthly_conversions', 'google_ads', 30, 5, 'monthly')
ON CONFLICT (client_id, metric_name, channel, period) 
DO UPDATE SET 
    target_value = EXCLUDED.target_value,
    warning_threshold = EXCLUDED.warning_threshold,
    updated_at = NOW();
