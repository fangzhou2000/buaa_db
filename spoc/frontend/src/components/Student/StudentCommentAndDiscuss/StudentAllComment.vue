<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main>
          <el-table :data="courseList"  v-loading="loading">
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称" prop="name"></el-table-column>
            <el-table-column label="评价"> <template slot-scope="scope">
          <el-button v-on:click="commentCourse(scope.$index)" type="primary" size="small">评价</el-button>
        </template></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
export default {
  name: 'StudentAllComment',
  components: {StudentNav, StudentHeading},
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
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCourseList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.courseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
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
  @import "../../../assets/css/back.css";
</style>
