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
        <el-main>
        <el-table :data="courseList" v-loading="loading">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称（可点击查看信息）">
              <template slot-scope="scope">
                <el-link type="primary" v-on:click="getCourseInfo(scope.$index)">
                  {{courseList[scope.$index].name}}
                </el-link>
                <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
                  <el-row class="info">
                    课程名称(id)：{{courseInfo.name}}({{courseInfo.id}})
                  </el-row>
                  <el-row class="info">
                    学习材料(id)：<a v-for="(m) in courseInfo.materialList" v-bind:key="m.id">{{m.name}}({{m.id}})，</a>
                  </el-row>
                  <el-row class="info">
                    课程介绍：{{courseInfo.introduction}}
                  </el-row>
                  <div slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="courseInfoVisible = false">确 定</el-button>
                  </div>
                </el-dialog>
              </template>
            </el-table-column>
        </el-table>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'AllCourse',
  components: {TeacherNav, TeacherHeading},
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
      loading: true,
      userNickName: '',
      userName: '',
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
        introduction: ''
      }, {
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
      }]
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
      }).catch(function (error) {
        console.log(error)
        that.loading = false
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

<style scoped>
 @import "../../../assets/css/nav.css";
 @import "../../../assets/css/back.css";
</style>
