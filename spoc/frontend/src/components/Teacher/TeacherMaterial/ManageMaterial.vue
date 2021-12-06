<template>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main>
        <el-table :data="myMaterialList" v-loading="loading" >
          <el-table-column label="学习材料ID" prop="id"></el-table-column>
          <el-table-column label="学习材料名称" prop="name"></el-table-column>
          <el-table-column label="删除">
            <template slot-scope="scope">
              <el-button v-on:click="deleteMaterial(scope.$index)"
                         type="danger"
                         size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
      </el-container>
    </el-container>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'ManageMaterial',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userNickName: '',
      userName: '',
      myMaterialList: [{
        id: '1',
        name: '前端测试学习材料'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getTeacherMaterialList()
  },
  methods: {
    getTeacherMaterialList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherMaterialList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.myMaterialList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    deleteMaterial: function (index) {
      this.$confirm('此操作将永久删除该学习材料，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        that.loading = true
        this.$http.request({
          url: that.$url + 'DeleteMaterial/',
          method: 'get',
          params: {
            userName: that.userName,
            id: that.myMaterialList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('删除成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getTeacherMaterialList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
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
 @import "../../../assets/css/nav.css";
 @import "../../../assets/css/back.css";
</style>
