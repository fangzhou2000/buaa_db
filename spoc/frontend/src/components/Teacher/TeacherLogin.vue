<template>
  <div class="TeacherRegister">
    <br>
    <div class="first_block">
      <p class="head">Spoc</p>
    </div>
    <div class="register_block">
      <div class="register_head">
        <p>教师登录</p>
      </div>
      <el-form>
        <div id="register-name">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入工号" v-model="userName"></el-input>
          </el-form-item>
        </div>
        <div id="register-password">
          <el-form-item>
            <el-input class="inputs" type="text" placeholder="请输入密码" v-model="userPassWord" show-password></el-input>
          </el-form-item>
        </div>
        <div class="confirm-button">
            <el-button id="button_in" type="primary" size="small" v-on:click="goToTeacherHead">
              确认
            </el-button>
        </div>
        <div class="return-button">
            <el-button id="button_re" type="primary" plain="true" size="small" v-on:click="goToTeacherRegister">
              注册
            </el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'TeacherLogin',
  data: function () {
    return {
      userName: '',
      userPassWord: '',
      status: -1
    }
  },
  methods: {
    goToTeacherHead: function () {
      let that = this
      /*if (that.userName === 'admin' && that.userPassWord === '123456') {
        that.$router.push({
            name: 'TeacherHead',
            params: {
              userName: that.userName
            }
          })
        console.log('from:' + that.userName)
      } else {
        alert('!')
      }*/
      this.$http.request({
        url: that.$url + 'TeacherLogin/',
        method: 'get',
        params: {
          userName: that.userName,
          userPassWord: that.userPassWord
        }
      }).then(function (response) {
        console.log(response)
        that.status = response.data
        if (that.status === 0) {
          that.$router.push({
            name: 'TeacherHead',
            params: {
              userName: that.userName
            }
          })
        } else if (that.status === 1) {
          alert('工号不存在')
        } else if (that.status === 2) {
          alert('密码错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    goToTeacherRegister: function () {
      this.$router.push({
        name: 'TeacherRegister'
      })
    }
  }
}
</script>

<style scoped>
  body,
  .TeacherRegister{
    background-color: white;
    background-image: linear-gradient(0deg, #f8f1ea 0%, #ffffff 30%);
    height: 100vh;
    font-family: 'Roboto Mono', monospace;
  }
  .first_block{
    height: 45px;
    border: 3px hidden;
    background-color: whitesmoke;
    text-align: center;
    padding-top: 0;
    padding-bottom: 0;
    margin-bottom: 20px;
  }
  .head{
    text-align: center;
    margin-top: 1px;
    font-size: 30px;
    font-family: '华文仿宋', serif;
  }
  .register_block{
    background-color: rgba(255, 255, 255, 0.15);
    position: center;
    margin-top: 50px;
    margin-left: 40%;
    width: 20%;
    height: 380px;
    border-color: #a8a8a8;
    border-style: solid;
    border-width: 1px;
    border-radius: 20px;
    opacity: 0.8;
  }
  .register_head{
    text-align: center;
    margin-top: 10%;
    font-family: "微软雅黑", serif;
    color: black;
    font-size: 30px;
  }
  #register-name, #register-password, #confirm-password{
    padding-left: 10%;
  }
  .confirm-button{
    margin-top: 25px;
    padding-left: 10%;
  }
  .return-button{
    margin-top: 15px;
    padding-left: 10%;
  }
  .inputs{
    width: 90%;
    height: 20px;
    border: none;
  }
  #button_in, #button_re{
    width: 90%;
  }

</style>
