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
        <el-main style="padding-left: 30%; padding-right: 10%">
        <el-form label-position="top" v-loading="loading" >
          <el-form-item label="课程名称">
            <el-col :span="12">
              <el-input v-model="course.name"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="学习材料ID (如有多个请用','隔开)">
<!--            <el-col :span="6">-->
<!--              <el-input v-model="materialIdString"></el-input>-->
<!--            </el-col>-->
            <el-select v-model="materialIdString" multiple placeholder="请选择" style="width: 50%">
              <el-option
                v-for="(item, index) in materialList"
                :key="index"
                :label="item.name"
                :value="item.id">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="课程介绍">
            <el-col :span="12">
              <quill-editor ref="text" v-model="course.introduction" style="height: 200px"></quill-editor>
            </el-col>
          </el-form-item>
          <el-form-item style="margin-top: 10%">
            <el-col :span="6">
              <el-button v-on:click="buildCourse" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  name: 'BuildCourse',
  components: {TeacherNav, TeacherHeading, quillEditor},
  data: function () {
    return {
      loading: false,
      userNickName: '',
      userName: '',
      materialIdString: '',
      materialList: '',
      course: {
        name: '',
        materialIdList: [],
        introduction: ''
      }
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
    this.getMaterialList()
  },
  methods: {
    getMaterialList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetMaterialList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.materialList = response.data
      }).catch(function (error) {
        that.loading = false
        console.log(error)
      })
    },
    buildCourse: function () {
      let that = this
      that.loading = true
      that.course.materialIdList = that.materialIdString
        // .split(',')
      console.log(that.course.materialIdList)
      this.$http.request({
        url: that.$url + 'BuildCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          course: that.course
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.status = response.data
        if (that.status === 0) {
          that.$message.success('创建成功')
          that.materialIdString = ''
          that.course = {
            name: '',
            materialIdList: []
          }
        } else if (that.status === 1) {
          that.$message.error('学习材料编号错误')
        } else if (that.status === 2) {
          that.$message.error('课程名称不能为空')
        }
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
