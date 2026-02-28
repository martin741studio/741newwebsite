import { motion } from "motion/react";
import { Send } from "lucide-react";

export default function ContactForm() {
  return (
    <section id="contact" className="py-32 bg-white relative overflow-hidden">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-fuchsia-200/50 rounded-full blur-[120px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <div>
            <motion.h2 
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-4xl md:text-6xl font-display font-bold text-zinc-950 mb-6 leading-tight"
            >
              Get Your Free <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-fuchsia-600">
                Digital Audit
              </span>
            </motion.h2>
            <motion.p 
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1 }}
              className="text-xl text-zinc-600 max-w-xl mb-12"
            >
              Ready to take your local business to the next level? Fill out the form below and our experts will analyze your current online presence for free.
            </motion.p>

            <div className="space-y-6">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-zinc-100 flex items-center justify-center border border-zinc-200">
                  <svg className="w-5 h-5 text-violet-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <div className="text-sm text-zinc-500">Email Us</div>
                  <div className="text-lg font-medium text-zinc-950">hello@741.studio</div>
                </div>
              </div>
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-zinc-100 flex items-center justify-center border border-zinc-200">
                  <svg className="w-5 h-5 text-fuchsia-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <div className="text-sm text-zinc-500">Visit Us</div>
                  <div className="text-lg font-medium text-zinc-950">Berlin & Bali</div>
                </div>
              </div>
            </div>
          </div>

          <motion.div 
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="bg-white/80 backdrop-blur-md border border-zinc-200 p-8 md:p-12 rounded-[2rem] shadow-2xl shadow-zinc-200/50"
          >
            <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
              <div className="grid grid-cols-2 gap-6">
                <div className="space-y-2">
                  <label className="text-sm font-medium text-zinc-600">First Name</label>
                  <input 
                    type="text" 
                    className="w-full bg-white border border-zinc-200 rounded-xl px-4 py-3 text-zinc-950 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all"
                    placeholder="John"
                  />
                </div>
                <div className="space-y-2">
                  <label className="text-sm font-medium text-zinc-600">Last Name</label>
                  <input 
                    type="text" 
                    className="w-full bg-white border border-zinc-200 rounded-xl px-4 py-3 text-zinc-950 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all"
                    placeholder="Doe"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium text-zinc-600">Work Email</label>
                <input 
                  type="email" 
                  className="w-full bg-white border border-zinc-200 rounded-xl px-4 py-3 text-zinc-950 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all"
                  placeholder="john@company.com"
                />
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium text-zinc-600">Website URL</label>
                <input 
                  type="url" 
                  className="w-full bg-white border border-zinc-200 rounded-xl px-4 py-3 text-zinc-950 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all"
                  placeholder="https://yourwebsite.com"
                />
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium text-zinc-600">How can we help?</label>
                <textarea 
                  rows={4}
                  className="w-full bg-white border border-zinc-200 rounded-xl px-4 py-3 text-zinc-950 focus:outline-none focus:ring-2 focus:ring-violet-500 transition-all resize-none"
                  placeholder="Tell us about your goals..."
                />
              </div>

              <button className="w-full bg-zinc-950 text-white font-bold text-lg rounded-full px-6 py-4 flex items-center justify-center gap-2 hover:bg-zinc-800 transition-all hover:scale-[1.02] active:scale-[0.98]">
                Request Free Audit
                <Send className="w-5 h-5" />
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
