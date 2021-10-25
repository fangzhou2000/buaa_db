<template>
  <div>
    <el-menu :default-active="this.$route.path" router>
      <el-menu-item index="/StudentHead">首页</el-menu-item>
      <el-menu-item index="/SelectCourse">学生选课</el-menu-item>
      <el-menu-item index="/StudentCourse">我的课程</el-menu-item>
      <el-menu-item index="/StudentChange">修改密码</el-menu-item>
      <el-menu-item v-on:click="goToHelloWorld">退出登录</el-menu-item>
    </el-menu>
  </div>
</template>

<style>
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: whitesmoke;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    text-align: center;
  }
  .el-main {
    width: 80%;
  }
  .el-menu-item {
    font-size: 18px;
  }
  .background {
    background-color: white;
    background-image: linear-gradient(0deg, #f8f1ea 0%, #ffffff 10%);
    height: 100vh;
  }
</style>

<script>
export default {
  name: 'StudentNav',
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped>

</style>
