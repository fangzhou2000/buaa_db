<template>
  <h1>
    这是注册页面
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
 p{
   display: block;
   background-color: #2c3e50;
 }
</style>
