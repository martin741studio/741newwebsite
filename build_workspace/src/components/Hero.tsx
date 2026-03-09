import { useRef, useState, useEffect } from "react";
import { motion, useMotionValue } from "motion/react";
import LeaderLine from "leader-line-new";

const NODE_DATA = [
  { id: "node1", label: "Acquisition & Demand", gridArea: "1 / 1 / 3 / 3" },
  { id: "node2", label: "Conversion Optimization", gridArea: "3 / 1 / 5 / 3" },
  { id: "node3", label: "Core Operations", gridArea: "1 / 3 / 3 / 5" },
  { id: "node4", label: "Tech & Automation", gridArea: "3 / 3 / 5 / 5" },
  { id: "node5", label: "Creative & Brand", gridArea: "3 / 5 / 5 / 7" },
  { id: "node6", label: "Profitable Growth", gridArea: "1 / 5 / 5 / 7" },
];

const CONNECTIONS = [
  { start: "node1", end: "node3" },
  { start: "node2", end: "node3" },
  { start: "node3", end: "node4" },
  { start: "node3", end: "node5" },
  { start: "node4", end: "node6" },
  { start: "node5", end: "node6" },
];

function Node({ id, label, gridArea }: { id: string; label: string; gridArea: string }) {
  const nodeRef = useRef<HTMLDivElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  return (
    <motion.div
      id={id}
      ref={nodeRef}
      style={{
        x,
        y,
        gridArea,
        backgroundColor: "white",
        color: "#252525",
        padding: "1.5vw 2vw",
        borderRadius: "0.7vw",
        cursor: "grab",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        fontSize: "1.2vw",
        fontWeight: "500",
        boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
        userSelect: "none",
        zIndex: 10,
        whiteSpace: "nowrap"
      }}
      drag
      dragMomentum={false}
      whileDrag={{ scale: 1.05, cursor: "grabbing" }}
      className="hr-card-3d node-connect"
    >
      {label}
    </motion.div>
  );
}

export default function Hero() {
  const [lines, setLines] = useState<LeaderLine[]>([]);

  useEffect(() => {
    const newLines = CONNECTIONS.map(conn => {
      const startEl = document.getElementById(conn.start);
      const endEl = document.getElementById(conn.end);
      if (startEl && endEl) {
        return new LeaderLine(startEl, endEl, {
          color: "#DEDEDE",
          size: 1.4,
          path: "fluid",
          startSocket: "right",
          endSocket: "left",
          startPlug: "disc",
          endPlug: "disc",
          startPlugColor: "#DEDEDE",
          startPlugSize: 3.5,
          startPlugOutline: true,
          startPlugOutlineColor: "#FFFFFF",
          endPlugColor: "#DEDEDE",
          endPlugSize: 3.5,
          endPlugOutline: true,
          endPlugOutlineColor: "#FFFFFF",
        });
      }
      return null;
    }).filter(Boolean) as LeaderLine[];

    setLines(newLines);

    const updateLines = () => {
      newLines.forEach(line => line.position());
    };

    window.addEventListener("scroll", updateLines);
    window.addEventListener("resize", updateLines);
    const interval = setInterval(updateLines, 16);

    return () => {
      newLines.forEach(line => line.remove());
      window.removeEventListener("scroll", updateLines);
      window.removeEventListener("resize", updateLines);
      clearInterval(interval);
    };
  }, []);

  return (
    <section className="section-hero">
      <div className="grid-container is-hero is-banner-top">
        <div className="div-block" />

        <div id="w-node-_54cd4306-560e-2f33-f07c-9009e4c604b4-78a6999f" className="h1-wrapper">
          <h1 className="heading_h1-hero">741.Studio</h1>
        </div>

        <div id="w-node-_5134b68b-08f8-d177-ea63-19167ba1aa94-78a6999f" className="vertical-wrapp">
          <div className="h1-wrapper extra-bot-pad">
            <h1 className="heading_h1-hero">Digital Excellence</h1>
          </div>
          <div id="w-node-_56bcb99c-0f2a-fed0-938f-1e64de8465f1-78a6999f" className="paragraph-wrapper p-max-width-23-875">
            <p className="text-size-large" style={{ marginTop: '2rem' }}>
              Turn your business vision into scalable results.
              We engineer strategic workflows, automation, and
              high-performance digital assets that compound.
            </p>
          </div>
        </div>

        <div id="w-node-ad200bf5-388c-5543-8832-565bb87fbb2f-78a6999f" className="hero-draggbles-comp" style={{ height: '50vw', position: 'relative' }}>
          {NODE_DATA.map((node) => (
            <Node key={node.id} {...node} />
          ))}
        </div>
      </div>
    </section>
  );
}
