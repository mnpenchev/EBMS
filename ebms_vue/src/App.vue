<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Enterprise Business Management System</strong></router-link>
      </div>
      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <div v-if="isLoggedIn">
            <router-link to="/home" class="navbar-item">Profile</router-link>
            <button @click="logout" class="navbar-item">Logout</button>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2024</p>
      <router-link to="/about" class="navbar-item">About</router-link>
    </footer>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['currentUser', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['logout'])
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>