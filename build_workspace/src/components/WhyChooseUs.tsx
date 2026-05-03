import { useState } from "react";

const TOOLS = [
  { id: "invert", label: "Invert", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/68224563d93b3ce65b54f07b_Invert%402x.avif" },
  { id: "outpaint", label: "Outpaint", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/6822456436dd3ce4b39b6372_Outpaint%402x.avif" },
  { id: "crop", label: "Crop", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/68224563af147b5d7c2496ff_Crop%402x.avif" },
  { id: "inpaint", label: "Inpaint", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682245639e16941f61edcc06_Inpaint%402x.avif" },
  { id: "mask", label: "Mask extractor", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/68224563d5cb54c747f189ae_Mask%402x.avif" },
  { id: "painter", label: "Painter", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682245634dee7dac1dc3ac42_Painter%402x.avif" },
  { id: "relight", label: "Relight", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/68224563b4846eaa2d70f69e_Relight%402x.avif" },
  { id: "upscale", label: "Upscale", image: "https://cdn.prod.website-files.com/681b040781d5b5e278a69989/682245638e6550c59d0bce8f_Upscale%402x.avif" },
];

export default function WhyChooseUs() {
  const [activeTool, setActiveTool] = useState(TOOLS[1]); // Default to Outpaint

  return (
    <section id="why-us" className="section_prof-tools">
      <div className="padding-global">
        <div className="simple-container">
          <div className="padding-section-large">
            <div className="outcome_comp">

              <div className="tools-header-wrapper">
                <h2 className="heading-style-xl">
                  With all the professional tools you rely on
                </h2>
                <p className="text-size-large">
                  In one seamless workflow
                </p>
              </div>

              <div className="prof-tools-interactionable-wrapper">
                <div className="prof_center-image-wrapp">
                  {TOOLS.map((tool) => (
                    <img
                      key={tool.id}
                      src={tool.image}
                      loading="lazy"
                      alt={tool.label}
                      className={`image-tools-inner ${activeTool.id === tool.id ? 'active' : ''}`}
                    />
                  ))}
                </div>
              </div>

              <div className="prof-tools-chips-comp">
                {TOOLS.map((tool) => (
                  <div
                    key={tool.id}
                    className={`tool_chip ${activeTool.id === tool.id ? 'active' : ''}`}
                    onMouseEnter={() => setActiveTool(tool)}
                  >
                    <div className="pointer-events-none">
                      {tool.label}
                    </div>
                  </div>
                ))}
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
