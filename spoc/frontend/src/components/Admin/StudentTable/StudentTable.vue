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
          <el-table :data="studentList">
            <el-table-column label="学号" prop="id"></el-table-column>
            <el-table-column label="姓名" prop="name"></el-table-column>
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
  name: 'AdminTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      studentList: [
        {
          id: 19373686,
          name: '欧阳奎'
        },
        {
          id: 19373135,
          name: '田旗舰'
        },
        {
          id: 19373136,
          name: '郭明明'
        },
        {
          id: 19373000,
          name: null
        },
        {
          id: null,
          name: null
        }
      ]
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
