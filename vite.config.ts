import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import handlebars from 'vite-plugin-handlebars';
import fs from 'fs';

// Helper to dynamically discover all HTML entry pages
function getHtmlInputs() {
  const inputs: Record<string, string> = {
    main: path.resolve(__dirname, '04_site/index.html'),
  };

  const pagesDir = path.resolve(__dirname, '04_site/pages');
  if (fs.existsSync(pagesDir)) {
    fs.readdirSync(pagesDir).forEach(file => {
      if (file.endsWith('.html')) {
        const key = file.replace('.html', '');
        inputs[key] = path.resolve(pagesDir, file);
      }
    });
  }

  const blogDir = path.resolve(__dirname, '04_site/pages/blog');
  if (fs.existsSync(blogDir)) {
    fs.readdirSync(blogDir).forEach(file => {
      if (file.endsWith('.html')) {
        const cleanName = file.replace('.html', '').replace(/-/g, '_');
        const key = `blog_${cleanName}`;
        inputs[key] = path.resolve(blogDir, file);
      }
    });
  }
  const deDir = path.resolve(__dirname, '04_site/de');
  if (fs.existsSync(deDir)) {
    inputs['de_main'] = path.resolve(deDir, 'index.html');
    
    const dePagesDir = path.resolve(deDir, 'pages');
    if (fs.existsSync(dePagesDir)) {
      fs.readdirSync(dePagesDir).forEach(file => {
        if (file.endsWith('.html')) {
          const key = 'de_' + file.replace('.html', '');
          inputs[key] = path.resolve(dePagesDir, file);
        }
      });
    }

    const deBlogDir = path.resolve(deDir, 'pages/blog');
    if (fs.existsSync(deBlogDir)) {
      fs.readdirSync(deBlogDir).forEach(file => {
        if (file.endsWith('.html')) {
          const cleanName = file.replace('.html', '').replace(/-/g, '_');
          const key = `de_blog_${cleanName}`;
          inputs[key] = path.resolve(deBlogDir, file);
        }
      });
    }
  }

  const reviewDir = path.resolve(__dirname, '04_site/review');
  if (fs.existsSync(reviewDir)) {
    const scanReview = (dir: string) => {
      fs.readdirSync(dir).forEach(file => {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
          scanReview(fullPath);
        } else if (file.endsWith('.html')) {
          const relKey = path.relative(reviewDir, fullPath).replace(/[\/\\]/g, '_').replace('.html', '');
          inputs[`review_${relKey}`] = fullPath;
        }
      });
    };
    scanReview(reviewDir);
  }

  const caseDir = path.resolve(__dirname, '04_site/case-studies');
  if (fs.existsSync(caseDir)) {
    const scanCase = (dir: string) => {
      fs.readdirSync(dir).forEach(file => {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
          scanCase(fullPath);
        } else if (file.endsWith('.html')) {
          const relKey = path.relative(caseDir, fullPath).replace(/[\/\\]/g, '_').replace('.html', '');
          inputs[`case_${relKey}`] = fullPath;
        }
      });
    };
    scanCase(caseDir);
  }

  return inputs;
}

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, '.', '');
  return {
    root: '04_site',
    build: {
      outDir: '../dist',
      emptyOutDir: true,
      rollupOptions: {
        input: getHtmlInputs(),
      },
    },
    plugins: [
      react(), 
      tailwindcss(),
      handlebars({
        partialDirectory: [
          path.resolve(__dirname, '04_site/components'),
          path.resolve(__dirname, '04_site/sections'),
        ],
      }) as any,
    ],
    define: {
      'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
    },
  };
});
