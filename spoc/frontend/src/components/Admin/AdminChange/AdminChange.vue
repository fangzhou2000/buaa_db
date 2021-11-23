<template>
  <div>
    <el-container class='background'>
      <el-aside class='aside' width="show?'64px':'300px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class='main'>
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main>
          暂未开放
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from '../AdminNav'
import AdminHeading from '../AdminHeading'
export default {
  name: 'AdminChange',
  components: {AdminNav, AdminHeading}
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
</style>
