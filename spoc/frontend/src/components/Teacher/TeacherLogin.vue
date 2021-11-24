<template>
  <transition name="head-login-register">
    <div class="background">
    <br>
    <div class="register_block">
      <div class="register_head">
        <p>教师登录</p>
      </div>
      <el-form>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入工号" v-model="userName" clearable></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入密码" v-model="userPassWord" show-password clearable></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="goToTeacherHead">
              确认
            </el-button>
        </div>
        <div class="register-button">
            <el-button id="button_re" type="primary" plain="true" size="small" v-on:click="goToTeacherRegister">
              注册
            </el-button>
        </div>
        <div class="return-text">
           <el-link href="#/" style="font-size: 8px; color: white">返回</el-link>
        </div>
      </el-form>
    </div>
  </div>
  </transition>
</template>

<script>
/* eslint-disable */
export default {
  name: 'TeacherLogin',
  data: function () {
    return {
      userNickName: '',
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keydown)
  },
  methods: {
    goToTeacherHead: function () {
      let that = this
      let debug = true
      if (debug) {
        if (that.userName === 'admin' && that.userPassWord === '123456') {
          let loginInfo = {userName: 'admin', userNickName: '前端测试教师'}
          that.cookie.setCookie(loginInfo)
          that.$router.push({
            name: 'TeacherHead',
          })
        } else {
          that.$message.error('!!!')
        }
      } else {
        this.$http.request({
          url: that.$url + 'TeacherLogin/',
          method: 'get',
          params: {
            userNickName: that.userNickName,
            userName: that.userName,
            userPassWord: that.userPassWord
          }
        }).then(function (response) {
          console.log(response)
          that.status = response.data.value
          if (that.status === 0) {
            let loginInfo = {userName: that.userName, userNickName: response.data.userNickName}
            that.cookie.setCookie(loginInfo)
            that.$router.push({
              name: 'TeacherHead',
            })
          } else if (that.status === 1) {
            that.$message.error('工号不存在')
          } else if (that.status === 2) {
            that.$message.error('密码错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    goToTeacherRegister: function () {
      this.$router.push({
        name: 'TeacherRegister'
      })
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.goToTeacherHead()
      }
    }
  },
  destroyed () {
    window.removeEventListener('keydown', this.keydown, false)
  }
}
</script>

<style scoped>
  @import "../../assets/css/login.css";
  @import "../../assets/css/Transition/head-login-register.css";
</style>
