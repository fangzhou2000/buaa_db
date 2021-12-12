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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header @back="returnStudentAllDiscuss" :content="postTheme.title" style="margin-bottom: 2%">
          </el-page-header>
          <el-row class="buttons">
          </el-row>
          <el-divider>楼主</el-divider>
          <el-card shadow="hover" style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="2" :span="2">
<!--                <el-row>-->
<!--                  <el-empty :image-size="80" style="margin: 0 !important; padding: 0 !important;"></el-empty>-->
<!--                </el-row>-->
                <el-row class="time">
                  {{postTheme.time}}
                </el-row>
                <el-row class="userName">
                  <el-col v-if="postTheme.isTeacher === 1">
                    {{postTheme.userNickName}}({{postTheme.userName}}) (教师)
                  </el-col>
                  <el-col v-else-if="postTheme.isTeacher === 2">
                    {{postTheme.userNickName}}({{postTheme.userName}}) (管理员)
                  </el-col>
                  <el-col v-else>
                    {{postTheme.userNickName}}({{postTheme.userName}})
                  </el-col>
                </el-row>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row class="content" v-html="postTheme.content">
                </el-row>
                <el-row class="delete">
                  <div v-if="postTheme.userName === userName">
                    <el-link type="danger" v-on:click="deletePostTheme">删除</el-link>
                  </div>
                </el-row>
              </el-col>
              <el-col :offset="1" :span="1">
                <el-button v-on:click="dialogFormVisible = true" type="primary" size="small" >跟贴</el-button>
              </el-col>
            </el-row>
          </el-card>

          <el-dialog :visible.sync="dialogFormVisible">
            <el-input class="input" v-model="input.content" type="textarea" :rows="4" placeholder="与主题相关的讨论">

            </el-input>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="buildPost">确 定</el-button>
            </div>
          </el-dialog>
          <el-divider>跟贴</el-divider>
          <div v-for="(post, index) in postList" v-bind:key="index">
            <el-row>
              <el-col :span="1" :offset="1">
                <el-image v-if="post.isTeacher === 1" :src="teacherImg" lazy></el-image>
                <el-image v-else-if="post.isTeacher === 2" :src="adminImg" lazy></el-image>
                <el-image v-else :src="studentImg" lazy></el-image>
              </el-col>
              <el-col :span="3">
                <el-row class="time">
                  {{post.time}}
                </el-row>
                <el-row class="userName">
                  <div v-if="post.isTeacher === 1">
                    {{post.userNickName}}({{post.userName}}) (教师) :
                  </div>
                  <div v-else-if="post.isTeacher === 2">
                    {{post.userNickName}}({{post.userName}}) (管理员) :
                  </div>
                  <div v-else>
                    {{post.userNickName}}({{post.userName}}) :
                  </div>
                </el-row>
              </el-col>
              <el-col class="content" :span="18" v-html="post.content">
<!--                {{post.content}}-->
              </el-col>
              <el-col class="delete" :span="1" style="float: right">
                <div v-if="post.userName === userName">
                  <el-link type="danger" v-on:click="deletePost(post.id)">删除</el-link>
                </div>
              </el-col>
            </el-row>
            <el-divider></el-divider>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
  .buttons {
    margin-bottom: 10px;
  }
  .input {
    font-size: large;
  }
  .time {
    font-size: small;
    color: #e2e2e2;
  }
  .userName {
    font-size: small;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
    word-break: break-all;
  }
</style>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
import StudentImg from '../../../assets/img/student.png'
import TeacherImg from '../../../assets/img/teacher.png'
import AdminImg from '../../../assets/img/admin.jpg'
export default {
  name: 'StudentDiscuss',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      userName: '前端测试用户名',
      userNickName: '前端测试姓名',
      dialogFormVisible: false,
      studentImg: StudentImg,
      teacherImg: TeacherImg,
      adminImg: AdminImg,
      postTheme: {
        id: '测试id',
        userName: 'admin',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: '111',
        isTeacher: 1
      },
      input: {
        content: ''
      },
      postList: [{
        id: '1',
        userName: '学号1',
        userNickName: '学生1',
        content: '课程评价内容1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
        time: '2021-11-19 11:11:11',
        isTeacher: 0
      }, {
        id: '1',
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11',
        isTeacher: 1
      }, {
        id: '1',
        userName: '学号3',
        userNickName: '学生3',
        content: '课程评价内容3',
        time: '2021-11-19 11:11:11',
        isTeacher: 0
      }, {
        id: '1',
        userName: 'admin',
        userNickName: '学生1',
        content: '课程评价内容1',
        time: '2021-11-19 11:11:11',
        isTeacher: 0
      }, {
        id: '1',
        userName: '学号2',
        userNickName: '学生2',
        content: '课程评价内容2',
        time: '2021-11-19 11:11:11',
        isTeacher: 0
      }, {
        id: '1',
        userName: '学号3',
        userNickName: '学生3',
        content: '课程评价内容3',
        time: '2021-11-19 11:11:11',
        isTeacher: 0
      }],
      time: ''
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.postTheme = this.$route.query.newPostTheme
    this.getPostList()
    console.log('Checking...')
    console.log(this.postTheme)
  },
  methods: {
    getTime: function () {
      let that = this
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      that.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    deletePostTheme: function () {
      this.$confirm('此操作将永久删除该主题贴及其跟贴，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeletePostTheme/',
          method: 'get',
          params: {
            postThemeId: that.postTheme.id
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.returnStudentAllDiscuss()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    getPostList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetPostList/',
        method: 'get',
        params: {
          postThemeId: that.postTheme.id
        }
      }).then(function (response) {
        console.log(response.data)
        that.postList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    buildPost: function () {
      this.dialogFormVisible = false
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'BuildPost/',
        method: 'get',
        params: {
          postThemeId: that.postTheme.id,
          userName: that.userName,
          content: that.input.content,
          time: that.time,
          isTeacher: 0
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('跟贴成功')
          that.getPostList()
          that.input.content = ''
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    deletePost: function (postId) {
      this.$confirm('此操作将永久删除该跟贴，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeletePost/',
          method: 'get',
          params: {
            postId: postId
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.getPostList()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    returnStudentAllDiscuss: function () {
      let that = this
      that.$router.push({
        name: 'StudentAllDiscuss'
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
