import { motion, useMotionValue, useSpring, useTransform } from "motion/react";
import { useEffect, useRef, useState } from "react";
import { Check } from "lucide-react";

export default function ValueProp() {
  const containerRef = useRef<HTMLDivElement>(null);
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const [layers, setLayers] = useState([
    { id: 'canvas', text: 'CANVAS', active: false, checked: true },
    { id: 'walkie', text: 'WALKIE TALKIE', active: false, checked: true },
    { id: 'text1', text: 'TEXT LAYER', active: true, checked: true },
    { id: 'text2', text: 'TEXT LAYER', active: false, checked: true },
    { id: 'astro', text: 'ASTRONAUT', active: false, checked: true },
    { id: 'ship', text: 'SPACESHIP', active: false, checked: true },
  ]);

  const toggleLayer = (id: string) => {
    setLayers(layers.map(l => l.id === id ? { ...l, checked: !l.checked } : l));
  };

  // Smooth springs for mouse movement
  const springConfig = { damping: 25, stiffness: 150 };
  const smoothX = useSpring(mouseX, springConfig);
  const smoothY = useSpring(mouseY, springConfig);

  // Parallax transforms for different layers
  // Background moves slightly opposite to mouse
  const bgX = useTransform(smoothX, [-0.5, 0.5], ["2%", "-2%"]);
  const bgY = useTransform(smoothY, [-0.5, 0.5], ["2%", "-2%"]);
  
  // Astronaut moves with mouse (more pronounced)
  const astroX = useTransform(smoothX, [-0.5, 0.5], ["-4%", "4%"]);
  const astroY = useTransform(smoothY, [-0.5, 0.5], ["-4%", "4%"]);

  // Text moves slightly with mouse
  const textX = useTransform(smoothX, [-0.5, 0.5], ["-2%", "2%"]);
  const textY = useTransform(smoothY, [-0.5, 0.5], ["-2%", "2%"]);

  // Foreground (phone) moves a lot opposite to mouse
  const fgX = useTransform(smoothX, [-0.5, 0.5], ["8%", "-8%"]);
  const fgY = useTransform(smoothY, [-0.5, 0.5], ["8%", "-8%"]);

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    
    // Calculate mouse position relative to center of container (-0.5 to 0.5)
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    
    mouseX.set(x);
    mouseY.set(y);
  };

  const handleMouseLeave = () => {
    // Reset to center
    mouseX.set(0);
    mouseY.set(0);
  };

  return (
    <section className="relative py-32 overflow-hidden bg-[#f8f9fa]">
      {/* Grid Background */}
      <div className="absolute inset-0 pointer-events-none" 
           style={{
             backgroundImage: 'linear-gradient(to right, rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,0.03) 1px, transparent 1px)',
             backgroundSize: '40px 40px'
           }} 
      />

      <div className="max-w-[1600px] mx-auto px-6 relative z-10">
        <div className="text-center mb-16">
          <h2 className="text-6xl md:text-8xl lg:text-[100px] font-display text-zinc-900 tracking-tight leading-[0.9] mb-6">
            Control the Outcome
          </h2>
          <p className="text-xl text-zinc-600 max-w-2xl mx-auto">
            Layers, type, and blends—all the tools to bring your wildest ideas to life. Your creativity, our compositing power.
          </p>
        </div>

        {/* Editor UI Mockup */}
        <div className="w-full max-w-[1400px] mx-auto bg-[#18181b] rounded-2xl overflow-hidden shadow-2xl flex border border-zinc-800 h-[800px]">
          {/* Left Sidebar */}
          <div className="w-72 bg-[#27272a] border-r border-zinc-800 flex flex-col shrink-0">
            <div className="p-6 border-b border-zinc-800">
              <h3 className="text-white font-medium text-lg">Title sequence</h3>
            </div>
            <div className="p-4 flex-1 overflow-y-auto">
              <div className="text-xs font-bold text-zinc-500 mb-4 tracking-widest">LAYERS</div>
              <div className="space-y-1">
                {layers.map((layer) => (
                  <LayerItem 
                    key={layer.id}
                    text={layer.text} 
                    active={layer.active} 
                    checked={layer.checked}
                    onClick={() => toggleLayer(layer.id)}
                  />
                ))}
              </div>
            </div>
          </div>

          {/* Center Canvas with Mouse Parallax */}
          <div 
            ref={containerRef}
            onMouseMove={handleMouseMove}
            onMouseLeave={handleMouseLeave}
            className="flex-1 bg-[#18181b] p-8 relative overflow-hidden flex items-center justify-center cursor-crosshair"
            style={{ 
              backgroundImage: 'linear-gradient(45deg, #27272a 25%, transparent 25%), linear-gradient(-45deg, #27272a 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #27272a 75%), linear-gradient(-45deg, transparent 75%, #27272a 75%)',
              backgroundSize: '20px 20px',
              backgroundPosition: '0 0, 0 10px, 10px -10px, -10px 0px'
            }}
          >
            <div className="relative w-full h-full max-w-5xl aspect-video rounded-lg overflow-visible shadow-2xl">
              
              {/* Base Background Image */}
              <motion.img 
                src="https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682ee1e4abc8a6ba31b611d5_spaceship.avif" 
                alt="Spaceship" 
                style={{ x: bgX, y: bgY, scale: 1.05 }}
                className="absolute inset-0 w-full h-full object-cover rounded-lg" 
              />
              
              {/* Astronaut Image */}
              <motion.img 
                src="https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682ee1e4018d126165811a7b_Astro.avif" 
                alt="Astronaut" 
                style={{ x: astroX, y: astroY, scale: 1.1 }}
                className="absolute inset-0 w-full h-full object-cover z-10" 
              />

              {/* Text Layer */}
              <motion.div 
                style={{ x: textX, y: textY }}
                className="absolute inset-0 z-20 flex flex-col items-center justify-center pointer-events-none"
              >
                <div className="text-black font-mono text-sm md:text-base mb-2 tracking-widest font-bold">Directed by</div>
                <div className="border border-black/20 p-3 backdrop-blur-sm bg-white/10 relative">
                  {/* Selection Handles */}
                  <div className="absolute -top-1 -left-1 w-2 h-2 bg-white border border-black" />
                  <div className="absolute -top-1 -right-1 w-2 h-2 bg-white border border-black" />
                  <div className="absolute -bottom-1 -left-1 w-2 h-2 bg-white border border-black" />
                  <div className="absolute -bottom-1 -right-1 w-2 h-2 bg-white border border-black" />
                  
                  <h1 className="text-3xl md:text-5xl font-mono font-bold text-black tracking-tighter">Martin Drendel</h1>
                </div>
              </motion.div>

              {/* Foreground Blur Element (Phone) */}
              <motion.img 
                src="https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682eecb4b45672741cafa0f6_phone.avif" 
                alt="Phone" 
                style={{ x: fgX, y: fgY, scale: 1.2 }}
                className="absolute -bottom-10 right-[15%] w-[450px] h-auto object-cover z-30 opacity-90 blur-[4px]" 
              />

            </div>
          </div>

          {/* Right Sidebar */}
          <div className="w-80 bg-[#27272a] border-l border-zinc-800 flex flex-col shrink-0">
            <div className="p-6 border-b border-zinc-800 flex items-center gap-3">
              <div className="w-6 h-6 border border-zinc-500 rounded flex items-center justify-center text-zinc-400 text-sm">T</div>
              <h3 className="text-white font-medium text-sm tracking-widest">TEXT LAYER</h3>
            </div>
            <div className="p-6 space-y-8">
              <div>
                <div className="text-xs font-bold text-zinc-500 mb-3 tracking-widest">DIMENSIONS</div>
                <div className="flex gap-3">
                  <div className="flex-1 bg-[#18181b] border border-zinc-700 rounded p-2.5 flex items-center gap-2">
                    <span className="text-zinc-500 text-xs">W</span>
                    <span className="text-white text-sm">1024</span>
                  </div>
                  <div className="flex-1 bg-[#18181b] border border-zinc-700 rounded p-2.5 flex items-center gap-2">
                    <span className="text-zinc-500 text-xs">H</span>
                    <span className="text-white text-sm">1240</span>
                  </div>
                </div>
              </div>
              <div>
                <div className="text-xs font-bold text-zinc-500 mb-3 tracking-widest">POSITION</div>
                <div className="flex gap-3">
                  <div className="flex-1 bg-[#18181b] border border-zinc-700 rounded p-2.5 flex items-center gap-2">
                    <span className="text-zinc-500 text-xs">X</span>
                    <span className="text-white text-sm">240</span>
                  </div>
                  <div className="flex-1 bg-[#18181b] border border-zinc-700 rounded p-2.5 flex items-center gap-2">
                    <span className="text-zinc-500 text-xs">Y</span>
                    <span className="text-white text-sm">724</span>
                  </div>
                </div>
              </div>
              <div>
                <div className="text-xs font-bold text-zinc-500 mb-3 tracking-widest">ROTATION</div>
                <div className="w-1/2 pr-1.5">
                  <div className="bg-[#18181b] border border-zinc-700 rounded p-2.5 flex items-center gap-2">
                    <span className="text-zinc-500 text-xs">∡</span>
                    <span className="text-white text-sm">90°</span>
                  </div>
                </div>
              </div>
              <div className="pt-6 border-t border-zinc-800">
                <div className="flex justify-between mb-3">
                  <div className="text-xs font-bold text-zinc-500 tracking-widest">OPACITY</div>
                  <div className="text-xs font-bold text-zinc-500 tracking-widest w-1/2 pl-1.5">BLEND MODE</div>
                </div>
                <div className="flex gap-3">
                  <div className="w-1/2 bg-[#18181b] border border-zinc-700 rounded p-2.5">
                    <span className="text-white text-sm">100%</span>
                  </div>
                  <div className="w-1/2 bg-[#18181b] border border-zinc-700 rounded p-2.5 flex justify-between items-center">
                    <span className="text-white text-sm">NORMAL</span>
                    <span className="text-zinc-500 text-xs">▼</span>
                  </div>
                </div>
              </div>
              <div className="pt-6 border-t border-zinc-800">
                <div className="text-xs font-bold text-zinc-500 mb-3 tracking-widest">FONT</div>
                <div className="bg-[#18181b] border border-zinc-700 rounded p-2.5 flex justify-between items-center mb-4">
                  <span className="text-white text-sm uppercase">JetBrains Mono</span>
                  <span className="text-zinc-500 text-xs">▼</span>
                </div>
                <div className="flex gap-3">
                  <div className="w-1/2">
                    <div className="text-xs font-bold text-zinc-500 mb-2 tracking-widest">STYLE</div>
                    <div className="bg-[#18181b] border border-zinc-700 rounded p-2.5 flex justify-between items-center">
                      <span className="text-white text-sm">MEDIUM</span>
                      <span className="text-zinc-500 text-xs">▼</span>
                    </div>
                  </div>
                  <div className="w-1/2">
                    <div className="text-xs font-bold text-zinc-500 mb-2 tracking-widest">SIZE</div>
                    <div className="bg-[#18181b] border border-zinc-700 rounded p-2.5">
                      <span className="text-white text-sm">12</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function LayerItem({ text, active, checked, onClick }: any) {
  return (
    <div 
      onClick={onClick}
      className={`flex items-center gap-3 p-3 rounded cursor-pointer transition-colors ${active ? 'bg-[#3f3f46]' : 'hover:bg-[#3f3f46]/50'}`}
    >
      <div className={`w-4 h-4 flex items-center justify-center border rounded-sm transition-colors ${checked ? 'bg-white border-white text-zinc-900' : 'border-zinc-500 text-transparent'}`}>
        <Check className="w-3 h-3" strokeWidth={4} />
      </div>
      <span className={`text-sm tracking-wide ${active ? 'text-white font-medium' : 'text-zinc-400'}`}>{text}</span>
    </div>
  );
}
