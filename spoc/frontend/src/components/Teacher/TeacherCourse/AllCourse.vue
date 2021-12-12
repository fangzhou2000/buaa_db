<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main style="padding-right: 10%; padding-left: 10%">
<!--          <el-table :data="courseList" v-loading="loading">-->
<!--            <el-table-column label="课程ID" prop="id"></el-table-column>-->
<!--            <el-table-column label="课程名称（可点击查看信息）">-->
<!--              <template slot-scope="scope">-->
<!--                <el-link type="primary" v-on:click="getCourseInfo(scope.$index)">-->
<!--                  {{ courseList[scope.$index].name }}-->
<!--                </el-link>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--          </el-table>-->
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找您的相关课程"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 5%"></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="float: right"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
          </el-row>
          <el-card v-for="(course, index) in showCourseList" :key="index"
                   v-loading="loading"
                   shadow="hover"
                   style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="1" :span="2">
                <el-image :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="info">课程编号<span>&nbsp;&nbsp;{{course.id}}</span></el-tag>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info">
              <el-descriptions-item label="课程名称(ID)">
                &nbsp;&nbsp;
                {{courseInfo.name}}({{courseInfo.id}})
              </el-descriptions-item>
              <el-descriptions-item label="学习材料(ID)">
                &nbsp;&nbsp;
                <a v-for="(m) in courseInfo.materialList" v-bind:key="m.id">{{ m.name }}({{ m.id }})，</a>
              </el-descriptions-item>
              <el-descriptions-item label="课程介绍">
                &nbsp;&nbsp;
                <span v-html="courseInfo.introduction"></span>
              </el-descriptions-item>
            </el-descriptions>
            <div slot="footer" class="dialog-footer">
              <el-button type="primary" @click="courseInfoVisible = false">确 定</el-button>
            </div>
          </el-dialog>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
export default {
  /* eslint-disable */
  name: 'AllCourse',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      courseInfoVisible: false,
      courseImg: CourseImg,
      courseInfo: {
        id: '',
        name: '',
        materialList: [{
          id: '',
          name: ''
        }],
        introduction: ''
      },
      loading: true,
      userNickName: '',
      userName: '',
      courseList: [{
        id: '2',
        name: '课程2',
        materialList: [{
          id: '03',
          name: '材料03'
        }, {
          id: '04',
          name: '材料04'
        }],
        introduction: ''
      }],
      showCourseList: this.courseList,
      inputSearch: ''
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
    this.getCourseList()
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.showCourseList[index]
      that.courseInfoVisible = true
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
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
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
@import "../../../assets/css/nav.css";
@import "../../../assets/css/back.css";
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>
