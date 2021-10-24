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

<script>
export default {
  name: 'StudentNav',
  methods: {
    goToStudentHead: function () {
      this.$router.push({
        name: 'StudentHead'
      })
    },
    goToSelectCourse: function () {
      this.$router.push({
        name: 'SelectCourse'
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.$router.replace('/')
    },
    goToStudentCourse: function () {
      this.$router.push({
        name: 'StudentCourse'
      })
    },
    goToStudentChange: function () {
      this.$router.push({
        name: 'StudentChange'
      })
    }
  }
}
</script>

<style scoped>

</style>
