<template>
  <div class="aside">
    <div>
      <el-card style="background-color: #66b1ff">
        <i class="el-icon-user-solid" style="font-size: 50px"></i>
        <p style="color: white">姓名:&nbsp;{{userNickName}}</p>
        <p style="color: white">学号:&nbsp;{{userName}}</p>
      </el-card>
    </div>
    <el-menu :default-active="this.$route.path" router>
      <el-menu-item class="item" index="/StudentHead">首页</el-menu-item>
      <el-submenu index="1" show-timeout:0>
        <template slot="title"><span class="item">课程信息</span></template>
        <el-menu-item class="subitem" index="/StudentCourse/SelectCourse">&emsp;&emsp;学生选课</el-menu-item>
        <el-menu-item class="subitem" index="/StudentCourse/SelectedCourse">&emsp;&emsp;我的课程</el-menu-item>
      </el-submenu>
      <el-submenu index="2" show-timeout:0>
        <template slot="title"><span class="item">用户信息</span></template>
        <el-menu-item class="subitem" index="/StudentChange/StudentChange">&emsp;&emsp;修改密码</el-menu-item>
      </el-submenu>
<!--      <el-menu-item class="item" v-on:click="goToHelloWorld">退出登录</el-menu-item>-->
    </el-menu>
  </div>
</template>

<style>
  .header {
    color: white;
    height: 80px;
  }
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: #66b1ff;
    line-height: 60px;
  }
  .background {
    height: 1920px;
    background-color: white;
  }
  .main {
    height: 900px;
  }
  .el-main{
    height: inherit;
  }
  .aside{
    height: 900px;
  }
  .el-aside {
    text-align: center;
  }
  .item {
    font-size: 18px;
  }
  .subitem {
    font-size: 16px;
  }
</style>

<script>
export default {
  name: 'StudentNav',
  data () {
    return {
      userName: '',
      userNickName: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped>

</style>
