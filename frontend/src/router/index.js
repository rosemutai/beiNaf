import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Orbituaries from '../views/Orbituaries.vue'
import OrbituaryDetail from '../views/OrbituaryDetail.vue'
import Contact from '../views/Contact.vue'
import Services from '../views/Services.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },

  {
    path: '/orbituaries',
    name: 'Orbituaries',
    component: Orbituaries
  },

  {
    path: '/orbituaries/:id',
    name: 'OrbituaryDetail',
    props: true,
    component: OrbituaryDetail
  },

  
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },

  {
    path: '/services',
    name: 'Services',
    component: Services
  },

]

const router = createRouter({
  mode: 'history',
  history: createWebHashHistory(),
  routes
})

export default router
