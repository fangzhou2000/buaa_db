<template>
  <div class="StudentRegister">
    <h1>
      学生注册页面
    </h1>
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
        <button v-on:click="goToStudentLogin">返回</button>
    </p>
  </div>
</template>

<script>
export default {
  name: 'StudentRegister',
  data: function () {
    return {
      status: -1
    }
  },
  methods: {
    goToStudentLogin: function() {
      this.$router.push({
        name: 'StudentLogin'
      })
    },
    Register: function() {
      let _this = this
      let userName = _this.$refs.userName.value
      let userPassWord = _this.$refs.userPassWord.value
      let userPassWord2 = _this.$refs.userPassWord2.value
      this.$http.request({
        url: _this.$url + 'StudentRegister/',
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
            name: 'StudentLogin',
            params: {
              userName: _this.userName
            }
          })
        } else if (_this.status === 1) {
          alert('学号已存在')
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
