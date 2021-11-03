<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  新建学习材料</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-form label-position="top">
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
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'

export default {
  name: 'BuildMaterial',
  components: {TeacherNav},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      materialName: ''
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    buildMaterial: function () {
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
    }
  }
}
</script>

<style scoped>

</style>
