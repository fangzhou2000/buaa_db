<template>
  <div>
    <el-row>
      <el-col :span="11">
        <el-input
          type="textarea"
          :rows="35"
          v-model="text"
          @change="convertText">
        </el-input>
      </el-col>
      <el-col :span="12" :offset="1">
        <div v-html="html" class="text">
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
//import showdown from 'showdown'
import showdown from '../../assets/js/showdown.min'
export default {
  name: "CommentPlatForm",
  data() {
    return {
      html: '',
      text: '',
      converter: {}
    }
  },
  components: {
    showdown
  },
  methods: {
    convertText() {
      this.html = this.converter.makeHtml(this.text);
    }
  },
  mounted() {
    //创建实例
    this.converter = new showdown.Converter();
  }
}
</script>

<style lang="less" scoped>
  @import "../../assets/css/markDownDec/sspai.css";
</style>
