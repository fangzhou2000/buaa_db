<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}}  我的课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        <el-table :data="myCourseList">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称" prop="name"></el-table-column>
          <el-table-column label="退课"> <template slot-scope="scope">
        <el-button v-on:click="dropCourse(scope.$index)" type="primary" plain="true">退课</el-button>
      </template></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<style>
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: whitesmoke;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
</style>

<script>
import StudentNav from './StudentNav'
export default {
  name: 'StudentCourse',
  components: {StudentNav},
  data: function () {
    return {
      userName: '',
      myCourseList: [{
        id: '1',
        name: 'Java程序设计'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.getMyCourseList()
  },
  methods: {
    getMyCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetMyCourseList/',
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
        alert('退课成功')
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>
