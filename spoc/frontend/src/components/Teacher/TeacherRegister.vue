<template>
  <h1>
    老师注册页面
    <p>
      <input type="text" placeholder="请输入学号" ref="userName">
    </p>
    <p>
      <input type="text" placeholder="请输入密码" ref="userPassWord">
    </p>
    <p>
      <input type="text" placeholder="请确认密码" ref="userPassWord2">
    </p>
    <p>
        <button v-on:click="Register">确认</button>
    </p>
    <p>
        <button v-on:click="goToTeacherLogin">返回</button>
    </p>
  </h1>
</template>

<script>
export default {
  methods: {
    goToTeacherLogin: function () {
      this.$router.push({
        name: 'TeacherLogin'
      })
    },
    Register: function () {
      let _this = this
      let userName = _this.$refs.userName.value
      let userPassWord = _this.$refs.userPassWord.value
      let userPassWord2 = _this.$refs.userPassWord2.value
      this.$http.request({
        url: _this.$url + 'TeacherRegister/',
        method: 'get',
        params: {
          userName,
          userPassWord,
          userPassWord2
        }
      }).then(function (response) {
        console.log(response)
        _this.status = response.data
        if (_this.status === 0) {
          _this.$router.push({
            name: 'TeacherLogin',
            params: {
              userName: _this.userName
            }
          })
        } else if (_this.status === 1) {
          alert('工号已存在')
        } else if (_this.status === 2) {
          alert('密码不一致')
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
