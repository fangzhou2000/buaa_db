<template>
  <div class="background">
    <el-container class="main">
      <el-aside width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container>
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main>
        <el-form label-position="top" v-loading="loading">
          <el-form-item label="学习材料名称">
            <el-col :span="6">
              <el-input placeholder="请输入学习材料名称" v-model="materialName"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col :span="6">
              <el-button v-on:click="buildMaterial" type="primary" >确认</el-button>
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
  name: 'BuildMaterial',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      materialName: '',
      loading: false
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    buildMaterial: function () {
      this.startLoading()
      let that = this
      this.$http.request({
        url: that.$url + 'BuildMaterial/',
        method: 'get',
        params: {
          userName: that.userName,
          materialName: that.materialName
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          that.$message.success('创建成功')
        } else {
          that.$message.error('!')
        }
      }).catch(function (error) {
        console.log(error)
      })
      that.materialName = ''
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    startLoading: function () {
      this.loading = true
      setTimeout(() => {
        this.loading = false
      }, 2000)
    }
  }
}
</script>

<style scoped>
 @import "../../../assets/css/Nav.css";
 @import "../../../assets/css/head.css";
</style>
