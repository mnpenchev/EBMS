import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Token ${localStorage.getItem('user-token')}`
  }
})

export default {
    async get(url) {
      try {
        const response = await apiClient.get(url)
        return response.data
      } catch (error) {
        console.error(error)
      }
    },
    async post(url, data) {
      try {
        const response = await apiClient.post(url, data)
        return response.data
      } catch (error) {
        console.error(error)
      }
    },
    async login(data) {
        return this.post('/login/', data)
    },
    async logout() {
        return this.post('/logout/')
    },
    getLoggedInUser() {
      return this.get('/whoami')
    },
    async getUsers() {
      return this.get('/users/')
    },
    getUserById(id) {
      let url = '/users/' + id + '/'
      return get(url)
    },
    postUser(data) {
      let url = '/users/'
      return post(url, data)
    }
  }
  