import { createRouter, createWebHistory } from 'vue-router'
import LinkShortener from '../views/LinkShortener.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LinkShortener',
      component: LinkShortener
    },
  ]
})

export default router
