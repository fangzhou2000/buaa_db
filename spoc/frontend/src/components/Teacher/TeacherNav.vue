<template>
    <el-menu :default-active="this.$route.path"
             router
             :collapse="isCollapsed" class="el-head-menu">
      <el-menu-item class="item" index="/TeacherHead">
        <i class="el-icon-s-home"></i>
        <span class="item">首页</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-reading"></i><span class="item">课程信息</span></template>
        <el-menu-item class="subitem" index="/TeacherCourse/AllCourse">查看课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/BuildCourse">开设课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/ManageCourse">管理课程</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-s-data"></i><span class="item">学习材料</span></template>
        <el-menu-item class="subitem" index="/TeacherMaterial/AllMaterial">查看学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/BuildMaterial">新建学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/ManageMaterial">管理学习材料</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-share"></i><span class="item">留言板</span></template>
        <el-menu-item class="subitem" index="/TeacherCommentAndDiscuss/TeacherAllComment">课程评价</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCommentAndDiscuss/TeacherAllDiscuss">自由讨论</el-menu-item>
      </el-submenu>
      <el-submenu index="4">
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
      isCollapsed: this.$root.isCollapsed
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
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed
      this.$root.isCollapsed = this.isCollapsed
    }
  }
}
</script>
