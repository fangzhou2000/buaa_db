<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 教师首页</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=1 router="true">
          <el-menu-item index=1 v-on:click="goToTeacherHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToBuildCourse">开设课程</el-menu-item>
          <el-menu-item index=3 v-on:click="goToTeacherCourse">查看课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToTeacherChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
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
export default {
  name: 'TeacherHead',
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
    goToTeacherChange: function () {
      this.$router.push({
        name: 'TeacherChange',
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
