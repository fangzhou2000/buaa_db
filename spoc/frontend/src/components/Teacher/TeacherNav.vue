<template>
  <div>
    <el-menu :default-active="this.$route.path" router>
      <el-menu-item index="/TeacherHead">首页</el-menu-item>
      <el-menu-item index="/BuildCourse">开设课程</el-menu-item>
      <el-menu-item index="/TeacherCourse">查看课程</el-menu-item>
      <el-menu-item index="/TeacherChange">修改密码</el-menu-item>
      <el-menu-item v-on:click="goToHelloWorld">退出登录</el-menu-item>
    </el-menu>
  </div>
</template>

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
