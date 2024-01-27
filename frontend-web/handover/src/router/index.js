import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Yumin from '../components/Yumin.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/yumin',
    name: 'Yumin',
    component: Yumin
  },  
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router