<template>
  <div>
<!--    <el-container class="header">-->
<!--      <el-header>-->
<!--        <span>{{userNickName}} 教师首页</span>-->
<!--        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>-->
<!--      </el-header>-->
<!--    </el-container>-->
    <el-container class="main">
      <el-aside width="show?'64px':30%">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container>
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main>
        欢迎来到SPOC教师界面，在这里你可以开设课程、查看已开设课程
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from './TeacherNav'
import TeacherHeading from './TeacherHeading'
export default {
  name: 'TeacherHead',
  components: {TeacherNav, TeacherHeading}
}
</script>

<style scoped>
  @import "../../assets/css/head.css";
  @import "../../assets/css/Nav.css";
</style>
