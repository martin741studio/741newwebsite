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
