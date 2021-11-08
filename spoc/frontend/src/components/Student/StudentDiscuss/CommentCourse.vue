<template>
  <div>
   <el-container class="header">
      <el-header>
        <span>{{userNickName}} 评论 {{name}}</span>
        <el-button style="margin-top: 10px; float: right" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        111
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'

export default {

  name: 'CommentCourse',
  components: {StudentNav},
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>
