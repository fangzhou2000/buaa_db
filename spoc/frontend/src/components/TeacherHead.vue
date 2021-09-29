<template>
  <h1>
    老师首页
    <p>
      <button v-on:click="goToTeacherLogin">返回</button>
    </p>
  </h1>
</template>

<script>

export default {
  methods: {
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
