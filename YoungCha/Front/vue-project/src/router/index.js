import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import HomeView from '../views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieListView from '@/views/MovieListView.vue'
import RecommendedView from '@/views/RecommendedView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import CommunityCreateView from '@/views/CommunityCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieComments from '@/views/MovieComments.vue'
import Profile from '@/views/Profile.vue'
import AccountView from '@/views/AccountView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
   {
    path: '/movies',
    name: 'movies',
    component: MovieListView
   },

   {
    path: '/movie/:movieId',
    name: 'movieId',
    component: MovieDetailView,
    props: true,
   },
   {
    path: '/review-search',
    name: 'Search',
    component: ReviewSearchView
   },
   {
    path: '/recommended',
    name: 'Recommend',
    component: RecommendedView
   },
   {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/:id',
    name: 'CommunityDetailView',
    component: CommunityDetailView
  },
  {
    path: '/community/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
  path: '/movie/:movieId/comments/',
  name: 'comment',
  component: MovieComments,
 },
 {
  path: '/profile/:nickname/',
  name: 'profile',
  component: Profile,
 },
 {
  path: '/account/:username/',
  name: 'account',
  component: AccountView,
 }

  ]
})
console.log(Profile)
router.beforeEach((to, from) => {
  const store = useCounterStore()
  if ((to.name === 'SignUpView') && store.isLogin) {
    return { name: 'home'}
  }
})


export default router
