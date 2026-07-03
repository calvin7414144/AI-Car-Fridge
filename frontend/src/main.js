import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

const page = document.body.dataset.page || 'home'

createApp(App, { page }).mount('#app')
