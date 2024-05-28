<template>
    <form @submit.prevent="submitForm">
      <label>
        Email:
        <input type="email" v-model="email" required>
      </label>
      <label>
        Password:
        <input type="password" v-model="password" required>
      </label>
      <button type="submit" :disabled="!emailIsValid || !password">Login</button>
      <p>Don't have an account? <router-link to="/register">Register</router-link></p>
    </form>
  </template>

<script>
import { mapActions } from 'vuex'
  
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  computed: {
    emailIsValid() {
      const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
      return re.test(this.email)
    }
  },
  methods: {
    ...mapActions(['login']),
    async submitForm() {
      const success = await this.login({ email: this.email, password: this.password })
      if (success) {
        this.$router.push('/home')
      } else {
        alert(user.error)
      }
    }
  }
}
</script>
  