<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  学生选课</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=2 router="true">
          <el-menu-item index=1 v-on:click="goToStudentHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToSelectCourse">学生选课</el-menu-item>
          <el-menu-item index=3 v-on:click="goToStudentCourse">我的课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToStudentChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="选课"> <template slot-scope="scope">
        <el-button v-on:click="selectCourse(scope.$index)" type="primary" plain="true">选课</el-button>
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
    selectCourse (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'SelectCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.courseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        var status = response.data
        if (status === 0) {
          alert('选课成功')
        } else if (status === 1) {
          alert('已选择该课程')
        } else {
          alert('!')
        }
      })
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
    goToStudentChange: function () {
      this.$router.push({
        name: 'StudentChange',
        params: {
          userName: this.userName
        }
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
