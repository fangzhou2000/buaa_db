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
        <el-page-header @back="returnManageCourse" :content="name" style="margin-bottom: 2%">
        </el-page-header>
        <el-form label-position="top" v-loading="loading">
          <el-form-item label="课程名称">
            <el-col :span="12">
              <el-input v-model="name"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="学习材料">
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
              <quill-editor ref="text" v-model="introduction" style="height: 200px"></quill-editor>
            </el-col>
          </el-form-item>
          <el-form-item style="margin-top: 20%">
            <el-col :span="6">
              <el-button v-on:click="changeCourse" type="primary">确认</el-button>
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
  /* eslint-disable */
  name: 'ChangeCourse',
  components: {TeacherNav, TeacherHeading, quillEditor},
  data: function () {
    return {
      loading: false,
      userName: '',
      userNickName: '',
      id: '',
      name: '',
      materialIdString: '',
      materialIdList: [],
      introduction: '',
      materialList: ''
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.id = this.$route.query.id
    this.name = this.$route.query.name
    this.materialIdString = this.$route.query.materialIdString
    this.introduction = this.$route.query.introduction
    this.getMaterialList()
  },
  methods: {
    getCourseInfo: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCourseInfo/',
        method: 'get',
        params: {
          id: that.id
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false

        // that.materialList = response.data
      }).catch(function (error) {
        that.loading = false
        console.log(error)
      })
    },
    returnManageCourse: function () {
      let that = this
      that.$router.push({
        name: 'ManageCourse'
      })
    },
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
    changeCourse: function () {
      let that = this
      // that.loading = true
      // that.materialIdList = that.materialIdString.split(',')
      console.log(that.materialIdList)
      console.log(that.materialIdString)
      this.$http.request({
        url: that.$url + 'ChangeCourse/',
        method: 'get',
        params: {
          id: that.id,
          name: that.name,
          // materialIdList: that.materialIdList,
          // 这里传List接受不到数据，改为传string
          materialIdString: that.materialIdString.join(','),
          introduction: that.introduction,
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        if (response.data === 0) {
          that.$message.success('修改成功')
          that.$router.push({
            name: 'ManageCourse'
          })
        } else if (response.data === 1) {
          that.$message.error('学习材料编号不存在')
        } else if (response.data === 2) {
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
