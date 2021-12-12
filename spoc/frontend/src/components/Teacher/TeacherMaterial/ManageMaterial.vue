<template>
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
        <el-table :data="showMyMaterialList" v-loading="loading" >
          <el-table-column label="学习材料ID" prop="id"></el-table-column>
          <el-table-column label="学习材料名称" prop="name"></el-table-column>
          <el-table-column label="删除">
            <template slot-scope="scope">
              <el-button v-on:click="deleteMaterial(scope.$index)"
                         type="danger"
                         size="small">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
      </el-container>
    </el-container>
</template>

<script>
import TeacherNav from '../TeacherNav'
import TeacherHeading from '../TeacherHeading'
export default {
  name: 'ManageMaterial',
  components: {TeacherNav, TeacherHeading},
  data: function () {
    return {
      loading: true,
      userNickName: '',
      userName: '',
      myMaterialList: [{
        id: '1',
        name: '前端测试学习材料'
      }],
      showMyMaterialList: [{
        id: '1',
        name: '前端测试学习材料'
      }],
      inputSearch: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getTeacherMaterialList()
  },
  methods: {
    getTeacherMaterialList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherMaterialList/',
        method: 'get',
        params: {
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.myMaterialList = response.data
        that.showMyMaterialList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    deleteMaterial: function (index) {
      this.$confirm('此操作将永久删除该学习材料，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        that.loading = true
        this.$http.request({
          url: that.$url + 'DeleteMaterial/',
          method: 'get',
          params: {
            userName: that.userName,
            id: that.showMyMaterialList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('删除成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getTeacherMaterialList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    searchCourse: function (inputSearch) {
      let that = this
      that.showMyMaterialList = that.searchByIndexOf(inputSearch, that.myMaterialList)
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
