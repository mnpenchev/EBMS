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
    <p v-if="!emailIsValid" class="error">Invalid email address</p>
    <p>Don't have an account? <router-link to="/register">Register</router-link></p>
  </form>
</template>

<script>
import { isValidEmail } from '@/validators'
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
      return isValidEmail(this.email)
    }
  },
  methods: {
    ...mapActions(['login']),
    async submitForm() {
      const success = await this.login({ email: this.email, password: this.password })
      if (success) {
        this.$router.push('/home')
      } else {
        alert('Login failed. Please check your email and password.')
      }
    }
  }
}
</script>

<style>
.error {
  color: red;
}
</style>
