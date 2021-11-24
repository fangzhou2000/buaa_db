<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main>
        <el-form label-position="top" v-loading="loading">
          <el-form-item label="课程名称">
            <el-col :span="6">
              <el-input v-model="course.name"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="学习材料 (如有多个请用','隔开)">
            <el-col :span="6">
              <el-input v-model="materialIdString"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col :span="6">
              <el-button v-on:click="changeCourse" type="primary" >确认</el-button>
              <el-button v-on:click="returnManageCourse" type="primary" >返回</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'ChangeCourse',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      id: '',
      name: '',
      materialIdString: '',
      course: {
        name: '',
        materialIdList: []
      }
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.id = this.$route.query.id
    this.name = this.$route.query.name
    this.course.name = this.name
    this.materialIdString = this.$route.query.materialIdString
  },
  methods: {
    returnManageCourse: function () {
      let that = this
      that.$router.push({
        name: 'ManageCourse'
      })
    },
    changeCourse: function () {
      let that = this
      that.loading = true
      if (that.course.materialIdString !== '') {
        that.course.materialIdList = that.materialIdString.split(',')
      }
      this.$http.request({
        url: that.$url + 'ChangeCourse/',
        method: 'get',
        params: {
          id: that.id,
          course: that.course,
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        if (response.data === 0) {
          that.$message.success('修改成功')
          that.$router.push({
            name: 'ManageCourse'
          })
        } else if (response.data === 1) {
          that.$message.error('学习材料编号不存在')
        } else if (response.data === 2) {
          that.$message.error('课程名称不能为空')
        }
      }).catch(function (error) {
        console.log(error)
        that.loading = false
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
 @import "../../../assets/css/nav.css";
 @import "../../../assets/css/back.css";
</style>
