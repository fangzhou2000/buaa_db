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
          <el-row>
            <el-col :span="14" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找您的相关课程"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 5%"></el-input>
                </el-col>
                <el-col :span="2">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: right"
                    @click="searchCourse(inputSearch)"
                    circle></el-button>
                </el-col>
              </el-row>
              <el-card
                v-for="(course, index) in showCourseList" :key="index"
                v-loading="loading"
                shadow="hover"
                style="font-size: small; margin-bottom: 2%;">
                <div slot="header" class="clearfix">
                  <el-col :span="2">
                    <el-image :src="courseImg" lazy></el-image>
                  </el-col>
                  {{ course.name }}
                  <el-button v-on:click="commentCourse(index)" type="text" style="font-size: smaller; float: right">
                    进入评价
                  </el-button>
                  <el-rate
                    v-model="course.avgDegree"
                    disabled
                    show-score
                    text-color="#ff9900">
                  </el-rate>
                </div>
                <div
                  style="font-size: x-small; text-overflow: ellipsis ;max-height: 50px; overflow: hidden; white-space: nowrap;">
                  <span v-html="course.introduction"></span>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8" :offset="2" class="right-information">
              <el-card shadow="hover" style="width: 100%">
                <el-row>
                  <el-col :span="2" >
                    &nbsp;
                  </el-col>
                  <el-col :span="6">
                    <el-image :src="studentImg" lazy></el-image>
                  </el-col>
                  <el-col :span="2" >
                    &nbsp;
                  </el-col>
                  <el-col :span="12" :offset="1">
                    <el-descriptions :column="1">
                      <el-descriptions-item label="用户名">{{ userNickName }}</el-descriptions-item>
                      <el-descriptions-item label="学号">{{ userName }}</el-descriptions-item>
                      <el-descriptions-item label="已选课程">{{ courseNum }}</el-descriptions-item>
                      <el-descriptions-item label="参与评价">{{ commentNum }}</el-descriptions-item>
                    </el-descriptions>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider></el-divider>
                </el-row>
                <el-row>
                  <el-descriptions :column="1" v-if="showIt">
                    <el-descriptions-item label="用户名">{{ userNickName }}</el-descriptions-item>
                    <el-descriptions-item label="学号">{{ userName }}</el-descriptions-item>
                  </el-descriptions>
                </el-row>
                <el-row class="el-row-button-head">
                  <el-button @click="changeShowIt" type="text" class="el-row-button">
                    <i v-if="showIt" class="el-icon-caret-top">隐藏</i>
                    <i v-else class="el-icon-caret-bottom">展开</i>
                  </el-button>
                </el-row>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
import StudentImg from '../../../assets/img/student.png'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'

export default {
  name: 'StudentAllComment',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      commentNum: '',
      courseNum: '',
      courseImg: CourseImg,
      studentImg: StudentImg,
      inputSearch: '',
      showIt: false,
      courseList: [{
        id: '',
        name: '',
        introduction: '',
        materialList: [{
          id: '',
          name: ''
        }],
        avgDegree: 3.0
      }],
      showCourseList: [{
        id: '',
        name: '',
        materialList: [{
          id: '',
          name: ''
        }],
        introduction: '',
        avgDegree: 3.0
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
    this.getStudentCommentNum()
    this.getStudentCourseNum()
    this.showCourseList = this.courseList
  },
  methods: {
    getStudentCourseNum: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetStudentCourseNum/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseNum = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    getStudentCommentNum: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetStudentCommentNum/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.commentNum = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    getCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCourseList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.courseList = response.data
        that.showCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    commentCourse: function (index) {
      let that = this
      this.$router.push({
        path: '/StudentCommentAndDiscuss/StudentComment',
        query: {
          courseId: that.showCourseList[index].id
        }
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    changeShowIt: function () {
      this.showIt = !this.showIt
    },
    searchCourse: function (inputSearch) {
      this.showCourseList = this.searchByIndexOf(inputSearch, this.courseList)
    },
    searchByIndexOf: function (keyWord, list) {
      if (!(list instanceof Array)) {
        return
      } else if (keyWord === '') {
        return list
      }
      const len = list.length
      const arr = []
      for (let i = 0; i < len; i++) {
        // 如果字符串中不包含目标字符会返回-1
        if (list[i].name.indexOf(keyWord) >= 0) {
          arr.push(list[i])
        }
      }
      return arr
    }
  }
}
</script>

<style scoped>
@import "../../../assets/css/back.css";

.el-row-button {
  width: 100% !important;
}

.el-row-button :hover {
  background-color: initial;
}

.el-row-button-head :hover {
  background-color: hsla(0, 0%, 74%, 0.2);
}
</style>
