<template>
  <div class="login">
    <h1>
      这是登录页面
    </h1>
    <p>
      <input type="text" placeholder="请输入用户名" ref="userName">
    </p>
    <p>
      <input type="text" placeholder="请输入密码" ref="userPassWord">
    </p>
    <button v-on:click="goToHead">登录</button>
    <button v-on:click="goToRegister">注册</button>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Login',
  data: function () {
    return {
      status: -1
    }
  },
  methods: {
    goToHead: function () {
      let _this = this
      let userName = _this.$refs.userName.value
      let userPassWord = _this.$refs.userPassWord.value
      this.$http.request({
        url: _this.$url + 'Login/',
        method: 'get',
        params: {
          userName,
          userPassWord
        }
      }).then(function (response) {
        console.log(response)
        _this.status = response.data
        if (_this.status === 0) {
          _this.$router.replace('Head/')
        } else if (_this.status === 1) {
          alert('用户名不存在')
        } else if (_this.status === 2) {
          alert('密码错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    goToRegister: function () {
      this.$router.replace('/Register')
    }
  }
}
</script>

<style scoped>

</style>
