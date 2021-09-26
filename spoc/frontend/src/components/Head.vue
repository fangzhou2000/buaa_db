<template>
  <h1>
    这是首页
    <p>
      <button v-on:click="goToLogin">返回</button>
    </p>
  </h1>
</template>

<script>
export default {
  methods: {
    goToLogin () {
      this.$router.replace('/Login')
    }
  }
}
</script>

<style scoped>

</style>
