<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}} 教师首页</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        欢迎来到SPOC教师界面，在这里你可以开设课程、查看已开设课程
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from './TeacherNav'
export default {
  name: 'TeacherHead',
  components: {TeacherNav},
  data: function () {
    return {
      userNickName: '',
      userName: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  }
}
</script>

<style scoped>

</style>
