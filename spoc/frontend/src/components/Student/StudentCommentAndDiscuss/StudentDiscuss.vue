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
            <el-input class="input" v-model="input.content" type="textarea" :rows="2" placeholder="与主题相关的讨论">
            </el-input>
          </el-col>
        </el-row>
        <el-divider>楼主</el-divider>
          <el-row class="time">
            {{postTheme.time}}
          </el-row>
          <el-row class="userName">
            {{postTheme.userNickName}}({{postTheme.userName}}) :
          </el-row>
          <el-row class="content">
            {{postTheme.content}}
          </el-row>
          <el-row class="delete">
            <div v-if="postTheme.userName === userName">
              <el-link type="danger" v-on:click="deletePostTheme">删除</el-link>
            </div>
          </el-row>
        <el-divider>跟贴</el-divider>
        <div v-for="(post) in postList" v-bind:key="post">
          <el-row class="time">
            {{post.time}}
          </el-row>
          <el-row class="userName">
            {{post.userNickName}}({{post.userName}}) :
          </el-row>
          <el-row class="content">
            {{post.content}}
          </el-row>
          <el-row class="delete">
            <div v-if="post.userName === userName">
              <el-link type="danger" v-on:click="deletePost(post.id)">删除</el-link>
            </div>
          </el-row>
          <el-divider></el-divider>
        </div>
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
    color: #e2e2e2;
  }
  .userName {
    font-size: small;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
    word-break: break-all;
  }
</style>

<script>
import StudentNav from '../StudentNav'

export default {
  name: 'StudentDiscuss',
  components: {StudentNav},
  data: function () {
    return {
      postTheme: {
        id: '测试id',
        userName: 'admin',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: '111'
      },
      input: {
        content: ''
      },
      postList: [{
        id: '1',
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
        time: '2021-11-19 11:11:11'
      }, {
        id: '1',
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11'
      }, {
        id: '1',
        userName: '学号3',
        userNickName: '学生3',
        content: '课程评价内容3',
        time: '2021-11-19 11:11:11'
      }, {
        id: '1',
        userName: 'admin',
        userNickName: '学生1',
        content: '课程评价内容1',
        time: '2021-11-19 11:11:11'
      }, {
        id: '1',
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11'
      }, {
        id: '1',
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
    deletePostTheme: function () {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'DeletePostTheme/',
        method: 'get',
        params: {
          postThemeId: that.postThemeId
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('删除成功')
          that.returnStudentAllDiscuss()
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
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
    buildPost: function () {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'BuildPost/',
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
    deletePost: function (postId) {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'DeletePost/',
        method: 'get',
        params: {
          postId: postId
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('删除成功')
          that.getPostList()
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
