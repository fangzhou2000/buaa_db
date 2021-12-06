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
          <el-table :data="teacherList" v-loading="loading">
            <el-table-column label="教师工号" prop="id"></el-table-column>
            <el-table-column label="教师名称" prop="name"></el-table-column>
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
  name: 'TeacherTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      teacherList: [
        {
          id: 't19373686',
          name: '欧阳老师'
        },
        {
          id: 't19373135',
          name: '田老师'
        },
        {
          id: 't19373136',
          name: '郭老师'
        }
      ]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getTeacherList()
  },
  methods: {
    getTeacherList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherList/',
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
