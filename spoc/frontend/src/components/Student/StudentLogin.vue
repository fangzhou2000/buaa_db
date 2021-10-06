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
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  methods: {
    goToStudentHead: function () {
      let that = this
      that.userName = that.$refs.userName.value
      that.userPassWord = that.$refs.userPassWord.value
      /*if (that.userName === 'admin' && that.userPassWord === '123456') {
        that.$router.push({
            name: 'StudentHead',
            params: {
              userName: that.userName
            }
          })
        console.log('from:' + that.userName)
      } else {
        alert('!')
      }*/
      this.$http.request({
        url: that.$url + 'StudentLogin/',
        method: 'get',
        params: {
          userName: that.userName,
          userPassWord: that.userPassWord
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          that.$router.push({
            name: 'StudentHead',
            params: {
              userName: that.userName
            }
          })
        } else if (that.status === 1) {
          alert('学号不存在')
        } else if (that.status === 2) {
          alert('密码错误')
        } else {
          alert('请输入学号')
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
