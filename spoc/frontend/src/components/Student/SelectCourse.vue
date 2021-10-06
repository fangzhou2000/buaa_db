<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 学生选课</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active="/" router="true">
          <el-menu-item v-on:click="goToStudentHead">首页</el-menu-item>
          <el-menu-item index="/">学生选课</el-menu-item>
          <el-menu-item v-on:click="goToStudentCourse">我的课程</el-menu-item>
          <el-menu-item v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        选课内容
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
export default {
  name: 'SelectCourse',
  data: function () {
    return {
      userName: '',
      courseList: []
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
  },
  methods: {
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
