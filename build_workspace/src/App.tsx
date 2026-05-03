/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Logos from "./components/Logos";
import Services from "./components/Services";
import WhyChooseUs from "./components/WhyChooseUs";
import ValueProp from "./components/ValueProp";
import ConceptToResults from "./components/Testimonials";
import ContactForm from "./components/ContactForm";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-white text-zinc-950 selection:bg-brand/30">
      <Navbar />
      <main>
        <Hero />
        <Logos />
        <Services />
        <WhyChooseUs />
        <ValueProp />
        <ConceptToResults />
        <ContactForm />
      </main>
      <Footer />
    </div>
  );
}
