<template>
  <div class="background">
<!--    <el-container class="header">-->
<!--      <el-header>-->
<!--        <span>{{userNickName}} 查看课程</span>-->
<!--        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>-->
<!--      </el-header>-->
<!--    </el-container>-->
    <el-container class="main">
      <el-aside width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container>
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main>
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="课程材料ID" prop="materialIdString"></el-table-column>
          <el-table-column label="课程材料" prop="materialNameString"></el-table-column>
        </el-table>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'AllCourse',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: [{
          id: '1',
          name: 'book1'
        }],
        materialNameString: 'book1,book2'
      }, {
        id: '2',
        name: '前端测试课程',
        materialIdString: '12',
        materialNameString: 'book1'
      }, {
        id: '3',
        name: '前端测试课程',
        materialIdString: '13',
        materialNameString: 'book1'
      }, {
        id: '4',
        name: '前端测试课程',
        materialIdString: '14',
        materialNameString: 'book1'
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

<style scoped>
 @import "../../../assets/css/Nav.css";
 @import "../../../assets/css/head.css";
</style>
