// Example of how to use Vue Router

import { createRouter, createWebHistory } from 'vue-router'

// 1. Define route components.
// These can be imported from other files
import MainPage from '../pages/MainPage.vue';
import AccountPage from '../pages/AccountPage.vue';
import ExpandedArticle from '../pages/ExpandedArticle.vue';

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Main Page', component: MainPage },
        { path: '/account/', name: 'Account Page', component: AccountPage },
        { path: '/Article/', name: 'Expanded Article', component: ExpandedArticle },
    ]
})

export default router
