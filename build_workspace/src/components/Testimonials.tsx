import { motion, AnimatePresence } from "motion/react";
import { useState, useEffect } from "react";
import { Check, Flame, Rocket, Star, Target, Zap } from "lucide-react";

const TASKS = [
  { id: 1, text: "Define Strategy & Positioning", icon: <Target className="w-4 h-4" /> },
  { id: 2, text: "High-Performance Web Design", icon: <Zap className="w-4 h-4" /> },
  { id: 3, text: "SEO & Global Dominance", icon: <Star className="w-4 h-4" /> },
  { id: 4, text: "Social Media Authority", icon: <Flame className="w-4 h-4" /> },
  { id: 5, text: "Automation & Growth Systems", icon: <Rocket className="w-4 h-4" /> },
];

export default function ConceptToResults() {
  const [isResultMode, setIsResultMode] = useState(false);
  const [showConfetti, setShowConfetti] = useState(false);

  useEffect(() => {
    if (isResultMode) {
      setShowConfetti(true);
      const timer = setTimeout(() => setShowConfetti(false), 3000);
      return () => clearTimeout(timer);
    }
  }, [isResultMode]);

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
        {/* Toggle Header */}
        <div className="flex flex-col md:flex-row items-center justify-center gap-6 mb-24">
          <h2 className={`text-5xl md:text-7xl lg:text-[90px] font-display tracking-tight transition-colors duration-500 ${!isResultMode ? 'text-zinc-900' : 'text-zinc-300'}`}>
            From your idea
          </h2>

          <button
            onClick={() => setIsResultMode(!isResultMode)}
            className="w-28 h-14 rounded-full bg-zinc-200 p-1.5 flex items-center relative cursor-pointer border border-zinc-300 transition-colors hover:bg-zinc-300 shadow-inner"
          >
            <motion.div
              animate={{
                x: isResultMode ? 56 : 0,
                backgroundColor: isResultMode ? "#7c3aed" : "#71717a"
              }}
              className="w-11 h-11 rounded-full shadow-lg flex items-center justify-center text-white"
            >
              {isResultMode ? <Zap className="w-5 h-5 fill-current" /> : <Star className="w-5 h-5" />}
            </motion.div>
          </button>

          <h2 className={`text-5xl md:text-7xl lg:text-[90px] font-display tracking-tight transition-colors duration-500 ${isResultMode ? 'text-zinc-900' : 'text-zinc-300'}`}>
            to reaching customers
          </h2>
        </div>

        <div className="max-w-4xl mx-auto relative">
          <AnimatePresence>
            {showConfetti && <ConfettiCanvas />}
          </AnimatePresence>

          <div className="bg-white rounded-[2.5rem] p-10 md:p-16 shadow-2xl border border-zinc-200/50 relative overflow-hidden">
            {/* Minimal Dashboard Header */}
            <div className="flex items-center justify-between mb-12 border-b border-zinc-100 pb-8">
              <div>
                <h3 className="text-2xl font-display font-medium text-zinc-900">Project Operations</h3>
                <p className="text-zinc-500 text-sm">741 Studio Execution Pipeline</p>
              </div>
              <div className="flex gap-2">
                <div className={`px-4 py-2 rounded-full text-xs font-bold tracking-widest uppercase transition-colors ${isResultMode ? 'bg-green-100 text-green-700' : 'bg-zinc-100 text-zinc-500'}`}>
                  {isResultMode ? "System Active" : "Planning Phase"}
                </div>
              </div>
            </div>

            {/* The To-Do List */}
            <div className="space-y-4">
              {TASKS.map((task, index) => (
                <motion.div
                  key={task.id}
                  initial={false}
                  animate={{
                    opacity: 1,
                    x: 0,
                    scale: 1
                  }}
                  className={`flex items-center gap-6 p-6 rounded-2xl border transition-all duration-500 ${isResultMode
                      ? 'bg-zinc-50 border-zinc-200'
                      : 'bg-white border-zinc-100 opacity-60'
                    }`}
                >
                  <motion.div
                    animate={{
                      backgroundColor: isResultMode ? "#22c55e" : "#f4f4f5",
                      borderColor: isResultMode ? "#22c55e" : "#e4e4e7",
                      scale: isResultMode ? [1, 1.2, 1] : 1
                    }}
                    transition={{ delay: index * 0.1 }}
                    className="w-10 h-10 rounded-full border-2 flex items-center justify-center shrink-0"
                  >
                    <AnimatePresence mode="wait">
                      {isResultMode ? (
                        <motion.div
                          key="check"
                          initial={{ scale: 0, opacity: 0 }}
                          animate={{ scale: 1, opacity: 1 }}
                          exit={{ scale: 0, opacity: 0 }}
                        >
                          <Check className="w-5 h-5 text-white" strokeWidth={4} />
                        </motion.div>
                      ) : (
                        <motion.div
                          key="icon"
                          className="text-zinc-400"
                        >
                          {task.icon}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </motion.div>

                  <div className="flex-1">
                    <motion.p
                      animate={{
                        color: isResultMode ? "#18181b" : "#71717a",
                        textDecoration: isResultMode ? "line-through" : "none"
                      }}
                      className="text-xl font-medium tracking-tight"
                    >
                      {task.text}
                    </motion.p>
                  </div>

                  {isResultMode && (
                    <motion.div
                      initial={{ opacity: 0, x: -10 }}
                      animate={{ opacity: 1, x: 0 }}
                      className="text-[10px] font-bold text-green-600 uppercase tracking-widest bg-green-50 px-3 py-1 rounded-full"
                    >
                      Done
                    </motion.div>
                  )}
                </motion.div>
              ))}
            </div>

            {/* Celebration State */}
            <AnimatePresence>
              {isResultMode && (
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="mt-12 text-center"
                >
                  <p className="text-zinc-500 italic mb-4">"Scale unlocked. The engine is running."</p>
                  <div className="inline-flex items-center gap-2 px-6 py-3 bg-violet-600 text-white rounded-full font-bold uppercase tracking-widest text-sm shadow-xl shadow-violet-200">
                    <Rocket className="w-4 h-4" />
                    Launch Successful
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}

function ConfettiCanvas() {
  return (
    <div className="absolute inset-0 z-50 pointer-events-none overflow-hidden">
      {[...Array(40)].map((_, i) => (
        <motion.div
          key={i}
          initial={{
            opacity: 1,
            scale: 0,
            x: "50%",
            y: "50%",
            rotate: 0
          }}
          animate={{
            opacity: 0,
            scale: [0, 1.5, 0],
            x: `${50 + (Math.random() - 0.5) * 100}%`,
            y: `${50 + (Math.random() - 0.5) * 100}%`,
            rotate: Math.random() * 360
          }}
          transition={{
            duration: 1.5,
            ease: "easeOut",
            delay: Math.random() * 0.2
          }}
          className={`absolute w-3 h-3 rounded-full ${['bg-yellow-400', 'bg-violet-400', 'bg-green-400', 'bg-blue-400'][i % 4]}`}
        />
      ))}
    </div>
  );
}
