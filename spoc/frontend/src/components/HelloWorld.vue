<template>
  <div class="welcome">
      <div class="navigator">
        <div class="navigator-left">
          <i class="el-icon-bell"></i>
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
  <!--        <div class="block1">-->
            <el-col span="4" offset="3">
              <el-card>
                <img :src="cardImg_group.src" alt="">
                <p>{{cardImg_group.title}}</p>
              </el-card>
            </el-col>
  <!--        <span>-->
  <!--          <i class="el-icon-edit"></i>-->
  <!--        </span>-->
  <!--        <span class="content1">三招搞定数学分析</span>-->
  <!--          <p class="line-1-text"><span>优质课程推荐</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">立即查看</a></span></p>-->
  <!--          <p class="line-1-text"><span>学习资料获取</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">抢先获得</a></span></p>-->
  <!--          <p class="line-1-text"><span>加入兴趣小组</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">点击加入</a></span></p>-->
  <!--      </div>-->
  <!--        <div class="block2">-->
            <el-col span="4" offset="3">
              <el-card>
                <img :src="cardImg_book.src" alt="">
                <p>{{cardImg_book.title}}</p>
              </el-card>
            </el-col>
  <!--        <span>-->
  <!--          <i class="el-icon-question"></i>-->
  <!--        </span>-->
  <!--        <span>&nbsp;&nbsp;</span>-->
  <!--        <span class="content2">课程查询指导</span>-->
  <!--          <p class="line-1-text">课程信息</p>-->
  <!--          <p class="line-1-text">使用指南</p>-->
  <!--          <p class="line-1-text">未完待续...</p>-->
  <!--      </div>-->
  <!--        <div class="block3">-->
            <el-col span="4" offset="3">
              <el-card>
                <img :src="cardImg_join.src" alt="">
                <p>{{cardImg_join.title}}</p>
              </el-card>
            </el-col>
  <!--        <span>-->
  <!--          <i class="el-icon-search"></i>-->
  <!--        </span>-->
  <!--        <span class="content3">成绩综合分析</span>-->
  <!--          <p class="line-1-text">查询成绩</p>-->
  <!--          <p class="line-1-text">未完待续...</p>-->
          </el-row>
        </div>
      </div>
      <div class="line_2">
        <div class="line-2-head"><span class="div-head">关于我们</span></div>
<!--        <div class="line-2-content">-->
<!--          <div class="line-2-admin">-->
<!--            <div class="left-photo">-->
<!--              <div class="imgs">-->
<!--              <img src="../assets/img/G.jpg" alt="fangzhou"/>-->
<!--            </div>-->
<!--              <div class="imgs">-->
<!--              <img src="../assets/img/O.jpg" alt="Mike-smith-rem"/>-->
<!--            </div>-->
<!--              <div class="imgs">-->
<!--              <img src="../assets/img/T.jpg" alt="mingx"/>-->
<!--            </div>-->
<!--            </div>-->
<!--            <div class="right-photo">-->
<!--              <div class="school1">-->
<!--               <img src="../assets/img/北航logo.png" alt="buaa"/>-->
<!--              </div>-->
<!--              <div class="school2">-->
<!--               <img src="../assets/img/北航计算机学院logo.png" alt="buaa-cs"/>-->
<!--            </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="line-2-intro">-->
<!--            <div id="first_row">-->
<!--              <ol>-->
<!--                <li>这是一个怎样的网站</li>-->
<!--                <ul>-->
<!--                  <li>这是一个用于检验学习成果的小项目，主要使用语言包括<strong>JS、VUE（前端），Python（后端）</strong>，同时利用<strong>Django</strong>框架进行交互</li>-->
<!--                  <li>这个网站提供后台数据库进行支持。其中利用<Strong>MySQL进行数据的操作和保存</Strong></li>-->
<!--                  <li>这个网站是开源的，您可以在github中找到源文件</li>-->
<!--                  <li>未完待续...</li>-->
<!--                </ul>-->
<!--                <li>您能在这里看到什么</li>-->
<!--                <ul>-->
<!--                  <li>学生互动平台和教师平台——在小组中展现特色</li>-->
<!--                  <li>多样的课程——多样的评价——多样的学习资料</li>-->
<!--                  <li>未完待续...</li>-->
<!--                  </ul>-->
<!--                <li>您需要如何操作</li>-->
<!--                <ul>-->
<!--                  <li>只需要点击对应的按钮，就能完成你需要的操作</li>-->
<!--                  <li>未完待续....</li>-->
<!--                </ul>-->
<!--              </ol>-->
<!--        </div>-->
<!--          </div>-->
<!--        </div>-->
        <div>

        </div>
    </div>
      <div class="copyright">
      <div class="copyright-logo">
        <font-awesome-icon class="graduation_cap" icon="graduation-cap"/>
        <span class="head">Spoc</span>
        <p class="end-read">壹课，发现课程之美</p>
      </div>
      <div class="copyright-author">
        <p class="t-head">关于我们</p>
        <ul class="author-name">
          <li>Vue设计&nbsp;&nbsp;</li>
          <li>Vue服务器链接&nbsp;&nbsp;</li>
          <li>后端框架&nbsp;&nbsp;</li>
        </ul>
      </div>
      <div class="copyright-resource">
        <p class="t-head">开源地址</p>
        <a href="https://github.com/fangzhou0216/buaa_db" class="links">@方舟</a>
      </div>
      <div class="relate-link">
        <p class="t-head">友情链接</p>
        <a href="https://www.icourse163.org/" class="links">中国大学MOOC</a>
      </div>
    </div>
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
    height: 450px;
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
  .line-2-content{
    width: 100%;
    height: 500px;
    overflow: hidden;
    float: left;
  }
  .line-2-admin{
    float: left;
    height: 320px;
    width: 40%;
    overflow: hidden;
    border-radius: 20px 20px 20px 20px;
    background: linear-gradient(2deg, deepskyblue 1%, cornflowerblue 20%);
    border:  1px solid white;
    opacity: 0.8;
    margin-top: 5%;
    margin-left: 5%;
    margin-bottom: 10%;
  }
  .left-photo{
    float: left;
    height: inherit;
    width: 30%;
    overflow: hidden;
  }
  .imgs img{
    margin-top: 12px;
    margin-left: 15px;
    float: top;
    width: 80px;
    height: 80px;
    border-radius: 40px;
    border-width: 3px;
    border-style: solid;
    border-color: yellowgreen;
  }
  .right-photo{
    float: left;
    width: 70%;
  }
  .school1 img{
    margin-top: 15%;
    width: 70%;
  }
  .school2 img{
    margin-top: 15%;
    width: 90%;
  }
  .line-2-intro{
    height: 450px;
    width: 35%;
    float: left;
    margin-left: 10%;
    margin-top: 2%;
    background-color: honeydew;
    overflow: hidden;
    border-radius: 10%;
    border-style: dotted;
    border-color: lightblue;
    border-width: 2px;
  }
  #first_row{
    margin-left: 5%;
    margin-right: 5%;
  }
  .line-1-text{
    margin-left: 20%;
    margin-top: 10%;
    font-size: 16px;
    font-family: Arial,serif;
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
    padding-left: 20%;
    font-size: 12px;
  }
  .links{
    font-size: 12px;
  }
  .line_2{
    margin-top: 50px;
    height: 600px;
    width: inherit;
    margin-left: 50px;
    margin-right: 50px;
  }
  .div-head{
    float: left;
    margin-left: 30px;
    margin-top: 10px;
  }
  .content1, .content2, .content3{
    font-size: 20px;
  }
</style>
