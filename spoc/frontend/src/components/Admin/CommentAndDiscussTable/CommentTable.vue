<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
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
              <el-card v-for="(course, index) in showCourseList" :key="index" shadow="hover" style="margin-bottom: 2%">
                <el-row>
                  <el-col :offset="1" :span="2">
                    <el-image :src="courseImg" lazy></el-image>
                  </el-col>
                  <el-col :offset="2" :span="18">
                    <el-row>
                      <el-col :span="18">
                        <strong>{{course.name}}</strong>
                      </el-col>
                      <el-col :span="4" :offset="2">
                        <el-button v-on:click="commentCourse(index)" type="text" style="float: right">查看</el-button>
                      </el-col>
                    </el-row>
                    <el-row>
                      <el-divider>
                      </el-divider>
                    </el-row>
                    <el-row>
                      <div style="font-size: 12px; text-overflow: ellipsis ;max-height: 100px; overflow: hidden; white-space: nowrap;">
                        {{course.introduction}}
                      </div>
                    </el-row>
                  </el-col>
<!--                  <el-col :offset="1" :span="3">-->
<!--                    <div><strong>评分</strong></div>-->
<!--                    <el-rate-->
<!--                      v-model="course.assessment"-->
<!--                      disabled-->
<!--                      show-score-->
<!--                      text-color="#ff9900"-->
<!--                      score-template="{course.assessment}">-->
<!--                    </el-rate>-->
<!--                  </el-col>-->
                </el-row>
              </el-card>
            </el-col>
          </el-row>
<!--          <el-table :data="courseList"  v-loading="loading">-->
<!--            <el-table-column label="课程ID" prop="id"></el-table-column>-->
<!--            <el-table-column label="课程名称" prop="name"></el-table-column>-->
<!--            <el-table-column label="评价"> <template slot-scope="scope">-->
<!--          <el-button v-on:click="commentCourse(scope.$index)" type="primary" size="small">评价</el-button>-->
<!--        </template></el-table-column>-->
<!--          </el-table>-->
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
export default {
  name: 'CommentTable',
  components: {AdminNav, AdminHeading},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      inputSearch: '',
      courseList: [{
        id: '1',
        name: '前端测试课程1',
        materialIdString: '1,2',
        materialNameString: 'book1,book2'
      }, {
        id: '2',
        name: '前端测试课程2',
        materialIdString: '1,2',
        materialNameString: 'book1,book2'
      }],
      courseImg: CourseImg,
      showCourseList: this.courseList
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
  },
  methods: {
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
        path: '/CommentAndDiscussTable/Comment',
        query: {
          courseId: that.showCourseList[index].id,
          courseName: that.showCourseList[index].name
        }
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
  @import "../../../assets/css/back.css";
</style>
