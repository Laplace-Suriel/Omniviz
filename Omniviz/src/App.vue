<template>
  <div>
    <el-container>
      <el-header id="header">Omniviz 遥感智能解译平台</el-header>
      <el-container id="container">
        <el-aside id="aside" width="200px">
          <Menu />
        </el-aside>
        <el-main id="main">
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Menu from "./components/menu.vue"

</script>

<style scoped>
#container{
  height: 94vh;
}
#header{
  height: 6vh;
  width: 100%;
  line-height: 40px;
  font-size: 20px;
  text-align: left;
  background-image: linear-gradient(120deg, #8fd3f4 0%, #84fab0 100%);
}

#main{
  display: flex;
  justify-content: space-between;
}

</style>
