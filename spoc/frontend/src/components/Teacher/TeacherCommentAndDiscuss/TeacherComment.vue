<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header @back="returnStudentAllComment" :content="courseName" style="margin-bottom: 2%">
          </el-page-header>
          <el-card shadow="hover" style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="1" :span="2">
                <el-row>
                  <el-image :src="courseImg" lazy></el-image>
                </el-row>
<!--                <el-row>-->
<!--                  <div><strong>评分</strong></div>-->
<!--                  <el-rate-->
<!--                    v-model="courseAssessment"-->
<!--                    disabled-->
<!--                    show-score-->
<!--                    text-color="#ff9900"-->
<!--                    score-template="{courseAssessment}">-->
<!--                  </el-rate>-->
<!--                </el-row>-->
              </el-col>
              <el-col :offset="2" :span="18">
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
                  <div style="font-size: 12px">
                    <h4>课程概述</h4>
                    <p>{{courseIntroduction}}</p>
                    <h4>课程资料</h4>
                    <p>{{courseMaterial}}</p>
                  </div>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-row>
            <el-divider></el-divider>
          </el-row>

          <div v-for="(comment) in commentList" v-bind:key="comment">
            <el-row class="time">
              <el-col :span="1">
                <el-avatar></el-avatar>
              </el-col>
              <el-col :span="3">
                <el-row class="userName">
                  {{comment.userNickName}}({{comment.userName}}) :
                </el-row>
                <el-row>{{comment.time}}</el-row>
              </el-col>
              <el-col :span="20" class="content">
                <el-row class="content-of-comment">
                {{comment.content}}
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
    word-break: break-all;
  }
</style>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
export default {
  name: 'TeacherComment',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      userName: '前端测试用户名',
      userNickName: '前端测试姓名',
      courseId: '前端测试课程id',
      courseName: '前端测试课程名称',
      courseIntroduction: '前端测试课程介绍',
      courseAssessment: '5',
      courseMaterial: '前端测试学习资料',
      contentInput: '',
      courseImg: CourseImg,
      time: '',
      commentList: [{
        id: 1,
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1',
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
    this.courseIntroduction = this.$route.query.courseIntroduction
    // this.courseAssessment = this.$route.query.courseAssessment
    this.courseMaterial = this.$route.query.courseMaterial
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
    returnStudentAllComment: function () {
      let that = this
      that.$router.push({
        name: 'TeacherAllComment'
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
