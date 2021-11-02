<template>
  <div class="background">
    <br>
    <div class="register_block">
      <div class="register_head">
        <p>学生登录</p>
      </div>
      <el-form>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入学号" v-model="userName"></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入密码" v-model="userPassWord" show-password></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="goToStudentHead">
              确认
            </el-button>
        </div>
        <div class="register-button">
            <el-button id="button_re" type="primary" plain="true" size="small" v-on:click="goToStudentRegister">
              注册
            </el-button>
        </div>
        <div class="return-text">
           <el-link href="#/">返回</el-link>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'StudentLogin',
  data: function () {
    return {
      userNickName: '',
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  methods: {
    goToStudentHead: function () {
      let that = this
      let debug = false
      if (debug) {
        if (that.userName === 'admin' && that.userPassWord === '123456') {
          that.$router.push({
            name: 'StudentHead',
            params: {
              userName: that.userName
            }
          })
          console.log('from:' + that.userName)
        } else {
          that.$message.error('!')
        }
      } else {
        this.$http.request({
          url: that.$url + 'StudentLogin/',
          method: 'get',
          params: {
            userNickName: that.userNickName,
            userName: that.userName,
            userPassWord: that.userPassWord
          }
        }).then(function (response) {
          console.log(response.data)
          that.status = response.data.value
          if (that.status === 0) {
            let loginInfo = {userName: that.userName, userNickName: response.data.userNickName}
            that.cookie.setCookie(loginInfo)
            that.$router.push({
              name: 'StudentHead'
            })
          } else if (that.status === 1) {
            that.$message.error('学号不存在')
          } else if (that.status === 2) {
            that.$message.error('密码错误')
          } else {
            that.$message.info('请输入学号')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
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
  @import "../../assets/css/login.css";
</style>
