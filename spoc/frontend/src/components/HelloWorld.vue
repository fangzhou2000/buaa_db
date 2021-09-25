<template>
    <div class="about">
        <h1>This is DataTest</h1>
        {{d2}}
        <p v-for="d in d1">
            {{d}}
        </p>
        <button @click="init">点击获取数据</button>

    </div>
</template>

<script>
    export default {
        data:function () {
            return{
                d1:['默认列表数据1','默认列表数据2'],
                d2:'默认字符串',
            }


        },
        methods:{
          init:function () {
            let _this = this
            this.$http.request({
                    url:_this.$url+'DataTest/',
                    method:'get',
                }).then(function (response) {
                    _this.d1=response.data
                }).catch(function (response) {
                    console.log(response)
                })
          }
        }
    }
</script>

<style scoped>

</style>
