<template>
  <div>
    <el-container class="header">
      <el-header>
        <span>{{userNickName}}  学生首页</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        欢迎来到SPOC学生界面，在这里你可以修改密码、选课、查看已选课程。
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StudentNav from './StudentNav'
export default {
  name: 'StudentHead',
  components: {StudentNav},
  data: function () {
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

  }
}
</script>
