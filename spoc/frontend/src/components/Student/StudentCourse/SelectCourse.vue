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
        <el-main>
          <el-table :data="courseList" v-loading="loading" >
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称（可点击查看信息）">
              <template slot-scope="scope">
                <el-link type="primart" v-on:click="courseInfoVisible = true">
                  {{courseList[scope.$index].name}}
                </el-link>
                <el-dialog title="提示" :visible.sync="courseInfoVisible" width="50%">
                  <el-row class="info">
                    课程名称(id)：{{courseList[scope.$index].name}}({{courseList[scope.$index].id}})
                  </el-row>
                  <el-row class="info">
                    学习材料(id)：<a v-for="(m) in courseList[scope.$index].materialList" v-bind:key="m.id">{{m.name}}({{m.id}})，</a>
                  </el-row>
                  <el-row class="info">
                    课程介绍：{{courseList[scope.$index].introduction}}
                  </el-row>
                  <el-button @click="courseInfoVisible = false">取 消</el-button>
                  <el-button type="primary" @click="courseInfoVisible = false">确 定</el-button>
                </el-dialog>
              </template>
            </el-table-column>
            <el-table-column label="选课">
              <template slot-scope="scope">
                <el-button v-on:click="selectCourse(scope.$index)" type="primary">选课</el-button>
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
  name: 'SelectCourse',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      courseInfoVisible: false,
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
        }]
      }],
      introduction: ''
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
          id: that.courseList[index].id
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
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
