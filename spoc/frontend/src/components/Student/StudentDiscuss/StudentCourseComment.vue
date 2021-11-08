<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  课程评论</span>
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
  name: 'StudentCourseComment',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: '1,2',
        materialNameString: 'book1,book2'
      }]
    }
  },
  methods: {
    commentCourse: function (index) {
      let that = this
      this.$router.push({
        path: '/StudentDiscuss/CommentCourse',
        query: {
          id: that.courseList[index].id,
          name: that.courseList[index].name
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
