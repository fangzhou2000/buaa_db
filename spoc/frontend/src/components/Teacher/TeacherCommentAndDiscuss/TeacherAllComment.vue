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
        <el-main style="padding-right: 10%; padding-left: 10%">
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
                  <el-button v-on:click="commentCourse(index)" type="text" style="font-size: small; float: right">
                    查看评价
                  </el-button>
                  <el-rate
                    v-model="course.avgDegree"
                    disabled
                    show-score
                    text-color="#ff9900">
                  </el-rate>
                </div>
                <div
                  style="font-size: smaller; text-overflow: ellipsis ;max-height: 50px; overflow: hidden; white-space: nowrap;">
                  <span v-html="course.introduction"></span>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8" :offset="2" class="right-information">
              <el-card shadow="hover" style="width: 100%">
                <el-row>
                  <el-col :span="11">
                    <el-image :src="teacherImg" lazy></el-image>
                  </el-col>
                  <el-col :span="12" :offset="1">
                    <el-descriptions :column="1">
                      <el-descriptions-item label="用户名">{{userNickName}}</el-descriptions-item>
                      <el-descriptions-item label="工号">{{userName}}</el-descriptions-item>
                      <el-descriptions-item label="开设课程">{{courseNum}}</el-descriptions-item>
                    </el-descriptions>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider></el-divider>
                </el-row>
                <el-row>
                  <el-descriptions :column="1" v-if="showIt">
                      <el-descriptions-item label="用户名">{{userNickName}}</el-descriptions-item>
                      <el-descriptions-item label="工号">{{userName}}</el-descriptions-item>
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
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
import TeacherImg from '../../../assets/img/teacher.png'
export default {
  name: 'TeacherAllComment',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      courseNum: '1',
      inputSearch: '',
      showIt: false,
      teacherImg: TeacherImg,
      courseImg: CourseImg,
      courseList: [{
        id: '1',
        name: '前端测试课程1',
        materialIdString: '1,2',
        materialNameString: 'book1,book2',
        assessment: '5'
      }, {
        id: '2',
        name: '前端测试课程2',
        materialIdString: '1,2',
        materialNameString: 'book1,book2',
        assessment: '5'
      }],
      showCourseList: this.courseList
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
    this.getTeacherCourseNum()
  },
  methods: {
    getTeacherCourseNum: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetTeacherCourseNum/',
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
        path: '/TeacherCommentAndDiscuss/TeacherComment',
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
