<template>
  <div class="background">
<!--    <el-container class="header">-->
<!--      <el-header>-->
<!--        <span>{{userNickName}} 查看学习材料</span>-->
<!--        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>-->
<!--      </el-header>-->
<!--    </el-container>-->
    <el-container class="main">
      <el-aside width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container>
        <el-header><TeacherHeading></TeacherHeading></el-header>
        <el-main>
        <el-table :data="materialList">
          <el-table-column label="学习材料ID" prop="id"></el-table-column>
          <el-table-column label="学习材料名称" prop="name"></el-table-column>
        </el-table>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'AllMaterial',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      materialList: [{
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getMaterialList()
  },
  methods: {
    getMaterialList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetMaterialList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.materialList = response.data
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

<style scoped>
 @import "../../../assets/css/Nav.css";
 @import "../../../assets/css/head.css";
</style>
