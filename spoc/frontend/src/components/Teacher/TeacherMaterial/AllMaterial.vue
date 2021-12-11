<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
      </el-aside>
      <el-container class="main">
        <el-header>
          <TeacherHeading></TeacherHeading>
        </el-header>
        <el-main style="padding-left: 10%; padding-right: 10%">
           <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找您的相关资料"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 5%"></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="float: right"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
          </el-row>
          <el-table :data="showMaterialList" v-loading="loading">
            <el-table-column label="学习材料ID" prop="id"></el-table-column>
            <el-table-column label="学习材料名称" prop="name"></el-table-column>
          </el-table>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'AllMaterial',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userNickName: '',
      userName: '',
      inputSearch: '',
      materialList: [{
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }, {
        id: '1',
        name: '前端测试课程材料'
      }],
      showMaterialList: this.materialList
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getMaterialList()
  },
  methods: {
    getMaterialList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetMaterialList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.materialList = response.data
        that.showMaterialList = response.data
      }).catch(function (error) {
        that.loading = false
        console.log(error)
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    searchCourse: function (inputSearch) {
      this.showMaterialList = this.searchByIndexOf(inputSearch, this.materialList)
    },
    searchByIndexOf: function (keyWord, list) {
      if (!(list instanceof Array)) {
        return
      } else if (keyWord === '') {
        return list
      }
      const len = list.length
      const arr = []
      for (let i = 0; i < len; i++) {
        // 如果字符串中不包含目标字符会返回-1
        if (list[i].name.indexOf(keyWord) >= 0) {
          arr.push(list[i])
        }
      }
      return arr
    }
  }
}
</script>

<style scoped>
 @import "../../../assets/css/nav.css";
 @import "../../../assets/css/back.css";
</style>
