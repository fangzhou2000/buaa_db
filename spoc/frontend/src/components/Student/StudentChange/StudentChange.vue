<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main>
          <el-row>{{userNickName}} 密码修改 </el-row>
        <el-form label-width="100px">
          <el-form-item label="原密码">
            <el-col span="6">
              <el-input placeholder="请输入原密码" v-model="userPassWord0" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="新密码">
            <el-col span="6">
              <el-input placeholder="请输入新密码" v-model="userPassWord1" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="确认新密码">
            <el-col span="6">
              <el-input placeholder="请确认新密码" v-model="userPassWord2" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col span="6">
              <el-button v-on:click="changePassWord" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
export default {
  name: 'StudentChange',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      userPassWord0: '',
      userPassWord1: '',
      userPassWord2: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    changePassWord: function () {
      let that = this
      if (that.userPassWord1 === '') {
        that.$message.error('密码不能为空')
      } else {
        this.$http.request({
          url: that.$url + 'StudentChange/',
          method: 'get',
          params: {
            userName: that.userName,
            userPassWord0: that.userPassWord0,
            userPassWord1: that.userPassWord1,
            userPassWord2: that.userPassWord2
          }
        }).then(function (response) {
          console.log(response.data)
          that.status = response.data
          if (that.status === 0) {
            that.$message.success('修改成功')
            that.$router.push({
              name: 'StudentLogin',
              params: {
                userName: that.userName
              }
            })
          } else if (that.status === 1) {
            that.$message.error('原密码错误')
          } else if (that.status === 2) {
            that.$message.error('新密码不一致')
          } else {
            that.$message.error('!')
          }
        }).catch(function (error) {
          console.log(error)
        })
      }
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
