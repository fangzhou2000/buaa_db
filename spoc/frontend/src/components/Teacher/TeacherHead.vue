<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 教师首页</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        欢迎来到SPOC教师界面，在这里你可以开设课程、查看已开设课程（小作业暂时就做这些）
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
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
</style>

<script>
import TeacherNav from './TeacherNav'
export default {
  name: 'TeacherHead',
  components: {TeacherNav},
  data: function () {
    return {
      userName: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
  }
}
</script>
