<template>
  <div>
    <el-container>
      <el-header>
        <span>{{userName}} 开设课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <el-menu default-active=2 router="true">
          <el-menu-item index=1 v-on:click="goToTeacherHead">首页</el-menu-item>
          <el-menu-item index=2 v-on:click="goToBuildCourse">开设课程</el-menu-item>
          <el-menu-item index=3 v-on:click="goToTeacherCourse">查看课程</el-menu-item>
          <el-menu-item index=4 v-on:click="goToTeacherChange">修改密码</el-menu-item>
          <el-menu-item index=5 v-on:click="goToHelloWorld">退出登录</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-form label-width="100px">
          <el-form-item label="课程名称">
            <el-col span="6">
              <el-input placeholder="请输入课程名称" v-model="courseName"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col span="6">
              <el-button v-on:click="buildCourse" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<style>
  .el-header {
    text-align: center;
    font-size: 24px;
    background-color: #b4f5ff;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    text-align: center;
  }
  .el-menu-item {
    font-size: 18px;
  }
</style>

<script>
export default {
  name: 'BuildCourse',
  data: function () {
    return {
      userName: '',
      courseName: ''
    }
  },
  mounted: function () {
    this.userName = this.$route.params.userName
  },
  methods: {
    buildCourse: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'BuildCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          courseName: that.courseName
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          alert('创建成功')
        } else {
          alert('!')
        }
      }).catch(function (error) {
        console.log(error)
      })
      that.courseName = ''
    },
    goToTeacherHead: function () {
      this.$router.push({
        name: 'TeacherHead',
        params: {
          userName: this.userName
        }
      })
    },
    goToBuildCourse: function () {
      this.$router.push({
        name: 'BuildCourse',
        params: {
          userName: this.userName
        }
      })
    },
    goToTeacherCourse: function () {
      this.$router.push({
        name: 'TeacherCourse',
        params: {
          userName: this.userName
        }
      })
    },
    goToTeacherChange: function () {
      this.$router.push({
        name: 'TeacherChange',
        params: {
          userName: this.userName
        }
      })
    },
    goToHelloWorld: function () {
      this.$router.push({
        name: 'HelloWorld'
      })
    }
  }
}
</script>
