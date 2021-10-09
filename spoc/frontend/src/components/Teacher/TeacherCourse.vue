<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 查看课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=3 router="true">
          <el-menu-item index=1 v-on:click="goToTeacherHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToBuildCourse">开设课程</el-menu-item>
          <el-menu-item index=3 v-on:click="goToTeacherCourse">查看课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToTeacherChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
        </el-table>
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
  name: 'TeacherCourse',
  data: function () {
    return {
      userName: '',
      courseList: []
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
    this.getCourseList()
  },
  methods: {
    getCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCourseList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.courseList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
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
