<template>
  <div class="home">
    <div v-if="currentUser">
      Hi {{ currentUser.first_name }} {{ currentUser.last_name }}
      Your e-mail is: {{ currentUser.email }}
    </div>
    <div v-else>
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
