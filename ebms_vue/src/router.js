import { createRouter, createWebHistory } from 'vue-router'

export default function createRouterWithStore(store) {
  const routes = [
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/',
      name: 'Login',
      component: () => import('@/views/LoginForm.vue')
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/RegisterView.vue')
    },
  ]

  const router = createRouter({
    history: createWebHistory(),
    routes
  })

  router.beforeEach((to, from, next) => {
    const loggedInPages = ['/', '/users']
    const loggedIn = store.state.isLoggedIn
  
    if (loggedInPages.includes(to.path) && loggedIn) {
      return next('/home')
    }
  
    next()
  })

  return router
}
