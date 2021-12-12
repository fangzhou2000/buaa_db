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

          <div v-for="(comment) in commentList" v-bind:key="comment">
            <el-row class="time">
              <el-col :span="1">
                <el-avatar :src="studentImg">
                </el-avatar>
              </el-col>
              <el-col :span="3">
                <el-row class="userName">
                  {{comment.userNickName}}({{comment.userName}}) :
                </el-row>
                <el-row>{{comment.time}}</el-row>
              </el-col>
              <el-col :span="20" class="content">
                <el-row class="content-of-comment" style="color: black">
                  <span v-html="comment.content"></span>
                </el-row>
                <el-row class="delete">
                  <div v-if="comment.userName === userName">
                    <el-link type="danger">删除</el-link>
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
import StudentImg from '../../../assets/img/student.png'
export default {
  name: 'TeacherComment',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      courseId: '',
      courseName: '',
      courseIntroduction: '',
      courseMaterialList: [],
      courseAvgDegree: 1.0,
      contentInput: '',
      courseImg: CourseImg,
      studentImg: StudentImg,
      time: '',
      commentList: [{
        id: 1,
        userName: '',
        userNickName: '',
        content: '',
        time: ''
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
        if (that.courseAvgDegree !== 5) {
          that.courseAvgDegree = Number(that.courseAvgDegree).toFixed(1)
        }
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
