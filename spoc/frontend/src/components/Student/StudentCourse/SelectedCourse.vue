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
          <el-table :data="myCourseList" v-loading="loading" >
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称" prop="name"></el-table-column>
            <el-table-column label="课程材料" prop="materialIdString"></el-table-column>
            <el-table-column label="退课"> <template slot-scope="scope">
          <el-button v-on:click="dropCourse(scope.$index)" type="danger" size="small">退课</el-button>
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
  name: 'StudentCourse',
  components: {StudentNav, StudentHeading},
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
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentCourseList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.myCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    dropCourse: function (index) {
      this.$confirm('此操作将退选该课程，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
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
          if (response.data === 0) {
            that.$message.success('退课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getStudentCourseList()
        }).catch(function (error) {
          console.log(error)
        })
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
