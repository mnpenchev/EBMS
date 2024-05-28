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
        <button type="submit">Register</button>
        <p>Already have an account? <router-link to="/">Login</router-link></p>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    data() {
        return {
            email: '',
            password: '',
            errorMessage: ''
        }
    },
    methods: {
    async submitForm() {
      const data = {
        email: this.email,
        password: this.password,
      }
      const result = await this.$store.dispatch('register', data)
      if (result && result.error) {
        this.errorMessage = result.error
      } else if (result && result.success) {
        this.errorMessage = ''
        this.$router.push('/home')
      } else {
        this.errorMessage = 'An unknown error occurred'
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
