<template>
  <div>
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
  </div>
</template>

<script>
import Utils from '../../assets/js/util.js'
import StudentNav from './StudentNav'
export default {
  name: 'StudentHeading',
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
    handleCommand (command) {
      this.goToHelloWorld()
    }
  }
}
</script>

<style scoped>
  @import "../../assets/css/head.css";
</style>
