<template>
  <div>
    <el-menu :default-active="this.$route.path" router>
      <el-menu-item index="/TeacherHead">首页</el-menu-item>
      <el-menu-item index="/AllCourse">查看课程</el-menu-item>
      <el-menu-item index="/BuildCourse">开设课程</el-menu-item>
      <el-menu-item index="/TeacherCourse">管理课程</el-menu-item>
      <el-menu-item index="/TeacherChange">修改密码</el-menu-item>
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
  name: 'TeacherNav',
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
