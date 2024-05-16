<template>
  <div class="home">
    <div v-if="currentUser">
      <h1>This is an about page</h1>
    </div>
    <div v-else>
      <h1>This is an about page</h1>
      <router-link to="/">Please log in.</router-link>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentUser() {
      return this.$store.state.currentUser;
    }
  }
}
</script>