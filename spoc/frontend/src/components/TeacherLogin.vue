<template>
  <div class="TeacherLogin">
    <h1>
      老师登录页面
    </h1>
    <p>
      <input type="text" placeholder="请输入工号" ref="userName">
    </p>
    <p>
      <input type="text" placeholder="请输入密码" ref="userPassWord">
    </p>
    <button v-on:click="goToTeacherHead">登录</button>
    <button v-on:click="goToTeacherRegister">注册</button>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'TeacherLogin',
  data: function () {
    return {
      status: -1
    }
  },
  methods: {
    goToTeacherHead: function () {
      let _this = this
      let userName = _this.$refs.userName.value
      let userPassWord = _this.$refs.userPassWord.value
      this.$http.request({
        url: _this.$url + 'TeacherLogin/',
        method: 'get',
        params: {
          userName,
          userPassWord
        }
      }).then(function (response) {
        console.log(response)
        _this.status = response.data
        if (_this.status === 0) {
          _this.$router.push({
            name: 'TeacherHead',
            params: {
              userName: _this.userName
            }
          })
        } else if (_this.status === 1) {
          alert('工号不存在')
        } else if (_this.status === 2) {
          alert('密码错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    goToTeacherRegister: function () {
      this.$router.push({
        name: 'TeacherRegister'
      })
    }
  }
}
</script>

<style scoped>

</style>
