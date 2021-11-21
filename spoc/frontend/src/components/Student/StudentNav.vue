<template>
  <div class="aside">
    <div>
      <el-card style="background-color: whitesmoke">
        <i class="el-icon-user-solid" style="font-size: 50px"></i>
        <p>姓名:&nbsp;{{userNickName}}</p>
        <p>学号:&nbsp;{{userName}}</p>
      </el-card>
    </div>
    <el-menu :default-active="this.$route.path" router>
      <el-menu-item class="item" index="/StudentHead">首页</el-menu-item>
      <el-submenu index="1">
        <template slot="title"><span class="item">课程信息</span></template>
        <el-menu-item class="subitem" index="/StudentCourse/SelectCourse">&emsp;&emsp;学生选课</el-menu-item>
        <el-menu-item class="subitem" index="/StudentCourse/SelectedCourse">&emsp;&emsp;我的课程</el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><span class="item">留言板</span></template>
        <el-menu-item class="subitem" index="/StudentCommentAndDiscuss/StudentAllComment">&emsp;&emsp;课程评价</el-menu-item>
        <el-menu-item class="subitem" index="/StudentCommentAndDiscuss/StudentAllDiscuss">&emsp;&emsp;自由讨论</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><span class="item">用户信息</span></template>
        <el-menu-item class="subitem" index="/StudentChange/StudentChange">&emsp;&emsp;修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<style>
  .header {
    height: 80px;
  }
  .exit {
    margin-top: 10px;
    float: right;
  }
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: whitesmoke;
    line-height: 60px;
  }
  .background {
    height: 100%;
    background-color: white;
  }
  .main {
    height: 600px;
  }
  .el-main{
    height: inherit;
  }
  .aside{
    height: 600px;
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
