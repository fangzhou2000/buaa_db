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
          <el-table :data="materialList">
            <el-table-column label="学习材料ID" prop="id"></el-table-column>
            <el-table-column label="学习材料名称" prop="name"></el-table-column>
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
      materialList: [{
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }, {
        id: '2',
        name: '前端测试课程材料'
      }]
    }
  },
  mounted () {
    this.getMaterialList()
  },
  methods: {
    getMaterialList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetMaterialList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.materialList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
