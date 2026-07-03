import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'node:path'

// https://vite.dev/config/
export default defineConfig({
  base: '/static/frontend/',
  plugins: [vue()],
  build: {
    outDir: '../static/frontend',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        index: resolve(__dirname, 'index.html'),
        product: resolve(__dirname, 'product.html'),
        factory: resolve(__dirname, 'factory.html'),
        custom: resolve(__dirname, 'custom.html'),
        contact: resolve(__dirname, 'contact.html'),
      },
    },
  },
})
