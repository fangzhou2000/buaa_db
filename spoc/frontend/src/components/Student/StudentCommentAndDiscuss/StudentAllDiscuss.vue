<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <StudentNav></StudentNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <StudentHeading></StudentHeading>
        </el-header>
        <el-main>
          <el-button @click="buildThemeVisible = true">新建主题贴</el-button>
          <el-dialog title="新建主题帖" :visible.sync = "buildThemeVisible">
            <el-row style="margin-bottom: 10px">
              <el-col>
                <el-input v-model="input.title" placeholder="请输入标题"></el-input>
              </el-col>
            </el-row>
            <el-row style="margin-bottom: 10px">
              <el-col>
                <el-input v-model="input.content" placeholder="请输入贴子的主题" type="textarea" :rows="10"></el-input>
              </el-col>
            </el-row>
            <div slot="footer" class="dialog-footer">
              <el-button @click="buildThemeVisible = false">取消</el-button>
              <el-button type="primary" @click="buildPostTheme">确定</el-button>
            </div>
          </el-dialog>
          <el-table :data="postThemeList">
            <el-table-column label="主题贴ID" prop="id"></el-table-column>
            <el-table-column label="主题贴标题" prop="title"></el-table-column>
            <el-table-column label="进入贴子"> <template slot-scope="scope">
          <el-button v-on:click="enterPostTheme(scope.$index)" type="primary" size="small">进入</el-button>
        </template></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
export default {
  name: 'StudentAllDiscuss',
  components: {StudentNav, StudentHeading},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      input: {
        title: '',
        content: ''
      },
      postThemeList: [{
        id: '1',
        userName: 'admin',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx'
      }, {
        id: '2',
        userName: '学号1',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx'
      }],
      buildThemeVisible: false,
      time: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getPostThemeList()
  },
  methods: {
    getPostThemeList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetPostThemeList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.postThemeList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    getTime: function () {
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      this.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    buildPostTheme: function () {
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'BuildPostTheme/',
        method: 'get',
        params: {
          userName: that.userName,
          userNickName: that.userNickName,
          title: that.input.title,
          content: that.input.content,
          time: that.time
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('创建成功')
          that.buildThemeVisible = false
          that.getPostThemeList()
          that.postThemeInput = {
            title: '',
            content: ''
          }
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    enterPostTheme: function (index) {
      let that = this
      this.$router.push({
        name: 'StudentDiscuss',
        query: {
          postTheme: {
            id: that.postThemeList[index].id,
            userName: that.postThemeList[index].userName,
            userNickName: that.postThemeList[index].userNickName,
            title: that.postThemeList[index].title,
            content: that.postThemeList[index].content,
            time: that.postThemeList[index].time
          }
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
