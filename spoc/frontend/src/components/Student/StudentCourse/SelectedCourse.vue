<template>
  <div>
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  我的课程</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        <el-table :data="myCourseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="课程材料" prop="materialIdString"></el-table-column>
          <el-table-column label="退课"> <template slot-scope="scope">
        <el-button v-on:click="dropCourse(scope.$index)" type="primary" plain="true">退课</el-button>
      </template></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
export default {
  name: 'StudentCourse',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      myCourseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: '1,2'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentCourseList()
  },
  methods: {
    getStudentCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetStudentCourseList/',
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
        that.$message.success('退课成功')
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>
