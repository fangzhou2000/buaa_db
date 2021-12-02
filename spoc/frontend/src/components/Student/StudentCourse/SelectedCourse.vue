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
        <el-main>
          <el-table :data="myCourseList" v-loading="loading">
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称（可点击查看信息）">
              <template slot-scope="scope">
                <el-link type="primary" v-on:click="getCourseInfo(scope.$index)">
                  {{ myCourseList[scope.$index].name }}
                </el-link>
              </template>
            </el-table-column>
            <el-table-column label="退课">
              <template slot-scope="scope">
                <el-button v-on:click="dropCourse(scope.$index)" type="danger" size="small">退课</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-row class="info">
              课程名称(id)：{{ courseInfo.name }}({{ courseInfo.id }})
            </el-row>
            <el-row class="info">
              学习材料(id)：<a v-for="(m) in courseInfo.materialList" v-bind:key="m.id">{{ m.name }}({{ m.id }})，</a>
            </el-row>
            <el-row class="info">
              课程介绍：{{ courseInfo.introduction }}
            </el-row>
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

export default {
  /* eslint-disable */
  name: 'StudentCourse',
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
      loading: true,
      userName: '',
      userNickName: '',
      myCourseList: [{
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
      },
        {
          id: '2',
          name: '课程2',
          materialList: [{
            id: '03',
            name: '材料03'
          }, {
            id: '03',
            name: '材料03'
          }],
          introduction: ''
        }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentCourseList()
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.myCourseList[index]
      that.courseInfoVisible = true
    },
    getStudentCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentCourseList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.myCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    dropCourse: function (index) {
      this.$confirm('此操作将退选该课程，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        this.$http.request({
          url: that.$url + 'DropCourse/',
          method: 'get',
          params: {
            userName: that.userName,
            id: that.myCourseList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('退课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getStudentCourseList()
        }).catch(function (error) {
          console.log(error)
        })
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
