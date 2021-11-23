<template>
  <transition name="head-login-register">
    <div class="background">
    <br>
    <div class="register_block">
      <div class="register_head">
        <p>管理员登录</p>
      </div>
      <el-form>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入您的管理员账号" v-model="userName" clearable></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入您的密码" v-model="userPassWord" show-password clearable></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="goToAdminHead">
              确认
            </el-button>
        </div>
        <div class="return-text">
           <el-link href="#/">返回</el-link>
        </div>
      </el-form>
    </div>
  </div>
  </transition>
</template>

<script>
export default {
  name: 'AdminLogin',
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
    goToAdminHead: function () {
      let that = this
      if ((that.userName === 'tqj' || that.userName === 'oyk' || that.userName === 'gmm') && that.userPassWord === '123456') {
        that.$router.push({
          name: 'AdminHead'
        })
        console.log('from' + that.userName)
      } else {
        if (that.userName === '' || that.userPassWord === '') {
          that.$message.info('请输入正确的形式！')
        } else {
          that.$message.error('不存在该管理员')
        }
      }
    },
    keydown (e) {
      if (e.keyCode === 13) {
        this.goToAdminHead()
      }
    },
    destroyed () {
      window.removeEventListener('keydown', this.keydown, false)
    }
  }
}
</script>

<style scoped>
  @import "../../assets/css/login.css";
  @import "../../assets/css/Transition/head-login-register.css";
</style>
