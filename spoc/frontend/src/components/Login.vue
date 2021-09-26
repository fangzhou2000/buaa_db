<template>
  <div class="login">
    <h1>
      这是登录页面
    </h1>
    <p>
      <input type="text" placeholder="请输入用户名" v-model="userName">
    </p>
    <p>
      <input type="text" placeholder="请输入密码" v-model="userPassWord">
    </p>
    <button v-on:click="login">登录</button>
    <button v-on:click="goToRegister">注册</button>
  </div>

</template>

<script>
export default {
  methods: {
    goToRegister () {
      this.$router.replace('/Register')
    }
  }
}
</script>

<style scoped>

</style>
