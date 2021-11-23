<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
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
  @import "../../assets/css/back.css";
  @import "../../assets/css/nav.css";
</style>
