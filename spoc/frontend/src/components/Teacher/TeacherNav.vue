<template>
  <div class="aside">
    <div>
      <el-card style="background-color: #66b1ff">
        <i class="el-icon-user-solid" style="font-size: 50px"></i>
        <p style="color: white">姓名:&nbsp;{{userNickName}}</p>
        <p style="color: white">工号:&nbsp;{{userName}}</p>
      </el-card>
    </div>
    <el-menu :default-active="this.$route.path"
             @open="handleOpen" @close="handleClose"
             router
             unique-opened:true>
      <el-menu-item class="item" index="/TeacherHead">首页</el-menu-item>
      <el-submenu index="1" show-timeout:0>
        <template slot="title"><span class="item">课程信息</span></template>
        <el-menu-item class="subitem" index="/TeacherCourse/AllCourse">&emsp;&emsp;查看课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/BuildCourse">&emsp;&emsp;开设课程</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCourse/ManageCourse">&emsp;&emsp;管理课程</el-menu-item>
      </el-submenu>
      <el-submenu index="2" show-timeout:0>
        <template slot="title"><span class="item">学习材料</span></template>
        <el-menu-item class="subitem" index="/TeacherMaterial/AllMaterial">&emsp;&emsp;&emsp;&emsp;查看学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/BuildMaterial">&emsp;&emsp;&emsp;&emsp;新建学习材料</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherMaterial/ManageMaterial">&emsp;&emsp;&emsp;&emsp;管理学习材料</el-menu-item>
      </el-submenu>
      <el-submenu index="3" show-timeout:0>
        <template slot="title"><span class="item">用户信息</span></template>
        <el-menu-item class="subitem" index="/TeacherChange/TeacherChange">&emsp;&emsp;修改密码</el-menu-item>
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
    height: 100%;
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
  name: 'TeacherNav',
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
    }
  }
}
</script>

<style scoped>

</style>
