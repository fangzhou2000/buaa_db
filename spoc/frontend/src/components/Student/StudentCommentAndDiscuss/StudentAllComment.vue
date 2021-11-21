<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>课程评价</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        <el-table :data="courseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="评价"> <template slot-scope="scope">
        <el-button v-on:click="commentCourse(scope.$index)" type="primary">评价</el-button>
      </template></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'

export default {
  name: 'StudentAllComment',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程1',
        materialIdString: '1,2',
        materialNameString: 'book1,book2'
      }, {
        id: '2',
        name: '前端测试课程2',
        materialIdString: '1,2',
        materialNameString: 'book1,book2'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
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
    commentCourse: function (index) {
      let that = this
      this.$router.push({
        path: '/StudentCommentAndDiscuss/StudentComment',
        query: {
          courseId: that.courseList[index].id,
          courseName: that.courseList[index].name
        }
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

</style>
