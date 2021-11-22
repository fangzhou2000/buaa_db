<template>
  <div>
    <el-container class="main">
      <el-aside width="show?'64px':30%">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container>
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main>
          欢迎来到SPOC学生界面，在这里你可以修改密码、选课、查看已选课程。
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from './StudentNav'
import StudentHeading from './StudentHeading'
export default {
  name: 'StudentHead',
  components: {StudentHeading, StudentNav}
}
</script>

<style scoped>
  @import "../../assets/css/head.css";
</style>
