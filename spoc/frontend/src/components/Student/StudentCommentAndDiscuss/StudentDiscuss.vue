<template>
  <div>
   <el-container class="header">
      <el-header>
        <span>贴子 {{postTheme.title}}</span>
        <el-button class="exit" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        <el-row class="buttons">
          <el-button v-on:click="buildPost" type="primary" size="small" >跟贴</el-button>
          <el-button v-on:click="returnStudentAllDiscuss" type="primary" size="small">返回</el-button>
        </el-row>
        <el-row class="buttons">
          <el-col :span="20">
            <el-input class="input" v-model="input.content" type="textarea" :rows="2" placeholder="对于课程内容、讲课质量、考核方式等的评价">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <el-row class="time">
            {{postTheme.time}}
          </el-row>
          <el-row class="userName">
            {{postTheme.userNickName}}({{postTheme.userName}}) :
          </el-row>
          <el-row class="content">
            <el-col :span="1">
              &nbsp;
            </el-col>
            {{postTheme.content}}
          </el-row>
        <el-divider></el-divider>
        <p v-for="(post) in postList" v-bind:key="post">
          <el-row class="time">
            {{post.time}}
          </el-row>
          <el-row class="userName">
            {{post.userNickName}}({{post.userName}}) :
          </el-row>
          <el-row class="content">
            <el-col :span="1">
              &nbsp;
            </el-col>
            {{post.content}}
          </el-row>
          <el-divider></el-divider>
        </p>
      </el-main>
    </el-container>
  </div>
</template>

<style scoped>
  .buttons {
    margin-bottom: 10px;
  }
  .input {
    font-size: large;
  }
  .time {
    font-size: small;
  }
  .userName {
    font-size: medium;
  }
  .content {
    font-size: medium;
  }
</style>

<script>
import StudentNav from '../StudentNav'

export default {
  name: 'StudentDiscuss',
  components: {StudentNav},
  data: function () {
    return {
      userName: '前端测试用户名',
      userNickName: '前端测试姓名',
      postTheme: {
        id: '测试id',
        userName: '学号1',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: '111'
      },
      input: {
        content: ''
      },
      postList: [{
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1',
        time: '2021-11-19 11:11:11'
      }, {
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11'
      }, {
        userName: '学号3',
        userNickName: '学生3',
        content: '课程评价内容3',
        time: '2021-11-19 11:11:11'
      }, {
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1',
        time: '2021-11-19 11:11:11'
      }, {
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11'
      }, {
        userName: '学号3',
        userNickName: '学生3',
        content: '课程评价内容3',
        time: '2021-11-19 11:11:11'
      }],
      time: ''
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.postTheme = this.$route.query.postTheme
    this.getPostList()
  },
  methods: {
    getPostList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetPostList/',
        method: 'get',
        params: {
          postThemeId: that.postTheme.id
        }
      }).then(function (response) {
        console.log(response.data)
        that.postList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    getTime: function () {
      let that = this
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      that.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    buildPost: function () {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'buildPost/',
        method: 'get',
        params: {
          postThemeId: that.postTheme.id,
          userName: that.userName,
          userNickName: that.userNickName,
          content: that.input.content,
          time: that.time
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('跟贴成功')
          that.getPostList()
          that.input.content = ''
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    returnStudentAllDiscuss: function () {
      let that = this
      that.$router.push({
        name: 'StudentAllDiscuss'
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>
