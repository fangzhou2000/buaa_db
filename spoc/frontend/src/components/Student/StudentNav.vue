<template>
  <div>
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
      <el-menu-item class="item" v-on:click="goToHelloWorld">退出登录</el-menu-item>
    </el-menu>
  </div>
</template>

<style>
  .header {
    height: 75px;
  }
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: whitesmoke;
    line-height: 60px;
  }
  .background {
    height: 700px;
    background-color: white;
    background-image: linear-gradient(0deg, #f8f1ea 0%, #ffffff 10%);
  }
  .main {
    height: 550px;
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
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped>

</style>
