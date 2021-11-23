<template>
  <div>
    <el-container class='background'>
      <el-aside class='aside' width="'show?'64px':'250px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class='main'>
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main>

        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminNav from './AdminNav'
import AdminHeading from './AdminHeading'
export default {
  name: 'AdminHead',
  components: {AdminHeading, AdminNav}
}
</script>

<style scoped>
  @import '../../assets/css/back.css';
  @import '../../assets/css/nav.css';
</style>
