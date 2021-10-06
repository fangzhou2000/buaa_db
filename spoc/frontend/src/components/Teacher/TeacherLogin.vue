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
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  methods: {
    goToTeacherHead: function () {
      let that = this
      that.userName = that.$refs.userName.value
      that.userPassWord = that.$refs.userPassWord.value
      /*if (that.userName === 'admin' && that.userPassWord === '123456') {
        that.$router.push({
            name: 'TeacherHead',
            params: {
              userName: that.userName
            }
          })
        console.log('from:' + that.userName)
      } else {
        alert('!')
      }*/
      this.$http.request({
        url: that.$url + 'TeacherLogin/',
        method: 'get',
        params: {
          userName: that.userName,
          userPassWord: that.userPassWord
        }
      }).then(function (response) {
        console.log(response)
        that.status = response.data
        if (that.status === 0) {
          that.$router.push({
            name: 'TeacherHead',
            params: {
              userName: that.userName
            }
          })
        } else if (that.status === 1) {
          alert('工号不存在')
        } else if (that.status === 2) {
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
