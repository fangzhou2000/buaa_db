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
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="选课"> <template slot-scope="scope">
        <el-button v-on:click="selectCourse(scope.$index)">选课</el-button>
      </template></el-table-column>
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
    width: 20%;
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
  .el-main {
    width: 80%;
  }
</style>

<script>
export default {
  name: 'SelectCourse',
  data: function () {
    return {
      userName: '',
      courseList: [{
        id: '1',
        name: 'C语言程序设计'
      }, {
        id: '2',
        name: '数学分析（1）'
      }]
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
    selectCourse (index) {
      console.log(index)
    },
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
