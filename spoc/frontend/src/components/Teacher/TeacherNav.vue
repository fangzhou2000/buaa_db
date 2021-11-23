<template>
    <el-menu :default-active="this.$route.path"
             @open="handleOpen" @close="handleClose"
             router
             :collapse="isCollapsed" class="el-head-menu">
      <el-menu-item class="item" index="/TeacherHead">
        <i class="el-icon-headset"></i>
        <span class="item">首页</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-location-information"></i><span class="item">课程信息</span></template>
        <el-menu-item class="subitem" index="/TeacherCourse/AllCourse">查看课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/BuildCourse">开设课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/ManageCourse">管理课程</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-s-marketing"></i><span class="item">学习材料</span></template>
        <el-menu-item class="subitem" index="/TeacherMaterial/AllMaterial">查看学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/BuildMaterial">新建学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/ManageMaterial">管理学习材料</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-user"></i><span class="item">用户信息</span></template>
        <el-menu-item class="subitem" index="/TeacherChange/TeacherChange">修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
</template>

<style>
  @import "../../assets/css/nav.css";
</style>

<script>
import Utils from '../../assets/js/util.js'
export default {
  name: 'TeacherNav',
  data () {
    return {
      userName: '',
      userNickName: '',
      isCollapsed: true
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    var that = this
    Utils.$on('toggleCollapseTeacher', function (message) {
      console.log(message)
      that.toggleCollapse()
    })
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed
    }
  }
}
</script>
