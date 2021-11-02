<template>
  <div class="background">
    <br>
    <div class="register_block">
      <div class="register_head">
        <p>教师注册</p>
      </div>
      <el-form>
        <div id="register-n">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入姓名" v-model="userNickName"></el-input>
          </el-form-item>
        </div>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入工号" v-model="userName"></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入密码" v-model="userPassWord" show-password></el-input>
          </el-form-item>
        </div>
        <div id="confirm-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请确认密码" v-model="userPassWord2" show-password></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="Register">
              确认
            </el-button>
        </div>
        <div class="return-button">
            <el-button id="button_re" type="primary" plain="true" size="small" v-on:click="goToTeacherLogin">
              返回
            </el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      userNickName: '',
      userName: '',
      userPassWord: '',
      userPassWord2: ''
    }
  },
  methods: {
    goToTeacherLogin: function () {
      this.$router.push({
        name: 'TeacherLogin'
      })
    },
    Register: function () {
      let that = this
      if (that.userPassWord === '') {
        that.$message.error('密码不能为空')
      } else if (that.userName === '') {
        that.$message.error('用户名不能为空')
      } else {
        this.$http.request({
          url: that.$url + 'TeacherRegister/',
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
              name: 'TeacherLogin'
            })
          } else if (that.status === 1) {
            that.$message.error('工号已存在')
          } else if (that.status === 2) {
            that.$message.error('密码不一致')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    }
  }
}
</script>

<style scoped>
  @import "../../assets/css/register.css";
</style>
