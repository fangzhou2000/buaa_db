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
          <el-table :data="teacherList">
            <el-table-column label="教师工号" prop="id"></el-table-column>
            <el-table-column label="教师名称" prop="name"></el-table-column>
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
  name: 'TeacherTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      teacherList: [
        {
          id: 't19373686',
          name: '欧阳老师'
        },
        {
          id: 't19373135',
          name: '田老师'
        },
        {
          id: 't19373136',
          name: '郭老师'
        },
        {
          id: 't19373000',
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
