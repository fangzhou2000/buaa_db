<template>
  <div class="StudentLogin">
    <h1>
      学生登录页面
    </h1>
    <p>
      <input type="text" placeholder="请输入学号" ref="userName">
    </p>
    <p>
      <input type="text" placeholder="请输入密码" ref="userPassWord">
    </p>
    <p>
      <button v-on:click="goToStudentHead">登录</button>
    </p>
    <p>
      <button v-on:click="goToStudentRegister">注册</button>
    </p>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'StudentLogin',
  data: function () {
    return {
      status: -1
    }
  },
  methods: {
    goToStudentHead: function () {
      let _this = this
      let userName = _this.$refs.userName.value
      let userPassWord = _this.$refs.userPassWord.value
      this.$http.request({
        url: _this.$url + 'StudentLogin/',
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
            name: 'StudentHead',
            params: {
              userName: _this.userName
            }
          })
        } else if (_this.status === 1) {
          alert('学号不存在')
        } else if (_this.status === 2) {
          alert('密码错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    goToStudentRegister: function () {
      this.$router.push({
        name: 'StudentRegister'
      })
    }
  }
}
</script>

<style scoped>

</style>
