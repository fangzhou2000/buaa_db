<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main>
          <el-table :data="materialList" v-loading="loading">
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
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
export default {
  name: 'MaterialTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      materialList: [{
        id: '1',
        name: '前端测试课程材料'
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getMaterialList()
  },
  methods: {
    getMaterialList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetMaterialList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.materialList = response.data
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
            id: that.materialList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('删除成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getMaterialList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
      })
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
