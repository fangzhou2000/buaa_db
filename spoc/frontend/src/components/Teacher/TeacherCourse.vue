<template>
  <div class="background">
    <el-container>
      <el-header>
        <span>{{userName}}  管理课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-table :data="myCourseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="修改名称">
            <template slot-scope="scope">
              <el-button v-on:click="changeCourseName(scope.$index)" type="warning" size="small">修改名称</el-button>
            </template>
          </el-table-column>
          <el-table-column label="停课">
            <template slot-scope="scope">
              <el-button v-on:click="cancelCourse(scope.$index)" type="danger" size="small">停课</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from './TeacherNav'
export default {
  name: 'TeacherCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      myCourseList: [{
        id: '1',
        name: '前端测试课程'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.getTeacherCourseList()
  },
  methods: {
    getTeacherCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetTeacherCourseList/',
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
    changeCourseName: function (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'ChangeCourseName/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.myCourseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        that.myCourseList = response.data
        alert('修改课程名称成功')
      }).catch(function (error) {
        console.log(error)
      })
    },
    cancelCourse: function (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'CancelCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.myCourseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        that.myCourseList = response.data
        alert('停课成功')
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
