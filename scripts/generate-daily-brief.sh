#!/usr/bin/env bash
# 741 Studio — Daily Brief Generator
# Usage: npm run brief (or bash scripts/generate-daily-brief.sh)

set -e

TODAY=$(date +"%Y-%m-%d")
BRIEF_DIR="00_project/daily-briefs/${TODAY}"
mkdir -p "${BRIEF_DIR}"

echo "=== 741 Studio — Morning Brief Generator ==="
echo "Generating daily brief for ${TODAY}..."

# 1. Regenerate goals from Supabase overlay if script exists
if [ -f "00_project/morning-grill-skill/scripts/generate_goals.py" ]; then
    python3 00_project/morning-grill-skill/scripts/generate_goals.py 2>/dev/null || true
fi

# 2. Run deterministic morning scanner
if [ -f "00_project/morning-grill-skill/scripts/scan.py" ]; then
    python3 00_project/morning-grill-skill/scripts/scan.py --date "${TODAY}" --bookmark "$(date -v-1d +"%Y-%m-%dT06:00:00+08:00" 2>/dev/null || date -d "yesterday" +"%Y-%m-%dT06:00:00+08:00")" --out "${BRIEF_DIR}" 2>/dev/null || true
fi

# 3. Build cards if brief.json exists
if [ -f "${BRIEF_DIR}/scan.json" ] && [ -f "00_project/morning-grill-skill/scripts/build_cards.py" ]; then
    python3 00_project/morning-grill-skill/scripts/build_cards.py --run "${BRIEF_DIR}" 2>/dev/null || true
fi

# 4. Render markdown and HTML briefs
if [ -f "${BRIEF_DIR}/brief.json" ] && [ -f "00_project/morning-grill-skill/scripts/render_brief.py" ]; then
    python3 00_project/morning-grill-skill/scripts/render_brief.py --run "${BRIEF_DIR}" 2>/dev/null || true
fi

echo "✅ Morning brief ready:"
echo "   Markdown: ${BRIEF_DIR}/brief.md"
if [ -f "${BRIEF_DIR}/brief.html" ]; then
    echo "   HTML View: ${BRIEF_DIR}/brief.html"
fi
