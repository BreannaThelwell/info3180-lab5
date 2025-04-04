import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue' //AddMovieFormView component
import MoviesView from '../views/MoviesView.vue' //new route for MoviesView component

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/movies/create',   //new route for adding movie
      name: 'addmovie',
      component: AddMovieFormView
    },
    {
      path: '/movies',
      name: 'Movies',
      component: MoviesView
    }
  ]
})

export default router
