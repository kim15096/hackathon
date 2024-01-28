import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Yumin from '../components/Yumin.vue'
import Items from '../components/Items.vue'
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
  {
    path: '/items',
    name: 'Items',
    component: Items
  },
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router