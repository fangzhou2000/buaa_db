<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main style="padding-right: 10%; padding-left: 10%">
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
              <el-col :offset="2" :span="14">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="primary">课程编号<span>&nbsp;&nbsp;{{course.id}}</span></el-tag>
                </el-row>
              </el-col>
              <el-col :span="2">
                <el-button-group style="margin-top: 2%">
                  <el-button v-on:click="selectCourse(index)" type="primary">选课</el-button>
                </el-button-group>
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
              <el-descriptions-item label="课程介绍">&nbsp;&nbsp;
                {{ courseInfo.introduction }}
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

<style scoped>
@import "../../../assets/css/back.css";
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
export default {
  /* eslint-disable */
  name: 'SelectCourse',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      courseInfoVisible: false,
      courseInfo: {
        id: '',
        name: '',
        materialList: [{
          id: '',
          name: ''
        }],
        introduction: ''
      },
      courseImg: CourseImg,
      loading: false,
      userName: '',
      userNickName: '',
      courseList: [{
        id: '1',
        name: '课程1',
        materialList: [{
          id: '01',
          name: '材料01'
        }, {
          id: '02',
          name: '材料02'
        }],
        introduction: '',
        avgDegree: 2.0
      }],
      showCourseList: this.courseList,
      inputSearch: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.courseList[index]
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
    selectCourse (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'SelectCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.showCourseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        var status = response.data
        if (status === 0) {
          that.$message.success('选课成功')
        } else if (status === 1) {
          that.$message.info('已选择该课程')
        } else {
          that.$message.error('!')
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
