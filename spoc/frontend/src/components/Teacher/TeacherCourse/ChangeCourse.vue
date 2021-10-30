<template>
<div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userName}} 修改 {{course.name}}</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-form label-position="top">
          <el-form-item label="课程名称">
            <el-col :span="6">
              <el-input v-model="course.name"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="学习材料 (如有多个请用','隔开)">
            <el-col :span="6">
              <el-input v-model="materialIdString"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col :span="6">
              <el-button v-on:click="changeCourse" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
export default {
  name: 'ChangeCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      id: '',
      course: {
        name: '前端测试课程',
        materialIdList: ['1', '2']
      },
      materialIdString: '123'
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.id = this.$route.params.id
    this.getCourseInfo()
    for (var i = 0; i < this.course.materialIdList.length; i++) {
      if (i === 0) {
        this.materialIdString = ''
      }
      if (i < this.course.materialIdList.length - 1) {
        this.materialIdString += this.course.materialIdList[i] + ','
      } else {
        this.materialIdString += this.course.materialIdList[i]
      }
    }
  },
  methods: {
    getCourseInfo: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCourseInfo/',
        method: 'get',
        params: {
          id: that.id
        }
      }).then(function (response) {
        console.log(response.data)
        that.course = response.data
        for (var i = 0; i < that.course.materialIdList.length; i++) {
          if (i === 0) {
            this.materialIdString = ''
          }
          if (i < that.course.materialIdList.length - 1) {
            that.materialIdString += that.course.materialIdList[i] + ','
          } else {
            that.materialIdString += that.course.materialIdList[i]
          }
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    changeCourse: function () {
      let that = this
      that.course.materialIdList = that.materialIdString.split(',')
      this.$http.request({
        url: that.$url + 'ChangeCourse/',
        method: 'get',
        params: {
          id: that.id,
          course: that.course
        }
      }).then(function (response) {
        console.log(response.data)
        alert('修改成功')
        that.$router.push({
          name: 'ManageCourse'
        })
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
