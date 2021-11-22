<template>
  <div>
<!--    <el-container class="header">-->
<!--      <el-header>-->
<!--        <span>{{userNickName}}  学生首页</span>-->
<!--        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>-->
<!--      </el-header>-->
<!--    </el-container>-->

    <el-container class="main">
      <el-aside width="show?'64px':'300px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container>
        <el-header>
          <span class="toggle-btn" @click="toggleCollapse">
            <i class="el-icon-s-unfold" v-if="!show"></i>
            <i class="el-icon-s-fold" v-else></i>
          </span>
          <el-dropdown @command="handleCommand"  class="userInfo" >
            <span class="el-dropdown-link">
              <i class="el-icon-user"></i>
              {{userNickName}}
              <i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="goToHelloWorld">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-header>
        <el-main>
          欢迎来到SPOC学生界面，在这里你可以修改密码、选课、查看已选课程。
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from './StudentNav'
import Utils from '../../assets/js/util.js'
export default {
  name: 'StudentHead',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      show: false
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.show = !this.show
      Utils.$emit('toggleCollapse', 'call function toggleCollapse in StudentNav')
    },
    handleCommand(command) {
      this.goToHelloWorld()
    }
  }
}
</script>

<style scoped>
  @import "../../assets/css/head.css";

</style>
