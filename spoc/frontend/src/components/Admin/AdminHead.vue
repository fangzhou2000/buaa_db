<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <AdminNav></AdminNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <AdminHeading></AdminHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
          <h1>FreeTalk课程平台</h1>
          <p>FreeTalk课程平台是一个基于Vue进行前端设计的平台，经历过多次更新。</p>
          <ul>
            <li>介绍</li>
            <li>项目地址</li>
          </ul>

          <h2>介绍</h2>
          <p>本次课程设计的FreeTalk课程平台是综合了选课系统、教材管理、课程评价和讨论，面向所有学生与老师的选课平台。</p>

          <h4>(1)综合需求</h4>
          <p>FreeTalk课程平台（FreeTalk1.0）初步实现了课程管理和评论区，通过对于以下单元进行操作完成您的需求：</p>
          <ul>
            <li>课程：根据您的需要进行选课</li>
            <li>资料：获取相应的学习资料</li>
            <li>留言：分享您的看法</li>
          </ul>

          <h4>(2)使用说明</h4>
          <p>左侧栏中进行如下操作：</p>
          <ul>
            <li>点击课程信息——进行选课退课</li>
            <li>点击留言板——进行讨论交流，查看您的课程</li>
            <li>点击课程管理——管理您的课程（教师端）</li>
          </ul>
          <h4>讨论区</h4>
          <p>在讨论区中进行问题交流，关注讨论区中的通知。您也可以向FreeTalk工作组进行反馈，我们会尽快解决您的问题。</p>

          <h2>项目地址</h2>
          <p>如果您的有更好的建议，欢迎通过以下方式联系我们：</p>
          <el-link href="https://github.com/fangzhou0216/buaa_db">fangzhou0216</el-link>
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
  // data() {
  //   return {
  //     html: FreeTalk
  //   }
  // }
}
</script>

<style scoped>
  @import '../../assets/css/back.css';
</style>
