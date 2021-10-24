<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 查看课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <TeacherNav></TeacherNav>
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
import TeacherNav from './TeacherNav'
export default {
  name: 'TeacherCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      courseList: []
    }
  },
  mounted: function () {
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
    }
  }
}
</script>
