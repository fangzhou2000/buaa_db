<template>
  <div class="welcome">
      <div class="navigator">
        <div class="navigator-left">
          <i class="el-icon-house"></i>
          &nbsp;&nbsp;&nbsp;Spoc
        </div>
        <div class="navigator-right">
          <el-button class="buttons" @click="goToStudentLogin">学生登录</el-button>
          <span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;</span>
          <el-button class="buttons" @click="goToTeacherLogin">教师登录</el-button>
        </div>
    </div>
      <div class="introduction">
        <el-carousel height="720px">
          <el-carousel-item v-for="(item, index) in headImg" :key="index">
            <img :src="item.src" style="width: 100%; height: 100%;" alt="">
            <div class="cover">
              {{item.title}}<br>
              <span style="font-size: 25px">{{item.subTitle}}</span>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="line_1">
        <div class="line-1-head"><span class="div-head">其他推荐</span></div>
        <br><br>
        <div class="line-1-content">
          <el-row>
            <el-col span="5" offset="2">
              <el-card>
                <img :src="cardImg_group.src" alt="" style="display: block; width: 100%">
                <p>{{cardImg_group.title}}</p>
              </el-card>
            </el-col>
            <el-col span="5" offset="2">
              <el-card>
                <img :src="cardImg_book.src" alt="" style="display: block; width: 100%;">
                <p>{{cardImg_book.title}}</p>
              </el-card>
            </el-col>
            <el-col span="5" offset="2">
              <el-card>
                <img :src="cardImg_join.src" alt="" style="display: block; width: 100%">
                <p>{{cardImg_join.title}}</p>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
      <div class="line_2">
        <div class="line-2-head"><span class="div-head">关于我们</span></div>
        <div>

        </div>
      </div>
      <el-row class="copyright">
        <el-col class="copyright-logo" span="6">
          <i class="el-icon-house"></i>
          <span class="head">Spoc</span>
          <p class="end-read">壹课，发现课程之美</p>
        </el-col>
        <el-col class="copyright-author" span="6">
          <p class="t-head">关于我们</p>
          <ul class="author-name">
            <li>Vue设计&nbsp;&nbsp;</li>
            <li>Vue服务器链接&nbsp;&nbsp;</li>
            <li>后端框架&nbsp;&nbsp;</li>
          </ul>
        </el-col>
        <el-col class="copyright-resource" span="6">
          <p class="t-head">开源地址</p>
          <a href="https://github.com/fangzhou0216/buaa_db" class="links">@方舟</a>
        </el-col>
        <el-col class="relate-link" span="6">
          <p class="t-head">友情链接</p>
          <a href="https://www.icourse163.org/" class="links">中国大学MOOC</a>
        </el-col>
    </el-row>
  </div>
</template>

<script>
import technology from '../assets/img/technology.jpg'
import book from '../assets/img/book.jpg'
import Computer from '../assets/img/Computer.jpg'
import cardBook from '../assets/img/300-240-book.png'
import cardJoin from '../assets/img/300-240-add.jpg'
import cardGroup from '../assets/img/300-240-group.jpg'

export default {
  data: function () {
    return {
      headImg: [
        {
          'title': '数据集成平台',
          'subTitle': 'Data Integration Platform',
          'src': technology
        },
        {
          'title': '更好的学习体验',
          'subTitle': 'Better Study Experience',
          'src': book
        },
        {
          'title': '合作与共享',
          'subTitle': 'Corporation and Sharing',
          'src': Computer
        }
      ],
      cardImg_group: {
        'id': 'group',
        'title': '小组生活',
        'src': cardGroup
      },
      cardImg_join: {
        'id': 'join',
        'title': '加入我们',
        'src': cardJoin
      },
      cardImg_book: {
        'id': 'book',
        'title': '资料查询',
        'src': cardBook
      }
    }
  },
  methods: {
    goToStudentLogin () {
      this.$router.push({
        name: 'StudentLogin'
      })
    },
    goToTeacherLogin () {
      this.$router.push({
        name: 'TeacherLogin'
      })
    }
  }
}
</script>

<style scoped>
  .navigator{
    height: 80px;
    width: 100%;
    background-color: whitesmoke;
  }
  .navigator-left{
    font-size: 40px;
    display: inline-flex;
    font-family: '华文仿宋', serif;
    float: left;
    margin-left: 5%;
    margin-top: 1%;
  }
  .navigator-right{
    align-self: center;
    display: inline-flex;
    float: right;
    margin-right: 5%;
    margin-top: 1%;
  }
  .buttons{
    display: inline-flex;
  }
  .introduction{
    margin-top: 20px;
    margin-left: 100px;
    margin-right: 100px;
    padding: 0;
    height: 720px;
    border: lightblue 1px hidden;
    background-color: ghostwhite;
    overflow: hidden;
  }
  .cover{
    position:absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.6);
    z-index: 100;
    text-align: center;
    top:0;
    color: white;
    font-size: 40px;
    line-height: 50px;
    margin-right: 20px;
    padding-top: 300px;
}
  .line_1, .line_2{
    margin-top: 50px;
    height: 600px;
    width: inherit;
    margin-left: 50px;
    margin-right: 50px;
  }
  .line-1-head, .line-2-head{
    width: inherit;
    height: 50px;
    font-size: 20px;
    font-family: "微软雅黑", serif;
    background-color: white;
    border-left: orange 10px solid;
  }
  .div-head{
    float: left;
    margin-left: 30px;
    margin-top: 10px;
  }
  .copyright{
    margin: 20px;
    padding: 0;
    height: 200px;
    border: lightblue 1px hidden;
    background-color: dimgray;
    color: white;
  }
  .copyright-logo, .copyright-author, .copyright-resource, .relate-link{
    padding-top: 1%;
    width: 24%;
    float: left;
    padding-left: 1%;
  }
  .author-name{
    list-style-type: none;
    text-align: left;
    font-size: 12px;
  }
  .links{
    font-size: 12px;
  }
</style>
