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
        <el-main style="padding-right: 10%; padding-left: 10%">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找学生"
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
          <el-card v-for="(student, index) in studentList" :key="index">
            <el-row>
              <el-col :offset="2" :span="2">
                <el-empty :image-size="40" style="margin: 0 !important; padding: 0 !important;"></el-empty>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <span style="font-size: 16px"><strong>{{ student.name }}</strong></span>
                </el-row>
                <el-row>
                  <el-tag type="info">学号</el-tag><span style="color: gray">&nbsp;&nbsp;{{student.id}}</span>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
<!--          <el-table :data="studentList" v-loading="loading">-->
<!--            <el-table-column label="学号" prop="id"></el-table-column>-->
<!--            <el-table-column label="姓名" prop="name"></el-table-column>-->
<!--          </el-table>-->
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
export default {
  name: 'AdminTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      studentList: [
        {
          id: 19373686,
          name: '欧阳奎'
        },
        {
          id: 19373135,
          name: '田旗舰'
        },
        {
          id: 19373136,
          name: '郭明明'
        }
      ],
      inputSearch: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentList()
  },
  methods: {
    getStudentList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.studentList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
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
