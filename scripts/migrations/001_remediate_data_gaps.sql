-- ==============================================================================
-- 741 STUDIO DATA BACKBONE MIGRATION 001
-- Remediating the 8 Core Data Gaps & Activating Multi-Agent Telemetry
--
-- Target Database: Supabase PostgreSQL (741-portal)
-- Strategy: Idempotent, Non-destructive, 100% harmonious with existing portal UI
-- ==============================================================================

BEGIN;

-- ------------------------------------------------------------------------------
-- 1. GOOGLE ADS CAMPAIGNS (Twin to live meta_campaigns)
-- ------------------------------------------------------------------------------
-- Note: 'campaigns' in portal-live.html is used for Strategy/Seasonal planning.
-- We create 'google_campaigns' matching the exact schema of 'meta_campaigns',
-- plus create a unified view 'v_paid_campaigns' combining Google & Meta.
CREATE TABLE IF NOT EXISTS public.google_campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES public.clients(id) ON DELETE CASCADE,
    campaign_id TEXT NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ENABLED', -- 'ENABLED', 'PAUSED', 'REMOVED'
    effective_status TEXT DEFAULT 'ENABLED',
    channel_type TEXT DEFAULT 'SEARCH', -- 'SEARCH', 'PERFORMANCE_MAX', 'DISPLAY', 'VIDEO'
    daily_budget NUMERIC(10, 2) DEFAULT 0.00,
    spend NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    impressions INTEGER NOT NULL DEFAULT 0,
    clicks INTEGER NOT NULL DEFAULT 0,
    ctr NUMERIC(6, 4) GENERATED ALWAYS AS (
        CASE WHEN impressions > 0 THEN ROUND((clicks::NUMERIC / impressions::NUMERIC) * 100, 4) ELSE 0.0000 END
    ) STORED,
    cpc NUMERIC(10, 2) GENERATED ALWAYS AS (
        CASE WHEN clicks > 0 THEN ROUND(spend / clicks, 2) ELSE 0.00 END
    ) STORED,
    conversions NUMERIC(10, 2) DEFAULT 0.00,
    cost_per_conversion NUMERIC(10, 2) GENERATED ALWAYS AS (
        CASE WHEN conversions > 0 THEN ROUND(spend / conversions, 2) ELSE 0.00 END
    ) STORED,
    currency TEXT DEFAULT 'EUR',
    date_start DATE NOT NULL,
    date_stop DATE NOT NULL,
    synced_at TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'::jsonb,
    CONSTRAINT uq_google_campaigns_id_dates UNIQUE (campaign_id, date_start, date_stop)
);

CREATE INDEX IF NOT EXISTS idx_google_campaigns_client ON public.google_campaigns(client_id);
CREATE INDEX IF NOT EXISTS idx_google_campaigns_dates ON public.google_campaigns(date_start DESC, date_stop DESC);

-- Unified Paid Ads View (Google Ads + Meta Ads)
CREATE OR REPLACE VIEW public.v_paid_campaigns AS
SELECT 
    'meta'::TEXT AS platform,
    NULL::UUID AS client_id,
    campaign_id,
    name,
    status,
    effective_status,
    daily_budget,
    spend,
    impressions,
    clicks,
    ctr,
    cpc,
    leads AS conversions,
    cost_per_lead AS cost_per_conversion,
    currency,
    date_start,
    date_stop,
    synced_at
FROM public.meta_campaigns
UNION ALL
SELECT 
    'google'::TEXT AS platform,
    client_id,
    campaign_id,
    name,
    status,
    effective_status,
    daily_budget,
    spend,
    impressions,
    clicks,
    ctr,
    cpc,
    conversions,
    cost_per_conversion,
    currency,
    date_start,
    date_stop,
    synced_at
FROM public.google_campaigns;

-- ------------------------------------------------------------------------------
-- 2. CLIENT_BACKLINKS (Relational Link Health & Toxicity Monitoring)
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.client_backlinks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    source_url TEXT NOT NULL,
    target_url TEXT NOT NULL,
    anchor_text TEXT,
    domain_authority INTEGER CHECK (domain_authority BETWEEN 0 AND 100),
    page_authority INTEGER CHECK (page_authority BETWEEN 0 AND 100),
    toxicity_score NUMERIC(5, 2) DEFAULT 0.00,
    is_toxic BOOLEAN DEFAULT FALSE,
    is_dofollow BOOLEAN DEFAULT TRUE,
    first_seen_date DATE DEFAULT CURRENT_DATE,
    last_verified_date DATE DEFAULT CURRENT_DATE,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'lost', 'removed', 'disavowed')),
    source_provider TEXT DEFAULT 'local_import', -- 'local_import', 'dataforseo', 'brightlocal', 'manual'
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_client_backlinks_pair UNIQUE (client_id, source_url, target_url)
);

CREATE INDEX IF NOT EXISTS idx_client_backlinks_client_status ON public.client_backlinks(client_id, status);
CREATE INDEX IF NOT EXISTS idx_client_backlinks_toxic ON public.client_backlinks(client_id, is_toxic) WHERE is_toxic = TRUE;

