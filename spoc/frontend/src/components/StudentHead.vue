<template>
  <h1>
    学生首页
    <p>
      <button v-on:click="goToStudentLogin">返回</button>
    </p>
  </h1>
</template>

<script>

export default {
  methods: {
    goToStudentLogin () {
      this.$router.push({
        name: 'StudentLogin'
      })
    }
  }
}
</script>

<style scoped>

</style>
