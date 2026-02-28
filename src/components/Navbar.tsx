import { useState, useEffect } from "react";

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div className="navbar_main">
      <div className="navbar-left">
        <a href="/" className="brand w-nav-brand">
          <div className="flex items-center gap-3">
            <span className="font-display font-medium text-[2.5rem] tracking-tight text-white uppercase">741.Studio</span>
            <div className="pl-4 border-l border-white/20 hidden md:block">
              <span className="font-display text-[1rem] tracking-widest text-white/60 uppercase leading-none block">Digital<br />Excellence</span>
            </div>
          </div>
        </a>
      </div>

      <div className="navbar-right">
        <div className="nav-bar-right">
          <div className="nav-links-wrapper">
            <a href="#services" className="nav_text-link">COLLECTIVE</a>
            <a href="#why-us" className="nav_text-link">ENTERPRISE</a>
            <a href="#testimonials" className="nav_text-link">Pricing</a>
            <a href="#contact" className="nav_text-link">Request a Demo</a>
            <a href="#contact" className="nav_text-link">Sign In</a>
          </div>
        </div>

        <div className="navbar_main-cta-wrapper">
          <div className="huge_nav-button-dummy">
            <div className="nav-button-spacer" />
            <div className="nav-link-text-block-large nav-normal-case">Start Now</div>
          </div>
        </div>
      </div>

      <a
        id="try_now_top"
        href="#contact"
        className={`huge_nav-button is-real w-inline-block transition-transform duration-300 ${isScrolled ? 'scale-75 translate-x-4 -translate-y-2' : ''}`}
      >
        <div className="nav-button-spacer" />
        <div className="nav-link-text-block-large nav-normal-case">Start Now</div>
      </a>
    </div>
  );
}
