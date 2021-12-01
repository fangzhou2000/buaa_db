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
        <el-table :data="myCourseList" v-loading="loading">
          <el-table-column label="课程ID" prop="id"></el-table-column>
          <el-table-column label="课程名称（可点击查看信息）">
              <template slot-scope="scope">
                <el-link type="primary" v-on:click="getCourseInfo(scope.$index)">
                  {{myCourseList[scope.$index].name}}
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
          <el-table-column label="修改课程">
            <template slot-scope="scope">
              <el-button v-on:click="changeCourse(scope.$index)" type="warning" size="small">修改课程</el-button>
            </template>
          </el-table-column>
          <el-table-column label="停课">
            <template slot-scope="scope">
              <el-button v-on:click="cancelCourse(scope.$index)" type="danger" size="small">停课</el-button>
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
  name: 'ManageCourse',
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
      }, {
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
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
    this.getTeacherCourseList()
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.myCourseList[index]
      that.courseInfoVisible = true
    },
    getTeacherCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherCourseList/',
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
    changeCourse: function (index) {
      console.log(index)
      let that = this
      let materialIdString = ''
      for (var i = 0; i < that.myCourseList[index].materialList.length; i++) {
        if (i === 0) {
          materialIdString = (that.myCourseList[index].materialList[i].id)
        } else {
          materialIdString = materialIdString + ',' + (that.myCourseList[index].materialList[i].id)
        }
      }
      this.$router.push({
        path: '/TeacherCourse/ChangeCourse',
        // 这里不能使用params传递参数，详见：
        // https://blog.csdn.net/qq_37548296/article/details/90446430
        query: {
          id: that.myCourseList[index].id,
          name: that.myCourseList[index].name,
          materialIdString: materialIdString,
          introduction: that.myCourseList[index].introduction
        }
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
