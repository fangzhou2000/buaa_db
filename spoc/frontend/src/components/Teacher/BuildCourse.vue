<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 开设课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active="/" router="true">
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item v-on:click="goToBuildCourse">开设课程</el-menu-item>
          <el-menu-item v-on:click="goToTeacherCourse">我的课程</el-menu-item>
          <el-menu-item v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        开设课程内容
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
  name: 'BuildCourse',
  data: function () {
    return {
      userName: ''
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
  },
  methods: {
    goToTeacherHead: function () {
      this.$router.push({
        name: 'TeacherHead',
        params: {
          userName: this.userName
        }
      })
    },
    goToBuildCourse: function () {
      this.$router.push({
        name: 'BuildCourse',
        params: {
          userName: this.userName
        }
      })
    },
    goToTeacherCourse: function () {
      this.$router.push({
        name: 'TeacherCourse',
        params: {
          userName: this.userName
        }
      })
    },
    goToHelloWorld: function () {
      this.$router.push({
        name: 'HelloWorld'
      })
    }
  }
}
</script>
