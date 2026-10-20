# WordPress Content & Client Text Boxes (Hard-Coded Rule)

## No Raw HTML in Client-Editable Text Boxes
In all WordPress, Elementor, Gutenberg, Page Builder, and ACF work:
- **Never put raw HTML tags** (`<span>`, `<br>`, `<strong>`, `<div>`, inline style attributes, etc.) inside text boxes, headings, or content fields where clients make text edits.
- Embedding HTML in text boxes confuses clients, causes accidental tag deletion, and breaks layouts.
- **Enforcement:**
  - Keep client-facing text boxes strictly **plain text**.
  - All styling, color accents, typography, spacing, and highlights must be achieved through **native widget controls, theme styling, dedicated sub-elements, or CSS classes applied at the container/wrapper level**.
  - If a layout requires highlighted words or multi-style text, split the elements into distinct controls or use native block styling instead of embedding raw HTML into a single text input.
