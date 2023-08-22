import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './LandingPage.vue'
import App from './App.vue'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/jobs', component: App, meta: {hideLayout: true} }
]

// ... rest of your router.js file remains the same

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