-- ------------------------------------------------------------------------------
-- 3. GSC_DAILY_PERFORMANCE (Daily Search Console Rollups & Target Keywords)
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.gsc_daily_performance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    page TEXT NOT NULL,
    query TEXT, -- NULL for total page-level rollup, populated for top target keywords
    is_target_keyword BOOLEAN DEFAULT FALSE,
    clicks INTEGER NOT NULL DEFAULT 0,
    impressions INTEGER NOT NULL DEFAULT 0,
    ctr NUMERIC(6, 4) NOT NULL DEFAULT 0.0000,
    position NUMERIC(6, 2) NOT NULL DEFAULT 0.00,
    country TEXT DEFAULT 'deu',
    device TEXT DEFAULT 'all',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_gsc_daily_entry UNIQUE (client_id, date, page, query)
);

CREATE INDEX IF NOT EXISTS idx_gsc_perf_client_date ON public.gsc_daily_performance(client_id, date DESC);
CREATE INDEX IF NOT EXISTS idx_gsc_perf_page ON public.gsc_daily_performance(client_id, page);
CREATE INDEX IF NOT EXISTS idx_gsc_perf_target_query ON public.gsc_daily_performance(client_id, query) WHERE is_target_keyword = TRUE;

-- ------------------------------------------------------------------------------
-- 4. GEO_GRID_SCANS (Local Falcon / Spatial Maps Scans + Grid Screenshots)
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.geo_grid_scans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    keyword TEXT NOT NULL,
    scan_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    grid_size TEXT DEFAULT '7x7',
    radius_km NUMERIC(6, 2) DEFAULT 5.0,
    center_lat NUMERIC(10, 7),
    center_lng NUMERIC(10, 7),
    arp NUMERIC(5, 2),   -- Average Rank Position
    atrp NUMERIC(5, 2),  -- Average Target Rank Position
    solv NUMERIC(5, 2),  -- Share of Local Voice (%)
    top3_count INTEGER DEFAULT 0,
    points JSONB NOT NULL DEFAULT '[]'::jsonb, -- Array of {lat, lng, rank, place_id, name}
    screenshot_path TEXT, -- Storage path in 'materials' bucket
    screenshot_url TEXT,  -- Public / signed preview URL
    raw_data_url TEXT,
    provider TEXT DEFAULT 'local_falcon',
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_geo_grid_client_date ON public.geo_grid_scans(client_id, scan_date DESC);
CREATE INDEX IF NOT EXISTS idx_geo_grid_keyword ON public.geo_grid_scans(client_id, keyword);

-- ------------------------------------------------------------------------------
-- 5. BRIGHTLOCAL_AUDITS (Directory Consistency & Citation Health)
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.brightlocal_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    audit_date DATE NOT NULL DEFAULT CURRENT_DATE,
    report_type TEXT NOT NULL DEFAULT 'citation_tracker',
    nap_consistency_score NUMERIC(5, 2), -- 0 - 100%
    citation_count INTEGER DEFAULT 0,
    citation_live_count INTEGER DEFAULT 0,
    citation_missing_count INTEGER DEFAULT 0,
    duplicate_count INTEGER DEFAULT 0,
    average_rating NUMERIC(3, 2),
    review_count INTEGER DEFAULT 0,
    report_url TEXT,
    raw_summary JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_brightlocal_client_date_type UNIQUE (client_id, audit_date, report_type)
);

CREATE INDEX IF NOT EXISTS idx_brightlocal_client_date ON public.brightlocal_audits(client_id, audit_date DESC);

-- ------------------------------------------------------------------------------
-- 6. CLIENT_DRIVE_ASSETS (Lightweight pointers to Google Drive assets)
-- ------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.client_drive_assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    drive_file_id TEXT,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL, -- Relative path from client folder, e.g. '_drive/exports/sample.xlsx'
    mime_type TEXT,
    size_bytes BIGINT,
    sha256_hash TEXT,
    web_view_link TEXT,
    web_content_link TEXT,
    category TEXT DEFAULT 'other', -- 'sheet', 'cro_asset', 'content_export', 'offer_pdf'
    last_synced_at TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_client_drive_assets_file UNIQUE (client_id, file_path)
);

CREATE INDEX IF NOT EXISTS idx_client_drive_assets_cat ON public.client_drive_assets(client_id, category);

-- ------------------------------------------------------------------------------
-- 7. ENHANCE LEADS & SITE_FORM_SUBMISSIONS
-- ------------------------------------------------------------------------------
-- Allow anon/webhook ingestion into site_form_submissions
ALTER TABLE public.site_form_submissions ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS anon_insert_site_form_submissions ON public.site_form_submissions;
CREATE POLICY anon_insert_site_form_submissions ON public.site_form_submissions
    FOR INSERT TO anon, authenticated
    WITH CHECK (true);

