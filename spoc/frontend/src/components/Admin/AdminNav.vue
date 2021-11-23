<template>
  <el-menu
    :default-active="this.$route.path" router
    :collapse="isCollapsed" class="el-head-menu">
    <el-menu-item class="item" index="/AdminHead">
      <i class="el-icon-headset"></i>
      <span class="item">首页</span>
    </el-menu-item>
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-location-information"></i><span class="item">课程信息</span></template>
      <el-menu-item class="subitem" index="/CourseTable/CourseTable">查看课程</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">查看课程</el-menu-item>-->
    </el-submenu>
    <el-submenu index="2">
        <template slot="title"><i class="el-icon-male"></i><span class="item">学生信息</span></template>
        <el-menu-item class="subitem" index="/StudentTable/StudentTable">学生资料</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">学生资料</el-menu-item>-->
    </el-submenu>
    <el-submenu index="3">
        <template slot="title"><i class="el-icon-female"></i><span class="item">教师信息</span></template>
        <el-menu-item class="subitem" index="/TeacherTable/TeacherTable">查看教师信息</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">查看教师信息</el-menu-item>-->
      </el-submenu>
    <el-submenu index="4">
        <template slot="title"><i class="el-icon-s-marketing"></i><span class="item">材料信息</span></template>
        <el-menu-item class="subitem" index="/MaterialTable/MaterialTable">查看学习材料</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">查看学习材料</el-menu-item>-->
    </el-submenu>
    <el-submenu index="5">
        <template slot="title"><i class="el-icon-user"></i><span class="item">用户信息</span></template>
        <el-menu-item class="subitem" index="/AdminChange/AdminChange">修改密码</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">修改密码</el-menu-item>-->
    </el-submenu>
  </el-menu>
</template>

<script>
import Utils from '../../assets/js/util.js'
export default {
  name: 'AdminNav',
  data () {
    return {
      userName: '',
      userNickName: '',
      isCollapsed: true
    }
  },
  mounted: function () {
    // this.userName = this.cookie.getCookie('userName')
    // this.userNickName = this.cookie.getCookie('userNickName')
    this.userNickName = 'Admin'
    this.userName = 'Admin'
    var that = this
    Utils.$on('toggleCollapseAdmin', function (message) {
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

<style scoped>
  @import "../../assets/css/nav.css";
</style>
