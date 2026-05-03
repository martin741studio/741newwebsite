import { motion } from "motion/react";

const LOGOS = [
  { name: "Reload Sanctuary", src: "/assets/logos/reload_sanctuary.png", invert: true },
  { name: "The Lawn", src: "/assets/logos/the_lawn.png" },
  { name: "Werbeagentur Bamberger", src: "/assets/logos/werbeagentur_bamberger.svg", invert: true },
  { name: "TalkinFive", src: "/assets/logos/talkinfive.png" },
  { name: "Single Fin Bali", src: "/assets/logos/single_fin_bali.png", invert: true },
  { name: "Avli Bali", src: "/assets/logos/avli_bali.webp" },
  { name: "Numero Quattro", src: "/assets/logos/numero_quattro.png" },
  { name: "Zyklusmentorin", src: "/assets/logos/zyklusmentorin.png" },
  { name: "Versance AI", src: "/assets/logos/versance.svg" },
  { name: "Tacheles Beratung", src: "/assets/logos/tacheles_beratung.png" },
  { name: "Immokauf.at", src: "/assets/logos/immokauf.svg" },
  { name: "Karin Lorenz TCM", src: "/assets/logos/karin_lorenz.svg" },
  { name: "Marugame Udon", src: "/assets/logos/marugame_udon.svg" },
  { name: "WBG Nürnberg", src: "/assets/logos/wbg_nurnberg.svg" },
  { name: "Lucky Loop", src: "/assets/logos/luckyloop.png" },
  { name: "Vertrauenszentrum", src: "/assets/logos/vertrauenszentrum.png" },
  { name: "Vesta Noris", src: "/assets/logos/vesta_noris.png" },
  { name: "Marina Development Indonesia", src: "/assets/logos/marina_development.svg" },
];

export default function Logos() {
  return (
    <section className="py-16 border-y border-zinc-200 bg-white overflow-hidden">
      <div className="max-w-7xl mx-auto px-6">
        <p className="text-center text-sm font-medium text-zinc-400 mb-12 uppercase tracking-[0.2em]">
          Trusted by Industry Leaders
        </p>
        <div className="flex overflow-hidden relative group">
          {/* Gradient Masks */}
          <div className="absolute left-0 top-0 bottom-0 w-40 bg-gradient-to-r from-white via-white/80 to-transparent z-10" />
          <div className="absolute right-0 top-0 bottom-0 w-40 bg-gradient-to-l from-white via-white/80 to-transparent z-10" />

          <motion.div
            animate={{ x: [0, -2000] }}
            transition={{
              repeat: Infinity,
              ease: "linear",
              duration: 40,
            }}
            className="flex gap-20 items-center whitespace-nowrap"
          >
            {[...LOGOS, ...LOGOS, ...LOGOS, ...LOGOS].map((logo, i) => (
              <div key={i} className="flex-shrink-0 flex items-center justify-center">
                <img
                  src={logo.src}
                  alt={logo.name}
                  className={`
                    h-10 w-auto object-contain
                    transition-all duration-700 ease-in-out
                    opacity-40 grayscale group-hover:opacity-100 group-hover:grayscale-0
                    ${logo.invert ? 'brightness-0' : ''}
                    hover:scale-110
                  `}
                />
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </section>
  );
}
