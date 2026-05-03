Global header, footer, and navigation are shared components and the single source of truth.

Do not recreate, rewrite, duplicate, or approximate them inside page files.

If a page needs a navbar or footer, reuse the existing shared component only.

Locked files by default:
- 04_site/components/header.html
- 04_site/components/footer.html
- 04_site/assets/weavy.css
- 04_site/index.html (Global Structure Elements)

If a requested task does not explicitly authorize editing these files, they must remain untouched.

Before saving changes, verify:
- no locked file was changed
- no shared component markup was duplicated
- no page contains a rebuilt version of header/footer
- all edits stay inside allowed files only
