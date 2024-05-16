import { createApp } from 'vue'
import App from './App.vue'
import createRouterWithStore from './router'
import createStoreWithRouter from './store'

const store = createStoreWithRouter()
const router = createRouterWithStore(store)

createApp(App).use(store).use(router).mount('#app')
