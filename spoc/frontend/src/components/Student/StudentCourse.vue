<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  我的课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=3 router="true">
          <el-menu-item index=1 v-on:click="goToStudentHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToSelectCourse">学生选课</el-menu-item>
          <el-menu-item index=3 v-on:click="goToStudentCourse">我的课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToStudentChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-table :data="myCourseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="退课"> <template slot-scope="scope">
        <el-button v-on:click="dropCourse(scope.$index)" type="primary" plain="true">退课</el-button>
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
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
</style>

<script>
export default {
  name: 'StudentCourse',
  data: function () {
    return {
      userName: '',
      myCourseList: [{
        id: '1',
        name: 'Java程序设计'
      }]
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
    this.getMyCourseList()
  },
  methods: {
    getMyCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetMyCourseList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.myCourseList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    dropCourse: function (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'DropCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.myCourseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        that.myCourseList = response.data
        alert('退课成功')
      }).catch(function (error) {
        console.log(error)
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
