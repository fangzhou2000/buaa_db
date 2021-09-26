<template>
  <div class="login">
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
    <div class="login_block">
      <div id="login_head">
         <p>账号密码登录</p>
      </div>
      <div id="login_name">
        <p>
          <input id="name" type="text" placeholder="请输入用户名" v-model="userName">
        </p>
      </div>
      <div id="login_password">
        <p>
          <input id="password" type="text" placeholder="请输入密码" v-model="userPassWord">
        </p>
      </div>
      <div id="login_button"><button id="button_in" v-on:click="login"><div id="button_in_name">登录</div></button></div>
      <div id="register_button"><button id="button_re" v-on:click="goToRegister"><div id="button_re_name">注册</div></button></div>
    </div>
  </div>

</template>

<script>
export default {
  methods: {
    goToRegister () {
      this.$router.push('/Register')
    }
  }
}
</script>

<style scoped>
body, .login{
    background-color: aqua;
    background-image: linear-gradient(0deg, #485461 0%, #28313b 50%);
    height: 100vh;
    font-family: 'Roboto Mono', monospace;
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
  .login_block{
    background-color: cadetblue;
    position: relative;
    margin-top: 100px;
    margin-left: 700px;
    width: 500px;
    height: 400px;
    border-radius: 20px;
    border-color: darkcyan;
    border-style: inset;
    opacity: 0.2;
  }
  #login_head{
    text-align: left;
    margin-left: 50px;
    margin-top: 50px;
    font-family: "微软雅黑", serif;
    color: greenyellow;
    font-size: 30px;
  }
  #password, #name{
    alignment: left;
    width: 360px;
    height: 30px;
    border: none;
  }
  #login_button, #register_button{
    margin-top: 10px;
  }
  #button_in, #button_re{
    background-color: darkcyan;
    width: 360px;
    height: 50px;
    font-family: "微软雅黑", serif;
    font-size: 25px;
    border-radius: 5px;
    border: none darkcyan;
  }
  #button_in_name, #button_re_name{
    color: lightblue;
  }
</style>
