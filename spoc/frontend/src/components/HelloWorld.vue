<template>
  <div class="welcome">
    <h1>Welcome to spoc</h1>
    <br>
    <button @click="goToStudentLogin">我是学生</button>
    <br>
    <button @click="goToTeacherLogin">我是老师</button>
  </div>
</template>

<script>
export default {
  methods: {
    goToStudentLogin () {
      this.$router.push({
        name: 'StudentLogin'
      })
    },
    goToTeacherLogin () {
      this.$router.push({
        name: 'TeacherLogin'
      })
    }
  }
}
</script>

<style scoped>

</style>
