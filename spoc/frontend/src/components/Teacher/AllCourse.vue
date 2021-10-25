<template>
  <div class="background">
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

<script>
import TeacherNav from './TeacherNav'
export default {
  name: 'AllCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程'
      }]
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
