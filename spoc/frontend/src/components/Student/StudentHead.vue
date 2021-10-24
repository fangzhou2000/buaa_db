<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  学生首页</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        欢迎来到SPOC学生界面，在这里你可以修改密码、选课、查看已选课程。
      </el-main>
    </el-container>
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
</style>

<script>
import StudentNav from './StudentNav'
export default {
  name: 'StudentHead',
  components: {StudentNav},
  data: function () {
    return {
      userName: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {

  }
}
</script>
