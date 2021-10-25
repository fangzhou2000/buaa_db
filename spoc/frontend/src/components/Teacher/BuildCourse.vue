<template>
  <div class="background">
    <el-container>
      <el-header>
        <span>{{userName}} 开设课程</span>
      </el-header>
    </el-container>

    <el-container>
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-form label-width="100px">
          <el-form-item label="课程名称">
            <el-col span="6">
              <el-input placeholder="请输入课程名称" v-model="courseName"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col span="6">
              <el-button v-on:click="buildCourse" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from './TeacherNav'
export default {
  name: 'BuildCourse',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      courseName: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    buildCourse: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'BuildCourse/',
        method: 'get',
        params: {
          userName: that.userName,
          courseName: that.courseName
        }
      }).then(function (response) {
        console.log(response.data)
        that.status = response.data
        if (that.status === 0) {
          alert('创建成功')
        } else {
          alert('!')
        }
      }).catch(function (error) {
        console.log(error)
      })
      that.courseName = ''
    }
  }
}
</script>
