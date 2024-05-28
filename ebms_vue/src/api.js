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

const api = {
  async get(url) {
    try {
      const response = await apiClient.get(url)
      return response.data
    } catch (error) {
      return null
    }
  },
  async post(url, data) {
    try {
      const response = await apiClient.post(url, data)
      return response.data
    } catch (error) {
      return null
    }
  },
  async login(data) {
    return this.post('/login/', data)
  },
  async logout() {
    return this.post('/logout/')
  },
  async register(data) {
    try {
      const response = await this.post('/users/', data)
      return response // Return the full response
    } catch (error) {
      if (error.response && error.response.data && error.response.data.email) {
        return { error: error.response.data.email[0] }
      } else {
        return { error: 'An unknown error occurred' }
      }
    }
  },
  getLoggedInUser() {
    return this.get('/whoami/')
  },
  async getUsers() {
    return this.get('/users/')
  },
  async getUserById(id) {
    let url = `/users/${id}/`
    return this.get(url)
  },
  async postUser(data) {
    let url = '/users/'
    return this.post(url, data)
  }
}

export default api
