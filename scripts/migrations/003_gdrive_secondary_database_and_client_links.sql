-- 741 Studio — Migration 003: Google Drive Secondary Operational Layer & Client Links
-- Author: Martin Drendel & AI Assistant
-- Date: 2026-10-16
-- Purpose:
--   1. Anchor Google Drive (741studio18@gmail.com / "741 Clients") as the extended secondary operational
--      database to Supabase as the primary Source of Truth.
--   2. Add drive_folder_url and drive_folder_id to public.clients so any AI agent or LLM (Claude, ChatGPT,
--      Antigravity, Gemini, n8n) querying Supabase can instantly resolve the client's Drive workspace.
--   3. Seed verified Drive folder URLs and IDs for active 741 clients.
--   4. Create public.v_client_drive_overview to summarize cataloged docs, sheets, and assets per client.

-- ============================================================================
-- 1. Extend public.clients with Google Drive Root Pointers
-- ============================================================================
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_schema = 'public' AND table_name = 'clients' AND column_name = 'drive_folder_url'
    ) THEN
        ALTER TABLE public.clients ADD COLUMN drive_folder_url TEXT;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_schema = 'public' AND table_name = 'clients' AND column_name = 'drive_folder_id'
    ) THEN
        ALTER TABLE public.clients ADD COLUMN drive_folder_id TEXT;
    END IF;
END $$;

-- ============================================================================
-- 2. Seed Verified Client Google Drive Folders (Root Account: 741studio18@gmail.com)
-- ============================================================================
-- Praxis Suriya (Ingelheim)
UPDATE public.clients
SET 
    drive_folder_url = 'https://drive.google.com/drive/folders/1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis',
    drive_folder_id = '1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis'
WHERE id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649';

-- Naturheilpraxis Daniela Dumann (Berlin)
UPDATE public.clients
SET 
    drive_folder_url = 'https://drive.google.com/drive/folders/1TYstYL7lzgRBgBk8P1MvOGcXtG4nEuD5',
    drive_folder_id = '1TYstYL7lzgRBgBk8P1MvOGcXtG4nEuD5'
WHERE id = 'd01f4236-8674-45fe-a347-0751fa7b24de';

-- Praxis Hüwel (Nürnberg)
UPDATE public.clients
SET 
    drive_folder_url = 'https://drive.google.com/drive/folders/1d_NkMF5YEDAkpuBvsfvfGJW9nnVloul6',
    drive_folder_id = '1d_NkMF5YEDAkpuBvsfvfGJW9nnVloul6'
WHERE id = 'f0a6730f-8f56-4c61-8085-1955f3bb285a';

-- Maria Brasse (Feng Shui Berlin)
UPDATE public.clients
SET 
    drive_folder_url = 'https://drive.google.com/drive/folders/18Zel5nZ7jNY6yFPsHJQrrS6-mLKeUkY8',
    drive_folder_id = '18Zel5nZ7jNY6yFPsHJQrrS6-mLKeUkY8'
WHERE id = '444ac77b-747d-4855-89e5-12ac97d2363c';

-- STÜRZL Steuerstrafrecht (Frankfurt & München)
UPDATE public.clients
SET 
    drive_folder_url = 'https://drive.google.com/drive/folders/1dF8IKY_Syjnji2CyHGAhY8SFb78dmlua',
    drive_folder_id = '1dF8IKY_Syjnji2CyHGAhY8SFb78dmlua'
WHERE id = 'b6f6e303-50e4-4afb-a343-337206cec316';

-- ============================================================================
-- 3. Ensure public.client_drive_assets Structure & Indexes
-- ============================================================================
CREATE TABLE IF NOT EXISTS public.client_drive_assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
    drive_file_id TEXT,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    mime_type TEXT,
    size_bytes BIGINT,
    sha256_hash TEXT,
    web_view_link TEXT,
    web_content_link TEXT,
    category TEXT DEFAULT 'other', -- 'sheet', 'doc', 'offer_pdf', 'cro_asset', 'content_export'
    last_synced_at TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_client_drive_assets_file UNIQUE (client_id, file_path)
);

CREATE INDEX IF NOT EXISTS idx_client_drive_assets_cat ON public.client_drive_assets(client_id, category);

-- Enable RLS
ALTER TABLE public.client_drive_assets ENABLE ROW LEVEL SECURITY;

DO $$ BEGIN
    DROP POLICY IF EXISTS "Allow read access to authenticated users" ON public.client_drive_assets;
    CREATE POLICY "Allow read access to authenticated users" 
        ON public.client_drive_assets FOR SELECT 
        TO authenticated 
        USING (true);
EXCEPTION WHEN OTHERS THEN NULL;
END $$;

-- ============================================================================
-- 4. Overview View: public.v_client_drive_overview
-- ============================================================================
CREATE OR REPLACE VIEW public.v_client_drive_overview AS
SELECT 
    c.id AS client_id,
    c.name AS client_name,
    c.status AS client_status,
    c.drive_folder_url,
    c.drive_folder_id,
    c.stammdaten_sheet_url,
    COUNT(a.id) AS total_drive_assets,
    COUNT(CASE WHEN a.category = 'sheet' THEN 1 END) AS count_sheets,
    COUNT(CASE WHEN a.category = 'doc' THEN 1 END) AS count_docs,
    COUNT(CASE WHEN a.category = 'offer_pdf' THEN 1 END) AS count_proposals_contracts,
    COUNT(CASE WHEN a.category = 'cro_asset' THEN 1 END) AS count_cro_assets,
    MAX(a.last_synced_at) AS last_asset_synced_at
FROM public.clients c
LEFT JOIN public.client_drive_assets a ON c.id = a.client_id
GROUP BY c.id, c.name, c.status, c.drive_folder_url, c.drive_folder_id, c.stammdaten_sheet_url;

COMMENT ON VIEW public.v_client_drive_overview IS 'Unified view linking Supabase clients to their Google Drive folders and cataloged Docs/Sheets.';
