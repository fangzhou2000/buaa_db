<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main>
          <el-table :data="courseList" v-loading="loading" >
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称" prop="name"></el-table-column>
            <el-table-column label="课程材料" prop="materialIdString"></el-table-column>
            <el-table-column label="选课"> <template slot-scope="scope">
          <el-button v-on:click="selectCourse(scope.$index)" type="primary">选课</el-button>
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
  name: 'SelectCourse',
  components: {StudentNav, StudentHeading},
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

<style scoped>
  @import "../../../assets/css/back.css";
</style>
