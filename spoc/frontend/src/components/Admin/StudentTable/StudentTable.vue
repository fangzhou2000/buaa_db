<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main>
          <el-table :data="studentList" v-loading="loading">
            <el-table-column label="学号" prop="id"></el-table-column>
            <el-table-column label="姓名" prop="name"></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
export default {
  name: 'AdminTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      studentList: [
        {
          id: 19373686,
          name: '欧阳奎'
        },
        {
          id: 19373135,
          name: '田旗舰'
        },
        {
          id: 19373136,
          name: '郭明明'
        }
      ]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentList()
  },
  methods: {
    getStudentList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.courseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
