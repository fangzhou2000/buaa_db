<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  学生选课</span>
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
          <el-table-column label="课程材料" prop="materialIdString"></el-table-column>
          <el-table-column label="选课"> <template slot-scope="scope">
        <el-button v-on:click="selectCourse(scope.$index)" type="primary" plain="true">选课</el-button>
      </template></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
export default {
  name: 'SelectCourse',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      courseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: '1,2'
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
          that.$message.success('选课成功')
        } else if (status === 1) {
          that.$message.info('已选择该课程')
        } else {
          that.$message.error('!')
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
