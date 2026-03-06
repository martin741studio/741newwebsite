import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import handlebars from 'vite-plugin-handlebars';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, '.', '');
  return {
    root: '04_site',
    build: {
      outDir: '../dist',
      emptyOutDir: true,
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, '04_site/index.html'),
          localSeo: path.resolve(__dirname, '04_site/pages/local-seo.html'),
          about: path.resolve(__dirname, '04_site/pages/about.html'),
          faq: path.resolve(__dirname, '04_site/pages/faq.html'),
          portfolio: path.resolve(__dirname, '04_site/pages/portfolio_full.html'),
        },
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
