import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import api from '@/api'

export default function createStoreWithRouter() {
  const store = createStore({
    state: {
      currentUser: null,
      isLoggedIn: false,
    },
    mutations: {
      SET_CURRENT_USER(state, user) {
        state.currentUser = user
        state.isLoggedIn = !!user
      },
    },
    actions: {
      async login({ commit }, data) {
        try {
          const response = await api.login(data)
          if (response && response.token) {
            localStorage.setItem('user-token', response.token)
            commit('SET_CURRENT_USER', response.user)
            return true
          }
          return false
        } catch {
          return {error: "Login failed, check your email or password"}
        }
      },
      async logout({ commit }) {
        await api.logout()
        localStorage.removeItem('user-token')
        commit('SET_CURRENT_USER', null)
        return true
      },
      async register({ commit }, data) {
        try {
          const response = await api.register(data)
          if (response && response.email) {
            commit('SET_CURRENT_USER', response)
            return { success: true }
          } else if (response.error) {
            return { error: response.error }
          } else {
            return { error: 'Registration failed' }
          }
        } catch (error) {
          return { error: 'An unknown error occurred' }
        }
      },
      async checkUser({ commit }) {
        const token = localStorage.getItem('user-token')
        if (token) {
          const response = await api.getLoggedInUser()
          if (response && response.user) {
            commit('SET_CURRENT_USER', response.user)
          }
        }
      }
    },
    getters: {
      getUserById: (state) => (id) => {
        return state.users.find(user => user.id === parseInt(id))
      },
    },
    plugins: [createPersistedState({
      paths: ['currentUser', 'isLoggedIn']
    })]
  })
  store.dispatch('checkUser')

  return store
}
