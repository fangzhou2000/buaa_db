<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  修改密码</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=4 router="true">
          <el-menu-item index=1 v-on:click="goToStudentHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToSelectCourse">学生选课</el-menu-item>
          <el-menu-item index=3 v-on:click="goToStudentCourse">我的课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToStudentChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
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
  </div>
</template>

<style>
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: #b4f5ff;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    width: 20%;
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
  .el-main {
  }
</style>

<script>
export default {
  name: 'StudentChange',
  data: function () {
    return {
      userName: '',
      userPassWord0: '',
      userPassWord1: '',
      userPassWord2: ''
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
  },
  methods: {
    changePassWord: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'StudentChange/',
        method: 'get',
        params: {
          userPassWord0: that.userPassWord0,
          userPassWord1: that.userPassWord1,
          userPassWord2: that.userPassWord2
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          alert('修改成功')
          that.$router.push({
            name: 'StudentLogin',
            params: {
              userName: that.userName
            }
          })
        } else if (that.status === 1) {
          alert('原密码错误')
        } else if (that.status === 2) {
          alert('新密码不一致')
        } else {
          alert('!')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    goToStudentHead: function () {
      this.$router.push({
        name: 'StudentHead',
        params: {
          userName: this.userName
        }
      })
    },
    goToSelectCourse: function () {
      this.$router.push({
        name: 'SelectCourse',
        params: {
          userName: this.userName
        }
      })
    },
    goToHelloWorld: function () {
      this.$router.push({
        name: 'HelloWorld'
      })
    },
    goToStudentChange: function () {
      this.$router.push({
        name: 'StudentChange',
        params: {
          userName: this.userName
        }
      })
    },
    goToStudentCourse: function () {
      this.$router.push({
        name: 'StudentCourse',
        params: {
          userName: this.userName
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
