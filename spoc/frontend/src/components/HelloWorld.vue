<template>
  <transition name="head-login-register">
    <div class="welcome">
    <div class="navigator">
      <div class="navigator-left">
        <i class="el-icon-s-platform"><span class="el-icon-s-platform-text">&nbsp;&nbsp;Spoc</span></i>
      </div>
      <div class="navigator-right">
        <span><el-button class="buttons" @click="goToStudentLogin">学生登录</el-button></span>
        <el-divider direction="vertical"></el-divider>
        <span><el-button class="buttons" @click="goToTeacherLogin">教师登录</el-button></span>
      </div>
  </div>
    <div class="introduction">
      <el-carousel height="600px">
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
        <el-row class="this-el-row">
          <el-col :span="5" :offset="2" >
            <el-card >
              <img
                :src="cardImg_group.src"
                alt=""
                style="width: 100%; height: auto"/>
              <p>{{cardImg_group.title}}</p>
            </el-card>
          </el-col>
          <el-col :span="5" :offset="2" >
            <el-card >
              <img
                style="width: 100%; height: auto"
                :src="cardImg_book.src"
                alt=""/>
              <p>{{cardImg_book.title}}</p>
            </el-card>
          </el-col>
          <el-col :span="5" :offset="2" >
            <el-card >
              <img
                :src="cardImg_join.src"
                alt=""
                style="width: 100%; height: auto"/>
              <p>{{cardImg_join.title}}</p>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="line_2">
      <div class="line-2-head"><span class="div-head">仍在优化...</span></div>
      <div class="timeline">
        <el-row>
          <el-col :span="12">
            <el-timeline>
              <el-timeline-item timestamp="2021/9/15" placement="top">
                <el-card>
                  <p>Initial Commit</p>
                  <p>Submitted on 2021/9/15 17:00</p>
                </el-card>
              </el-timeline-item>
              <el-timeline-item timestamp="2021/10/9" placement="top">
                <el-card>
                  <p>HomeWork One Completed</p>
                  <p>Submitted on 2021/10/14 22:18</p>
                </el-card>
              </el-timeline-item>
              <el-timeline-item timestamp="2021/11/3" placement="top">
                <el-card>
                  <p>The Representation On DB Design</p>
                  <p>Submitted on 2021/11/3 16:16</p>
                </el-card>
              </el-timeline-item>
            </el-timeline>
          </el-col>
          <el-col :span="12">
            <el-timeline>
              <el-timeline-item timestamp="2021/11/23" placement="top">
                <el-card>
                  <p>The Second Check</p>
                  <p>Submitted on 2021/11/23 01:20</p>
                </el-card>
              </el-timeline-item>
              <el-timeline-item timestamp="2021/11/?" placement="top">
                <el-card>
                  <p>HomeWork Two Completed</p>
                  <p>Submitted on 2021/11/? ??:??</p>
                </el-card>
              </el-timeline-item>
              <el-timeline-item timestamp="202?/?/?" placement="top">
                <el-card>
                  <p>To be Continued...</p>
                  <p><span></span></p>
                </el-card>
              </el-timeline-item>
            </el-timeline>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="copyright">
      <div class="copyright-block">
        <div class="first-copyright-head">Platform</div>
        <div class="first-copyright-content">壹课，发现课程之美</div>
      </div>
      <div class="copyright-block">
        <div class="author-head">Developers</div>
        <div class="author-task">
          <span class="author-task">oyk---Vue设计</span>
        </div>
        <div class="author-task">
          <span class="author-task">tqj---Vue服务器链接</span>
        </div>
        <div class="author-task">
          <span class="author-task">gmm---后端框架</span>
        </div>
      </div>
      <div class="copyright-block">
        <div class="third-copyright-head">Relatives</div>
        <div class="third-copyright-link">
          <p><a href="https://github.com/fangzhou0216/buaa_db" class="links">@方舟</a></p>
          <p><a href="https://www.icourse163.org/" class="links">中国大学MOOC</a></p>
        </div>
        <div class="admin-enter-item">
          <p class="admin-enter-text" @click="goToAdminLogin">
            Be&nbsp;an&nbsp;Admin?
          </p>
        </div>
      </div>
    </div>
  </div>
  </transition>
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
        'title': '讨论交流',
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
      },
      fullscreenLoading: false
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
    },
    goToAdminLogin () {
      this.$router.push({
        name: 'AdminLogin'
      })
    }
  }
}
</script>

<style scoped>
  @import "../assets/css/HelloWorld/block1.css";
  @import "../assets/css/HelloWorld/block2.css";
  @import "../assets/css/HelloWorld/copyright.css";
  @import "../assets/css/HelloWorld/introduction.css";
  @import "../assets/css/HelloWorld/navigator.css";
  @import "../assets/css/Transition/head-login-register.css";
  .welcome {
    margin-left: 80px;
    margin-right: 80px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
  }
  .el-divider--horizontal {
    display: block;
    height: 1px;
    width: 100%;
    margin: 8px 0 !important;
}
  .in-helloworld-leave-active {
    transition: all 2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .in-helloworld-leave-to
  /* .slide-fade-leave-active for below version 2.1.8 */ {
    transform: translateX(10px);
    opacity: 0;
  }
  .in-helloworld-enter-active {
    transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }

</style>
