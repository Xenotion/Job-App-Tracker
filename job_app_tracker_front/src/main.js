import { createApp } from 'vue'
import MainLayout from './MainLayout.vue' // Import the new component
import axios from 'axios'
import router from './router'

const app = createApp(MainLayout) // Use MainLayout as root component
app.config.globalProperties.$http = axios;
app.use(router)
app.mount('#app')
