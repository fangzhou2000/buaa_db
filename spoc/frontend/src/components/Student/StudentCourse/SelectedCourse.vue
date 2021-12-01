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
          <el-table :data="myCourseList" v-loading="loading" >
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称（可点击查看信息）">
              <template slot-scope="scope">
                <el-link type="primary" v-on:click="courseInfoVisible = true">
                  {{myCourseList[scope.$index].name}}
                </el-link>
                <el-dialog title="提示" :visible.sync="courseInfoVisible" width="50%">
                  <el-row class="info">
                    课程名称(id)：{{myCourseList[scope.$index].name}}({{myCourseList[scope.$index].id}})
                  </el-row>
                  <el-row class="info">
                    学习材料(id)：<a v-for="(m) in myCourseList[scope.$index].materialList" v-bind:key="m.id">{{m.name}}({{m.id}})，</a>
                  </el-row>
                  <el-row class="info">
                    课程介绍：{{myCourseList[scope.$index].introduction}}
                  </el-row>
                  <div slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="courseInfoVisible = false">确定</el-button>
                  </div>
                </el-dialog>
              </template>
            </el-table-column>
            <el-table-column label="退课">
              <template slot-scope="scope">
                <el-button v-on:click="dropCourse(scope.$index)" type="danger" size="small">退课</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
export default {
  name: 'StudentCourse',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      courseInfoVisible: false,
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
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentCourseList()
  },
  methods: {
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

<style scoped>
  @import "../../../assets/css/back.css";
</style>
