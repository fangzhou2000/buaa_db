<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userName}}  管理学习材料</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-table :data="myMaterialList">
          <el-table-column label="学习材料ID" prop="id"></el-table-column>
          <el-table-column label="学习材料名称" prop="name"></el-table-column>
          <el-table-column label="删除">
            <template slot-scope="scope">
              <el-button v-on:click="deleteMaterial(scope.$index)" type="danger" size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'

export default {
  name: 'ManageMaterial',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
      myMaterialList: [{
        id: '1',
        name: '前端测试学习材料'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.getTeacherMaterialList()
  },
  methods: {
    getTeacherMaterialList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetTeacherMaterialList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.myMaterialList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    deleteMaterial: function (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'DeleteMaterial/',
        method: 'get',
        params: {
          userName: that.userName,
          id: that.myMaterialList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          alert('删除成功')
        } else {
          alert('!')
        }
        that.getTeacherMaterialList()
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
