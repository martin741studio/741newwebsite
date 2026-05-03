import { motion, useScroll } from "motion/react";
import { useState, useEffect, useRef } from "react";

const SERVICES_DATA = [
  { id: "web_design", title: "Web Design", video: "https://assets.741-studio.com/homepage/videos/wan.mp4" },
  { id: "development", title: "Development", video: "https://assets.741-studio.com/homepage/videos/wan.mp4" },
  { id: "local_seo", title: "Local SEO", video: "https://assets.741-studio.com/homepage/videos/runway_gen-4.mp4" },
  { id: "seo", title: "SEO", video: "https://assets.741-studio.com/homepage/videos/runway_gen-4.mp4" },
  { id: "social_media", title: "Social Media", video: "https://assets.741-studio.com/homepage/videos/Veo2.mp4" },
  { id: "strategy", title: "Strategy", video: "https://assets.741-studio.com/homepage/videos/Veo2.mp4" },
  { id: "branding", title: "Branding", video: "https://assets.741-studio.com/homepage/videos/kling.mp4" },
  { id: "automation", title: "Automation", video: "https://assets.741-studio.com/homepage/videos/kling.mp4" },
  { id: "ai_integration", title: "AI Integration", video: "https://assets.741-studio.com/homepage/videos/minimax_video.mp4" },
  { id: "client_acquisition", title: "Client Acquisition", video: "https://assets.741-studio.com/homepage/videos/luma_ray_2.mp4" },
];

export default function Services() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"]
  });

  const [activeIndex, setActiveIndex] = useState(0);

  useEffect(() => {
    return scrollYProgress.on("change", (latest) => {
      const index = Math.min(Math.floor(latest * SERVICES_DATA.length), SERVICES_DATA.length - 1);
      setActiveIndex(index);
    });
  }, [scrollYProgress]);

  return (
    <section id="services" ref={containerRef} className="section_models text-color-white">
      <div className="layout355_component">
        <div className="padding-global">
          <div className="container-large">
            <div className="padding-section-large is-models">
              <div className="layout62_component">
                <div className="w-layout-grid models_content">

                  <div className="models_content-left">
                    <h2 className="heading-style-xl">
                      741 Studio builds complete digital growth systems
                    </h2>
                    <p className="paragraph-line-height-1-15 text-size-large">
                      Strategic assets and high-performance workflows in one seamless architecture.
                      Scale your impact without losing quality.
                    </p>
                  </div>

                  <div className="models_content-right">
                    <div className="w-layout-grid models_item-list">
                      {SERVICES_DATA.map((service, index) => (
                        <div
                          key={service.id}
                          className={`models_item ${activeIndex === index ? 'is-active' : ''}`}
                        >
                          <h3 className="heading-style-xl pointer-events-none">
                            {service.title}
                          </h3>
                        </div>
                      ))}
                    </div>
                  </div>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Background Layer */}
      <div className="models_bg-image-layer" style={{ position: 'fixed', inset: 0, zIndex: -1 }}>
        <div className="image-overlay-layer" />
        {SERVICES_DATA.map((service, index) => (
          <motion.div
            key={`${service.id}-bg`}
            initial={{ opacity: 0 }}
            animate={{ opacity: activeIndex === index ? 1 : 0 }}
            transition={{ duration: 0.8 }}
            className="absolute inset-0 w-full h-full"
          >
            <video
              src={service.video}
              autoPlay muted loop playsInline
              className="models_bg-image"
              style={{ objectFit: 'cover', width: '100%', height: '100%' }}
            />
          </motion.div>
        ))}
      </div>
    </section>
  );
}
