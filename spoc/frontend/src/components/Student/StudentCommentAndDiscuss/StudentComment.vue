<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header @back="returnStudentAllComment" :content="courseName" style="margin-bottom: 2%"></el-page-header>
          <el-card shadow="hover" style="margin-bottom: 1%">
            <el-row>
              <el-col :offset="1" :span="3">
                <el-image :src="courseImg" lazy></el-image>
                <el-row>
                  &nbsp;
                </el-row>
                <el-row style="text-align: center; font-size: medium">
                  课程评分
                </el-row>
                <el-rate
                  align="center"
                  v-model="courseAvgDegree"
                  disabled
                  show-score
                  text-color="#ff9900"></el-rate>
              </el-col>
              <el-col :offset="2" :span="17">
                <el-row>
                  <el-col :span="18">
                    <strong>{{courseName}}</strong>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider>
                  </el-divider>
                </el-row>
                <el-row>
                  <div style="font-size: small">
                    <h3>课程介绍</h3>
                    <span v-html="courseIntroduction"></span>
                    <h3>课程资料</h3>
                    <p><a v-for="(m) in courseMaterialList" v-bind:key="m.id">{{ m.name }}，</a></p>
                  </div>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-row>
            <el-divider></el-divider>
          </el-row>
          <el-row>
            <div style="font-size: medium">
              评分
            </div>
            <el-rate
              style="font-size: medium"
              v-model="degree"
              show-text>
            </el-rate>
          </el-row>
          <el-row>
            &nbsp;
          </el-row>
          <el-row>
            <el-col>
              <el-input class="input" v-model="contentInput" type="textarea" :rows="3" placeholder="对于课程内容、讲课质量、考核方式等的评价">
              </el-input>
            </el-col>
            <el-button v-on:click="commentCourse" type="primary" size="small" style="float: right">添加评价</el-button>
          </el-row>
          <el-divider></el-divider>
          <div v-for="(comment) in commentList" v-bind:key="comment">
            <el-row class="time" v-loading="loading">
              <el-col :span="1">
                <el-image :src="studentImg" fit="contain" lazy></el-image>
              </el-col>
              <el-col :span="3" :offset="1">
                <el-row class="userName">
                  {{comment.userNickName}}({{comment.userName}}) :
                </el-row>
                <el-row>{{comment.time}}</el-row>
              </el-col>
              <el-col :span="19" class="content">
                <el-row class="content-of-comment" v-html="comment.content">
                </el-row>
                <el-row class="delete">
                  <div v-if="comment.userName === userName">
                    <el-link type="danger" v-on:click="deleteComment(comment.id)">删除</el-link>
                  </div>
                </el-row>
              </el-col>
            </el-row>
            <el-divider></el-divider>
          </div>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
  .buttons {
    margin-bottom: 10px;
  }
  .input {
    font-size: medium;
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
    word-break: break-all;
  }
  .content-of-comment {
    color: black;
  }
</style>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
import StudentImg from '../../../assets/img/student.png'
export default {
  name: 'StudentComment',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      loading: true,
      userName: '前端测试用户名',
      userNickName: '前端测试姓名',
      courseId: '前端测试课程id',
      courseName: '前端测试课程名称',
      courseIntroduction: '前端测试课程介绍',
      courseMaterialList: [{
        id: '1',
        name: 'book1'
      }],
      courseAvgDegree: 3.0,
      degree: 5,
      contentInput: '',
      courseImg: CourseImg,
      studentImg: StudentImg,
      time: '',
      commentList: [{
        id: 1,
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1' +
          '课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1课程评价内容1',
        time: '2021-11-19 11:11:11'
      }
      ]
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.courseId = this.$route.query.courseId
    this.getCourseInfo()
    this.getDegree()
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
    getCourseInfo: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCourseInfo/',
        method: 'get',
        params: {
          courseId: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseName = response.data.name
        that.courseIntroduction = response.data.introduction
        that.courseMaterialList = response.data.materialList
      }).catch(function (error) {
        console.log(error)
      })
    },
    getCommentList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCommentList/',
        method: 'get',
        params: {
          courseId: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.commentList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    getDegree: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetDegree/',
        method: 'get',
        params: {
          id: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseAvgDegree = response.data.avgDegree
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
          time: that.time,
          degree: that.degree
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('评价成功')
          that.getCommentList()
          that.getDegree()
          that.contentInput = ''
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    deleteComment: function (commentId) {
      this.$confirm('此操作将永久删除该评价，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeleteComment/',
          method: 'get',
          params: {
            commentId: commentId
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.getCommentList()
            that.getDegree()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
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
