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
          <el-table :data="courseList">
            <el-table-column label="课程ID" prop="id"></el-table-column>
            <el-table-column label="课程名称" prop="name"></el-table-column>
            <el-table-column label="课程材料ID" prop="materialIdString"></el-table-column>
            <el-table-column label="课程材料" prop="materialNameString"></el-table-column>
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
  name: 'CourseTable',
  components: {AdminHeading, AdminNav},
  data: function () {
    return {
      courseList: [{
        id: '1',
        name: '前端测试课程',
        materialIdString: [{
          id: '1',
          name: 'book1'
        }],
        materialNameString: 'book1,book2'
      }, {
        id: '2',
        name: '前端测试课程',
        materialIdString: '12',
        materialNameString: 'book1'
      }, {
        id: '3',
        name: '前端测试课程',
        materialIdString: '13',
        materialNameString: 'book1'
      }, {
        id: '4',
        name: '前端测试课程',
        materialIdString: '14',
        materialNameString: 'book1'
      }]
    }
  },
  mounted () {
    this.getCourseList()
  },
  methods: {
    getCourseList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCourseList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.courseList = response.data
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
