<template>
  <div class="welcome">
      <div class="navigator">
        <span class="head">Spoc</span>
        <span class="reference">课程</span>
        <span class="reference">学校</span>
        <span class="reference">云端</span>
        <span class="reference">更多</span>
        <div class="buttons"><button class="buttons" @click="goToStudentLogin">学生登录</button></div>
          <span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;</span>
        <div class="buttons"><button class="buttons" @click="goToTeacherLogin">教师登录</button></div>
    </div>
      <div class="introduction">
        <div class="class-center">
        <p class="class-center-name">热门课程</p>
        <ul class="class-center-id">
          <li>工科数学分析&nbsp;<span class="sub">数学/6学分</span></li>
          <li>C语言程序设计&nbsp;<span class="sub">计算机基础/3学分</span></li>
          <li>Python程序设计&nbsp;<span class="sub">计算机基础/2学分</span></li>
          <li>C++:从入门到入土&nbsp;<span class="sub">选修课/1学分</span></li>
          <li>Spring架构分析&nbsp;<span class="sub">选修课/2学分</span></li>
          <li>编译原理&nbsp;<span class="sub">计算机核心/4学分</span></li>
          <li>数据库原理&nbsp;<span class="sub">计算机核心/4学分</span></li>
        </ul>
        </div>
        <div class="blink-block"></div>
        <div class="picture">
          <img class="imgt" src="../assets/learning-hard.png" alt="photo">
        </div>
        <div class="blink-block"></div>
        <div class="news">
          <p class="class-center-name">更新新闻</p>
          <ul class="class-center-id">
            <li>页面二次设计<span class="sub">2021.10.6</span></li>
            <li>使用Element UI优化<span class="sub">2021.10.6</span></li>
          </ul>
        </div>
      </div>
      <div class="line_1">
        <div class="line-1-head"><span class="div-head">其他推荐</span></div>
        <div class="block1">
        <span>
          <i class="el-icon-edit"></i>
        </span>
        <span class="content1">三招搞定数学分析</span>
          <p class="line-1-text"><span>优质课程推荐</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">立即查看</a></span></p>
          <p class="line-1-text"><span>学习资料获取</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">抢先获得</a></span></p>
          <p class="line-1-text"><span>加入兴趣小组</span>&nbsp;&nbsp;<span class="line-1-link"><a href="">点击加入</a></span></p>
      </div>
        <div class="block2">
        <span>
          <i class="el-icon-question"></i>
        </span>
        <span>&nbsp;&nbsp;</span>
        <span class="content2">课程查询指导</span>
          <p class="line-1-text">课程信息</p>
          <p class="line-1-text">使用指南</p>
          <p class="line-1-text">未完待续...</p>
      </div>
        <div class="block3">
        <span>
          <i class="el-icon-search"></i>
        </span>
        <span class="content3">成绩综合分析</span>
          <p class="line-1-text">查询成绩</p>
          <p class="line-1-text">未完待续...</p>
      </div>
      </div>
      <div class="line_2">
        <div class="line-2-head"><span class="div-head">指导单位</span></div>
        <div class="line-2-content">
          <div class="line-2-admin">
            <div class="left-photo">
              <div class="imgs">
              <img src="../assets/G.jpg" alt="fangzhou"/>
            </div>
              <div class="imgs">
              <img src="../assets/O.jpg" alt="Mike-smith-rem"/>
            </div>
              <div class="imgs">
              <img src="../assets/T.jpg" alt="mingx"/>
            </div>
            </div>
            <div class="right-photo">
              <div class="school1">
               <img src="../assets/北航logo.png" alt="buaa"/>
              </div>
              <div class="school2">
               <img src="../assets/北航计算机学院logo.png" alt="buaa-cs"/>
            </div>
            </div>
          </div>
          <div class="line-2-intro">
            <div id="first_row">
              <ol>
                <li>这是一个怎样的网站</li>
                <ul>
                  <li>这是一个用于检验学习成果的小项目，主要使用语言包括<strong>JS、VUE（前端），Python（后端）</strong>，同时利用<strong>Django</strong>框架进行交互</li>
                  <li>这个网站提供后台数据库进行支持。其中利用<Strong>MySQL进行数据的操作和保存</Strong></li>
                  <li>这个网站是开源的，您可以在github中找到源文件</li>
                  <li>未完待续...</li>
                </ul>
                <li>您能在这里看到什么</li>
                <ul>
                  <li>学生互动平台和教师平台——在小组中展现特色</li>
                  <li>多样的课程——多样的评价——多样的学习资料</li>
                  <li>未完待续...</li>
                  </ul>
                <li>您需要如何操作</li>
                <ul>
                  <li>只需要点击对应的按钮，就能完成你需要的操作</li>
                  <li>未完待续....</li>
                </ul>
              </ol>
        </div>
          </div>
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
export default {
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
a{
    text-decoration: none;
    color: deepskyblue;
  }
  .welcome{
    margin: 0;
    padding: 0;
    height: auto;
    width: auto;
    background-color: white;
    background-image: linear-gradient(0deg, wheat 0%, white 50%);
  }
  .navigator{
    height: 60px;
    border: 3px hidden;
    background-color: whitesmoke;
    text-align: center;
    padding-top: 0;
    padding-bottom: 0;
    margin-bottom: 20px;
  }
  .graduation_cap{
    margin-top: 0.5%;
    font-size: 30px;
  }
  .head{
    margin-top: 30px;
    font-size: 30px;
    font-family: '华文仿宋', serif;
    margin-right: 60px;
  }
  .reference{
    margin-top: 10%;
    margin-right: 40px;
    font-size: 16px;
  }
  .reference :hover{
    background-color: green;
  }
  .buttons{
    border-radius: 10px;
    border-style: none;
    border-width: 0;
    box-shadow: none;
    background-color: yellowgreen;
    color: #ffffff;
    padding: 0;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    height: 50px;
    width: 80px;
    font-size: 16px;
  }
  .buttons :hover{
    text-decoration: underline;
    cursor: pointer;
  }
  .introduction{
    margin-top: 20px;
    margin-left: 100px;
    margin-right: 100px;
    padding: 0;
    height: 300px;
    border: lightblue 1px hidden;
    background-color: ghostwhite;
    overflow: hidden;
  }
  .class-center{
    float: left;
    height: 260px;
    width: 25%;
    padding: 10px;
    margin: 10px;
    border: 1px white solid;
    list-style-type: none;
    line-height: 24px;
    text-align: left;
    background-color: white;
    overflow: hidden;
  }
  .blink-block{
    width: 3%;
    height: 250px;
    float: left;
  }
  .class-center-name{
    font-family: "微软雅黑",serif;
    font-size: 20px;
    margin-left: 10px;
    padding-left: 10px;
  }
  .sub{
    font-family: "华文仿宋", serif;
    font-size: 18px;
    float: right;
  }
  .picture{
    margin: 10px;
    float: left;
    width: 35%;
  }
  .imgt{
    width: 100%;
  }
  .news{
    float: right;
    height: 260px;
    width: 25%;
    padding: 10px;
    margin: 10px;
    border: 1px white solid;
    list-style-type: none;
    line-height: 24px;
    text-align: left;
    background-color: white;
    overflow: hidden;
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
  ul{
    font-size: 12px;
    text-align: left;
    list-style: linear-gradient(30deg, darkgrey 10%, darkcyan 50%, darkslategrey 40%);
    line-height: 25px;
  }
  ol {
    font-size: 15px;
    text-align: left;
    line-height: 45px;
    list-style: none;
    color: black;
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
  .line_1{
    margin-top: 50px;
    height: 400px;
    width: inherit;
    margin-left: 50px;
    margin-right: 50px;
  }
  .line_2{
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
  .block1, .block2, .block3{
    float: left;
    margin-left: 10%;
    margin-top: 40px;
    margin-bottom: 40px;
    width: 20%;
    height: 70%;
    border: 1px whitesmoke solid;
    border-radius: 3px;
    background: linear-gradient(2deg, ghostwhite 1%, whitesmoke 20%);
  }
  .icons, .el-icon-search, .el-icon-question, .el-icon-edit{
    margin-top: 10px;
    margin-right: 10px;
    font-size: 40px;
    align-self: center;
  }
  .content1, .content2, .content3{
    font-size: 20px;
  }
</style>
