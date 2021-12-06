<template>
  <el-menu :default-active="this.$route.path" router :collapse="isCollapsed" class="el-head-menu">
    <el-menu-item class="item" index="/StudentHead">
      <i class="el-icon-headset"></i>
      <span class="item">首页</span>
    </el-menu-item>
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-box"></i><span class="item">课程信息</span></template>
      <el-menu-item class="subitem" index="/StudentCourse/SelectCourse">学生选课</el-menu-item>
      <el-menu-item class="subitem" index="/StudentCourse/SelectedCourse">我的课程</el-menu-item>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title"><i class="el-icon-s-platform"></i><span class="item">留言板</span></template>
      <el-menu-item class="subitem" index="/StudentCommentAndDiscuss/StudentAllComment">课程评价</el-menu-item>
      <el-menu-item class="subitem" index="/StudentCommentAndDiscuss/StudentAllDiscuss">自由讨论</el-menu-item>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title"><i class="el-icon-user"></i><span class="item">用户信息</span></template>
      <el-menu-item class="subitem" index="/StudentChange/StudentChange">修改密码</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<style>
@import "../../assets/css/nav.css";
</style>

<script>
import Utils from '../../assets/js/util.js'

export default {
  name: 'StudentNav',
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
    Utils.$on('toggleCollapse', function (message) {
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
