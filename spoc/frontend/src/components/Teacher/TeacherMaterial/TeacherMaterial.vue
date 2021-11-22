<template>
  <router-view></router-view>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'TeacherMaterial',
  components: {TeacherNav, TeacherHeading}
}
</script>

<style scoped>
 @import "../../../assets/css/Nav.css";
 @import "../../../assets/css/head.css";
</style>