-- Extend leads table with agent scoring columns without touching existing portal fields
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='leads' AND column_name='lead_score') THEN
        ALTER TABLE public.leads ADD COLUMN lead_score INTEGER DEFAULT 0 CHECK (lead_score BETWEEN 0 AND 100);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='leads' AND column_name='scoring_rationale') THEN
        ALTER TABLE public.leads ADD COLUMN scoring_rationale TEXT;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='leads' AND column_name='intent_category') THEN
        ALTER TABLE public.leads ADD COLUMN intent_category TEXT;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='leads' AND column_name='submission_id') THEN
        ALTER TABLE public.leads ADD COLUMN submission_id UUID REFERENCES public.site_form_submissions(id) ON DELETE SET NULL;
    END IF;
END $$;

-- ------------------------------------------------------------------------------
-- 8. ENHANCE WORK_AGENT_RUNS (Telemetry, Cost Accounting & Token Optimization)
-- ------------------------------------------------------------------------------
-- Note: work_agent_runs already exists with: id, client_id, work_item_id, agent_id, delegated_by, state, summary, session_ref, started_at, ended_at, cost_eur, source, source_id
-- We safely add token telemetry columns:
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='agent_lane') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN agent_lane TEXT;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='model_name') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN model_name TEXT;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='model_tier') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN model_tier TEXT CHECK (model_tier IN ('tier_1', 'tier_2', 'tier_3'));
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='prompt_tokens') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN prompt_tokens INTEGER DEFAULT 0;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='cached_prompt_tokens') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN cached_prompt_tokens INTEGER DEFAULT 0;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='completion_tokens') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN completion_tokens INTEGER DEFAULT 0;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='cost_estimate_usd') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN cost_estimate_usd NUMERIC(10, 6) DEFAULT 0.000000;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='duration_ms') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN duration_ms INTEGER DEFAULT 0;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='tool_call_count') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN tool_call_count INTEGER DEFAULT 0;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='tool_calls') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN tool_calls JSONB DEFAULT '[]'::jsonb;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema='public' AND table_name='work_agent_runs' AND column_name='harness_engine') THEN
        ALTER TABLE public.work_agent_runs ADD COLUMN harness_engine TEXT DEFAULT 'odysseus';
    END IF;
END $$;

-- ------------------------------------------------------------------------------
-- ROW-LEVEL SECURITY (RLS) POLICIES
-- ------------------------------------------------------------------------------

ALTER TABLE public.google_campaigns ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.client_backlinks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.gsc_daily_performance ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.geo_grid_scans ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.brightlocal_audits ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.client_drive_assets ENABLE ROW LEVEL SECURITY;

-- 1. Service Role & Admin Access (Full CRUD)
-- 1. Admin Full CRUD & Delivery Read
DO $$
DECLARE
    t TEXT;
BEGIN
    FOR t IN 
        SELECT unnest(ARRAY[
            'google_campaigns', 'client_backlinks', 'gsc_daily_performance',
            'geo_grid_scans', 'brightlocal_audits', 'client_drive_assets'
        ])
    LOOP
        EXECUTE format('DROP POLICY IF EXISTS "admin all" ON public.%I', t);
        EXECUTE format('DROP POLICY IF EXISTS "delivery read" ON public.%I', t);
        EXECUTE format('DROP POLICY IF EXISTS "client read own" ON public.%I', t);
        
        -- Admin has full read/write access (includes standup-bot)
        EXECUTE format('CREATE POLICY "admin all" ON public.%I FOR ALL TO authenticated USING (is_admin()) WITH CHECK (is_admin())', t);
        
        -- Delivery staff has read access
        EXECUTE format('CREATE POLICY "delivery read" ON public.%I FOR SELECT TO authenticated USING (is_delivery())', t);
        
        -- Clients can read only their own rows
        EXECUTE format('CREATE POLICY "client read own" ON public.%I FOR SELECT TO authenticated USING (client_id = my_client_id())', t);
    END LOOP;
END $$;

COMMIT;

-- ==============================================================================
-- ROLLBACK SCRIPT (Execute only if needed to cleanly reverse this migration)
-- ==============================================================================
/*
BEGIN;
    DROP VIEW IF EXISTS public.v_paid_campaigns CASCADE;
    DROP TABLE IF EXISTS public.google_campaigns CASCADE;
    DROP TABLE IF EXISTS public.client_drive_assets CASCADE;
    DROP TABLE IF EXISTS public.brightlocal_audits CASCADE;
    DROP TABLE IF EXISTS public.geo_grid_scans CASCADE;
    DROP TABLE IF EXISTS public.gsc_daily_performance CASCADE;
    DROP TABLE IF EXISTS public.client_backlinks CASCADE;
    
    -- Revert added columns in work_agent_runs
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS agent_lane;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS model_name;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS model_tier;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS prompt_tokens;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS cached_prompt_tokens;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS completion_tokens;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS cost_estimate_usd;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS duration_ms;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS tool_call_count;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS tool_calls;
    ALTER TABLE public.work_agent_runs DROP COLUMN IF EXISTS harness_engine;

    -- Revert added columns in leads
    ALTER TABLE public.leads DROP COLUMN IF EXISTS lead_score;
    ALTER TABLE public.leads DROP COLUMN IF EXISTS scoring_rationale;
    ALTER TABLE public.leads DROP COLUMN IF EXISTS intent_category;
    ALTER TABLE public.leads DROP COLUMN IF EXISTS submission_id;
COMMIT;
*/
