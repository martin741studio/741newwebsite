import re

with open('/Users/martindrendel/741website/WABA/Reference code', 'r') as f:
    content = f.read()

# Add hero.css to <head>
if '</head>' in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="hero.css" />\n  </head>')

# Extract the SVG Logo so we can inject it back into the new header
svg_logo = ''
svg_match = re.search(r'(<svg width="100%" height="100%" viewBox="0 0 154 152".*?</svg>)', content, re.DOTALL)
if svg_match:
    svg_logo = svg_match.group(1)

new_header = f"""      <header class="home">
        <div class="container max-w-none px-cont">
          <div class="pt-cont h-screen pb-cont s:h-svh">
            <div class="home_body flex flex-col py-20 h-full relative rounded-20 overflow-hidden justify-between s:rounded-10">
              
              <!-- LAYER 1: Background Video -->
              <div class="absolute inset-0 z-0">
                  <video class="w-full h-full object-cover" autoplay muted loop playsinline poster="https://cdn.sanity.io/images/lnp5wwlt/production/38ae871813b1377acbf8d1f2d67f6c601d5f8f43-3800x1900.jpg?w=1024&amp;blur=10&amp;q=30">
                    <!-- Placeholder video, user will replace with actual video asset -->
                    <source src="https://lolo-website.b-cdn.net/Home%20Page/compressed/home.webm" type="video/mp4" />
                  </video>
              </div>

              <!-- LAYER 2: Overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-[#efece8]/90 via-[#efece8]/40 to-[#efece8]/20 z-1 pointer-events-none"></div>

              <!-- LAYER 3: Floating Elements (with CSS animations) -->
              <div class="floating-elements absolute inset-0 z-2 overflow-hidden pointer-events-none">
                  <!-- Abstract shapes or placeholders, animated in CSS -->
                  <div class="float-item float-item-1"><div class="placeholder-shape sphere"></div></div>
                  <div class="float-item float-item-2"><div class="placeholder-shape cube"></div></div>
                  <div class="float-item float-item-3"><div class="placeholder-shape pyramid"></div></div>
                  <div class="float-item float-item-4"><div class="placeholder-shape torus"></div></div>
                  <div class="float-item float-item-5"><div class="placeholder-shape cone"></div></div>
                  <div class="float-item float-item-6"><div class="placeholder-shape ring"></div></div>
                  <div class="float-item float-item-7"><div class="placeholder-shape abstract"></div></div>
                  <!-- The user will replace these with actual image assets like the glasses, book, trumpet -->
              </div>

              <!-- LAYER 4: People Subject Integration -->
              <div class="absolute bottom-[-10px] left-1/2 -translate-x-1/2 w-[80%] max-w-[1200px] z-3 flex justify-center items-end pointer-events-none">
                  <!-- Placeholder image for the people sitting on couch. The user will swap this with their cutout. -->
                  <img src="https://images.unsplash.com/photo-1543269664-56d5d51436fd?q=80&w=1200&auto=format&fit=crop" alt="Team" class="w-full h-auto subject-image" />
              </div>

              <!-- LAYER 5: UI Elements (Logo) -->
              <div class="absolute left-1/2 -translate-x-1/2 top-cont z-10 w-154 h-152 l:w-120 l:h-116 mix-blend-difference text-white">
                {svg_logo}
              </div>
              
              <h1 class="text-2xl uppercase text-center h1 invisible">
                WABA Premium Hero Section
              </h1>
            </div>
          </div>
        </div>
      </header>"""

# Replace the original <header class="home">
content = re.sub(r'<header class="home">.*?</header>', new_header, content, flags=re.DOTALL)

with open('/Users/martindrendel/741website/WABA/index.html', 'w') as f:
    f.write(content)

print("index.html created successfully.")
