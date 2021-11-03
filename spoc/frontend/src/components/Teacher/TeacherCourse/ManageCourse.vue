<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  管理课程</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-table :data="myCourseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="课程材料" prop="materialString"></el-table-column>
          <el-table-column label="修改课程">
            <template slot-scope="scope">
              <el-button v-on:click="changeCourse(scope.$index)" type="warning" size="small">修改课程</el-button>
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
import TeacherNav from '../TeacherNav'

export default {
  name: 'ManageCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      myCourseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: '资料',
        materialString: ''
      }]
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
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
    changeCourse: function (index) {
      let that = this
      console.log(index)
      this.$router.push({
        path: '/TeacherCourse/ChangeCourse',
        // 这里不能使用params传递参数，详见：
        // https://blog.csdn.net/qq_37548296/article/details/90446430
        query: {
          id: that.myCourseList[index].id,
          name: that.myCourseList[index].name,
          materialIdString: that.myCourseList[index].materialIdString
        }
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
        if (response.data === 0) {
          that.$message.success('停课成功')
        } else {
          that.$message.error('!')
        }
        that.getTeacherCourseList()
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
