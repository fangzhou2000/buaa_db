<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}} 开设课程</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-form label-position="top">
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
              <el-button v-on:click="buildCourse" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
export default {
  name: 'BuildCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      materialIdString: '',
      course: {
        name: '',
        materialIdList: []
      }
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    buildCourse: function () {
      let that = this
      that.course.materialIdList = that.materialIdString.split(',')
      console.log(that.course.materialIdList)
      this.$http.request({
        url: that.$url + 'BuildCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          course: that.course
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          that.$message.success('创建成功')
          that.materialIdString = ''
          that.course = {
            name: '',
            materialIdList: []
          }
        } else if (that.status === 1) {
          that.$message.error('学习材料编号错误')
        } else if (that.status === 2) {
          that.$message.error('课程名称不能为空')
        }
      }).catch(function (error) {
        console.log(error)
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
