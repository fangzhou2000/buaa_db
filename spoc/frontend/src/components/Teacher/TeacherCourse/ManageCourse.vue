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
        <el-main style="padding-left: 10%; padding-right: 10%">
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
          <el-card v-for="(course, index) in showMyCourseList" :key="index" shadow="hover" style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="2" :span="2">
                <el-empty :image-size="50" style="margin: 0 !important; padding: 0 !important;"></el-empty>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="info">课程编号</el-tag>&nbsp;&nbsp;<span style="color: gray">{{course.id}}</span>
                </el-row>
              </el-col>
              <el-col :span="2">
                <el-button-group style="margin-bottom: 1%">
                  <el-button type="primary" icon="el-icon-edit" v-on:click="changeCourse(index)">编辑</el-button>
                </el-button-group>
                <el-button-group>
                  <el-button type="primary" icon="el-icon-delete" v-on:click="cancelCourse(index)">停课</el-button>
                </el-button-group>
              </el-col>
            </el-row>
          </el-card>

          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info" direction="vertical">
              <el-descriptions-item label="课程名称(ID)">
                &nbsp;&nbsp;{{courseInfo.name}}({{courseInfo.id}})
              </el-descriptions-item>
              <el-descriptions-item label="学习材料ID">
                &nbsp;&nbsp;
                <a v-for="(m) in courseInfo.materialList" v-bind:key="m.id">{{ m.name }}({{ m.id }})，</a>
              </el-descriptions-item>
              <el-descriptions-item label="课程介绍">
                &nbsp;&nbsp;
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

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'

export default {
  /* eslint-disable */
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
          id: '04',
          name: '材料03'
        }],
        introduction: ''
      }],
      showMyCourseList: this.myCourseList,
      inputSearch: ''
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
      that.courseInfo = that.showMyCourseList[index]
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
        that.showMyCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    changeCourse: function (index) {
      console.log(index)
      let that = this
      let materialIdString = ''
      for (var i = 0; i < that.showMyCourseList[index].materialList.length; i++) {
        if (i === 0) {
          materialIdString = (that.showMyCourseList[index].materialList[i].id)
        } else {
          materialIdString = materialIdString + ',' + (that.showMyCourseList[index].materialList[i].id)
        }
      }
      this.$router.push({
        path: '/TeacherCourse/ChangeCourse',
        // 这里不能使用params传递参数，详见：
        // https://blog.csdn.net/qq_37548296/article/details/90446430
        query: {
          id: that.showMyCourseList[index].id,
          name: that.showMyCourseList[index].name,
          materialIdString: materialIdString,
          introduction: that.showMyCourseList[index].introduction
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
            id: that.showMyCourseList[index].id
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
    },
    searchCourse: function (inputSearch) {
      let that = this
      that.showMyCourseList = this.searchByIndexOf(inputSearch, that.myCourseList)
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
