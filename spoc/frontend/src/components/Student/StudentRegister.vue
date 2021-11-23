<template>
  <transition name="head-login-register">
    <div class="background">
    <br>
    <div class="register_block">
      <div class="register_head">
        <p>学生注册</p>
      </div>
      <el-form rules="rules">
        <div id="register-n">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入姓名" v-model="userNickName" clearable></el-input>
          </el-form-item>
        </div>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入学号" v-model="userName" clearable></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入密码" v-model="userPassWord" show-password clearable></el-input>
          </el-form-item>
        </div>
        <div id="confirm-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请确认密码" v-model="userPassWord2" show-password clearable></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="Register">
              确认
            </el-button>
        </div>
        <div class="return-button">
            <el-button id="button_re" type="primary" plain="true" size="small" v-on:click="goToStudentLogin">
              返回
            </el-button>
        </div>
      </el-form>
    </div>
  </div>
  </transition>
</template>

<script>
export default {
  name: 'StudentRegister',
  data: function () {
    return {
      status: -1,
      userNickName: '',
      userName: '',
      userPassWord: '',
      userPassWord2: ''
    }
  },
  mounted () {
    window.addEventListener('keydown', this.keydown)
  },
  methods: {
    goToStudentLogin: function () {
      this.$router.push({
        name: 'StudentLogin'
      })
    },
    Register: function () {
      let that = this
      if (that.userPassWord === '') {
        that.$message.error('密码不能为空')
      } else if (that.userName === '') {
        that.$message.error('用户名不能为空')
      } else if (that.userNickName === '') {
        that.$message.error('请添加您的昵称')
      } else {
        this.$http.request({
          url: that.$url + 'StudentRegister/',
          method: 'get',
          params: {
            userNickName: that.userNickName,
            userName: that.userName,
            userPassWord: that.userPassWord,
            userPassWord2: that.userPassWord2
          }
        }).then(function (response) {
          console.log(response)
          that.status = response.data
          if (that.status === 0) {
            that.$router.push({
              name: 'StudentLogin',
              params: {
                userName: that.userName
              }
            })
          } else if (that.status === 1) {
            that.$message.error('学号已存在')
          } else if (that.status === 2) {
            that.$message.error('密码不一致')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.Register()
      }
    }
  },
  destroyed () {
    window.removeEventListener('keydown', this.keydown, false)
  }
}
</script>

<style scoped>
  @import "../../assets/css/register.css";
  @import "../../assets/css/Transition/head-login-register.css";
</style>
