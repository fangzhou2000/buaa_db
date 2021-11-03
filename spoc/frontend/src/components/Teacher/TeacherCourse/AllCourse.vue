<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}} 查看课程</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="课程材料" prop="materialIdString"></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
export default {
  name: 'AllCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: '11'
      }, {
        id: '2',
        name: '前端测试课程',
        materialIdString: '12'
      }, {
        id: '3',
        name: '前端测试课程',
        materialIdString: '13'
      }, {
        id: '4',
        name: '前端测试课程',
        materialIdString: '14'
      }]
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
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
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>
