"""Build the me&you Impressum page (desktop 1440 px). Statutory page, not marketing copy: text is
reproduced verbatim from the live page, only the Geschäftsführer name changed (Martin, 2026-10-19).
Design + text source: ../../rechtliches_build.py and ../../rechtliches_quelltext.py. Run: python3 build.py"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rechtliches_build', os.path.join(HERE, '..', '..', 'rechtliches_build.py'))
rb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rb)

if __name__ == '__main__':
    out = rb.page(rb.src.IMPRESSUM)
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
