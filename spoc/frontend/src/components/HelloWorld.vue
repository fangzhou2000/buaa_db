<template lang="html">
  <div class="main">
    <br>
    <div class="first_block">
      <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
      <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Ephesis&display=swap" rel="stylesheet">
              <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
      <div class="i_block">
        <div class="i_block_welcome">课程中心 试行版</div>
      </div>
      <div class="i_block_introduction">这里是由BUAAer打造的<strong>简易课程系统</strong>，我们期待您的光临和加入！</div>
    </div>
    <div class="left_photo">
      <img src="../assets/logo.png" alt="logo" id="logo">
    </div>
    <div class="right_block">
      <div class="right_block_head">
        <p id="right_block_head_text">索引</p>
      </div>
      <div class="right_block_content">
        <div id="first_row">
          <ol>
            <li>这是一个怎样的网站</li>
            <ul>
              <li>这是一个用于检验学习成果的小项目，主要使用语言包括<strong>JS、VUE（前端），Python（后端）</strong>，同时利用<strong>Django</strong>框架进行交互</li>
              <li>这个网站提供后台数据库进行支持。其中利用<Strong>MySQL进行数据的操作和保存</Strong></li>
              <li>这个网站是开源的，您可以在github中找到源文件</li>
              <li>网站尚不成熟，开发人员也正在学习中。如果遇到各种问题或者有什么建议，请在github中联系我们</li>
            </ul>
            <li>您能在这里看到什么</li>
            <ul>
              <li></li>
              </ul>
            <li>您需要如何操作</li>
            <ul>
              <li></li>
            </ul>
          </ol>
        </div>
      </div>
    </div>
    <br>
    <div class="last_button">
    <button id="login_button" @click="goToLogin">Enter</button>
      </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToLogin () {
      this.$router.push('Login')
    }
  }
}
</script>

<style scoped>
  body, .main{
    background-color: aqua;
    background-image: linear-gradient(0deg, #485461 0%, #28313b 50%);
    height: 100vh;
    font-family: 'Roboto Mono', monospace;
  }
  ul{
    font-size: 20px;
    text-align: left;
    list-style: linear-gradient(30deg, darkgrey 10%, darkcyan 50%, darkslategrey 40%);
    line-height: 30px;
  }
  ol {
    font-size: 30px;
    text-align: left;
    line-height: 50px;
    color: yellowgreen;
  }
  .first_block{
    background-color: deepskyblue;
    height: 100px;
    margin:0 0;
    border-top:2px dashed #000;
    border-bottom:2px solid #000;
    border-left:1px dashed #000;
    border-right:1px solid #000;
    border-image: linear-gradient(0deg, #485461 0%, #28313b 50%, #2c3e50 50%);
    opacity: 0.4;
  }
  .i_block{
    background-color: darkslategrey;
    position: relative;
    padding: 2px 20px 2px 20px;
    margin: 2px 150px 2px 150px;
    border: 1px  dot-dot-dash turquoise;
    border-radius: 20px;
  }
  .i_block_welcome{
    color: yellowgreen;
    font-size: 35px;
    font-family: 'ZCOOL KuaiLe',serif ;
    margin: 5px 15px 5px 15px;
    text-decoration: underline;
    text-shadow: 3px 3px 1px black;
  }
  .i_block_introduction{
    color: black;
    font-family: '华文仿宋',serif;
    font-size: 20px;
    margin-top: 10px;
  }
  #logo{
    position: absolute;
    left: 200px;
    top: 300px;
    width: 300px;
    height: auto;
    size: 300px;
    -webkit-box-reflect: below 0 -webkit-gradient(linear, left top, left bottom, from(transparent), color-stop(70%, transparent) , to(rgba(250, 250, 250, 0.1)))
  }
  .right_block{
    background-color: gray;
    opacity: 0.4;
    border-radius: 30px;
    position: absolute;
    left: 900px;
    top: 200px;
    width: 900px;
    height: 700px;
  }
  .right_block_head{
    background-color: lightblue;
    position: relative;
    margin: 50px;
    width: auto;
    height: 100px;
    border: 1px dot-dash #485461;
    border-radius: 30px 0 0 30px;
  }
  #right_block_head_text{
    padding-left: 10px;
    padding-top: 25px;
    font-family: 'ZCOOL Xiaowei',serif;
    font-size: 40px;
    text-align: left;
  }
  .right_block_content{
    background-color: #485461;
    border-radius: 20px;
    width: auto;
    height: 450px;
    opacity: 0.4;
    margin: 40px;
  }
  #first_row{
    margin-left: 20px;
    margin-right: 20px;
  }
  .last_button{
    position: absolute;
    margin:225px;
    padding-top: 400px;
  }
  #login_button{
    height: 100px;
    width: 250px;
    background-color: darkcyan;
    border-radius: 10px;
    border: none;
    font-size: 40px;
    cursor: pointer;
  }
  button:hover{
    float: left;
  }
  *:focus {outline: none;}
</style>
