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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-row>
            <el-col :span="14" class="left-information" style="width: 50%">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找相关帖子"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 5%"></el-input>
                </el-col>
                <el-col :span="2">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: right"
                    @click="searchDiscuss(inputSearch)"
                    circle></el-button>
                </el-col>
              </el-row>
              <el-card v-for="(postTheme, index) in showPostThemeList" :key="index" shadow="hover" style="margin-bottom: 2%">
                <div class="clearfix">
                  <span><strong>{{postTheme.title}}</strong></span>
                  <el-button style="float: right; padding: 3px 0" type="text"
                             v-on:click="enterPostTheme(index)">进入帖子</el-button>
                </div>
                <div class="textitem" style="font-size: 10px; margin-top: 2%; margin-bottom: 2%">
                  <el-tag size="mini">
                  <span v-if="postTheme.isTeacher === 0">学生</span>
                  <span v-else-if="postTheme.isTeacher === 1">教师</span>
                  <span v-else-if="postTheme.isTeacher === 2">管理员</span>
                  </el-tag>
                </div>
                <div>
                  <span style="color: gray; font-size: 8px">发表于-{{postTheme.time}}</span>
                </div>
              </el-card>
            </el-col>
            <el-col :span="8" :offset="2" class="right-information">
              <el-card shadow="hover" style="width: 100%">
                <el-row>
                  <el-col :span="12">
                    <el-empty :image-size="80" style="margin: 0 !important; padding: 0 !important;"></el-empty>
                  </el-col>
                  <el-col :span="12">
                    <el-descriptions :column="1">
                      <el-descriptions-item label="用户名">{{userNickName}}</el-descriptions-item>
                      <el-descriptions-item label="学号">{{userName}}</el-descriptions-item>
                      <el-descriptions-item label="已发帖子">{{discussNum}}</el-descriptions-item>
                    </el-descriptions>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider></el-divider>
                </el-row>
                <el-row>
                  <el-button @click="buildThemeVisible = true" style="width: 100%" type="primary">新建主题贴</el-button>
                  <el-dialog title="新建主题帖" :visible.sync = "buildThemeVisible" width="70%">
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input v-model="input.title" placeholder="请输入标题"></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
<!--                        <el-input v-model="input.content" placeholder="请输入贴子的主题" type="textarea" :rows="10"></el-input>-->
                        <quill-editor ref="text" v-model="input.content" style="height: 400px"></quill-editor>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer">
                      <el-button @click="buildThemeVisible = false">取消</el-button>
                      <el-button type="primary" @click="buildPostTheme">确定</el-button>
                    </div>
                  </el-dialog>
                </el-row>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import StudentNav from '../StudentNav'
import StudentHeading from '../StudentHeading'
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  name: 'StudentAllDiscuss',
  components: {StudentNav, StudentHeading, quillEditor},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      discussNum: '1',
      input: {
        title: '',
        content: ''
      },
      inputSearch: '',
      postThemeList: [{
        id: '1',
        userName: 'admin',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx',
        isTeacher: 1
      },
      {
        id: '2',
        userName: '学号1',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx',
        isTeacher: 0
      }],
      showPostThemeList: [
        {
          id: '1',
          userName: 'admin',
          userNickName: '学生1',
          title: '前端测试贴标题',
          content: '前端测试贴内容',
          time: 'xxxx',
          isTeacher: 1
        },
        {
          id: '2',
          userName: '学号1',
          userNickName: '学生1',
          title: '前端测试贴标题',
          content: '前端测试贴内容',
          time: 'xxxx',
          isTeacher: 0
        }
      ],
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
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetPostThemeList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.postThemeList = response.data
        that.showPostThemeList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
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
          title: that.input.title,
          content: that.input.content,
          time: that.time,
          isTeacher: 0
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
          newPostTheme: {
            id: that.showPostThemeList[index].id,
            userName: that.showPostThemeList[index].userName,
            userNickName: that.showPostThemeList[index].userNickName,
            title: that.showPostThemeList[index].title,
            content: that.showPostThemeList[index].content,
            time: that.showPostThemeList[index].time,
            isTeacher: that.showPostThemeList[index].isTeacher
          }
        }
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    searchDiscuss: function (inputSearch) {
      this.showPostThemeList = this.searchByIndexOf(inputSearch, this.postThemeList)
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
        if (list[i].title.indexOf(keyWord) >= 0) {
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
