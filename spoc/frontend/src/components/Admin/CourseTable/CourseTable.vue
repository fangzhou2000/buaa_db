<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
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
            <el-table-column label="删除">
              <template slot-scope="scope">
                <el-button v-on:click="cancelCourse(scope.$index)" type="danger" size="small">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
export default {
  name: 'CourseTable',
  components: {AdminHeading, AdminNav},
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
      }).catch(function (error) {
        that.loading = false
        console.log(error)
      })
    },
    cancelCourse: function (index) {
      this.$confirm('此操作将停开并删除该课程，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        that.loading = true
        this.$http.request({
          url: that.$url + 'CancelCourse/',
          method: 'get',
          params: {
            userName: that.userName,
            id: that.myCourseList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('停课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getTeacherCourseList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
      })
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
