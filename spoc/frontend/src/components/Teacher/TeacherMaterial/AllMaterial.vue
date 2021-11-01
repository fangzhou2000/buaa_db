<template>
  <div class="background">
    <el-container class="header">
      <el-header>
        <span>{{userName}} 查看学习材料</span>
      </el-header>
    </el-container>

    <el-container class="main">
      <el-aside>
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-main>
        <el-table :data="materialList">
          <el-table-column label="学习材料ID" prop="id"></el-table-column>
          <el-table-column label="学习材料名称" prop="name"></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
export default {
  name: 'AllMaterial',
  components: {TeacherNav},
  data: function () {
    return {
      userName: '',
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
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
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
