<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  学生选课</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <StudentNav></StudentNav>
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
    background-color: whitesmoke;
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
import StudentNav from './StudentNav'
export default {
  name: 'SelectCourse',
  components: {StudentNav},
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
    }
  }
}
</script>
