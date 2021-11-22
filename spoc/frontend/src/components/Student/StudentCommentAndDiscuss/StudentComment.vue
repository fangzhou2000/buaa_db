<template>
  <div>
   <el-container class="header">
      <el-header>
        <span>评价 {{courseName}}</span>
        <el-button class="exit" v-on:click="goToHelloWorld">退出登录</el-button>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <StudentNav></StudentNav>
      </el-aside>
      <el-main>
        <el-row class="buttons">
          <el-button v-on:click="commentCourse" type="primary" size="small" >发表评价</el-button>
          <el-button v-on:click="returnStudentAllComment" type="primary" size="small">返回</el-button>
        </el-row>
        <el-row class="buttons">
          <el-col :span="20">
            <el-input class="input" v-model="contentInput" type="textarea" :rows="2" placeholder="对于课程内容、讲课质量、考核方式等的评价">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <div v-for="(comment) in commentList" v-bind:key="comment">
          <el-row class="time">
            {{comment.time}}
          </el-row>
          <el-row class="userName">
            {{comment.userNickName}}({{comment.userName}}) :
          </el-row>
          <el-row class="content">
            {{comment.content}}
          </el-row>
          <el-row class="delete">
            <div v-if="comment.userName === userName">
              <el-link type="danger" v-on:click="deleteComment(comment.id)">删除</el-link>
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
    font-size: medium;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
  }
</style>

<script>
import StudentNav from '../StudentNav'

export default {
  name: 'StudentComment',
  components: {StudentNav},
  data: function () {
    return {
      userName: '前端测试用户名',
      userNickName: '前端测试姓名',
      courseId: '前端测试课程id',
      courseName: '前端测试课程名称',
      contentInput: '',
      time: '',
      commentList: [{
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1',
        time: '2021-11-19 11:11:11'
      }, {
        userName: 'admin',
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
      }
      ]
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.courseId = this.$route.query.courseId
    this.courseName = this.$route.query.courseName
    this.getCommentList()
  },
  methods: {
    getTime: function () {
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      this.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    getCommentList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCommentList/',
        method: 'get',
        params: {
          courseId: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.commentList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    commentCourse: function () {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'CommentCourse/',
        method: 'get',
        params: {
          courseId: that.courseId,
          userName: that.userName,
          userNickName: that.userNickName,
          content: that.contentInput,
          time: that.time
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('评价成功')
          that.getCommentList()
          that.contentInput = ''
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    deleteComment: function (commentId) {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'DeletePost/',
        method: 'get',
        params: {
          commentId: commentId
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
    returnStudentAllComment: function () {
      let that = this
      that.$router.push({
        name: 'StudentAllComment'
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
