<template>
  <el-menu
    active-text-color="#ffd04b"
    background-color="#545c64"
    class="el-menu-vertical"
    :default-active="$route.name"
    text-color="#fff"
  >
    <el-menu-item index="ObjectDetection" @click="switchComponent('ObjectDetection')">
      <el-icon><icon-menu /></el-icon>
      <span>目标检测</span>
    </el-menu-item>
    <el-menu-item index="Classification" @click="switchComponent('Classification')">
      <el-icon><document /></el-icon>
      <span>地物分类</span>
    </el-menu-item>
    <el-menu-item index="ChangeDetection" @click="switchComponent('ChangeDetection')">
      <el-icon><setting /></el-icon>
      <span>变化检测</span>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import {
  Document,
  Menu as IconMenu,
  Setting,
} from "@element-plus/icons-vue";
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();

function switchComponent(componentName) {
  router.push({ name: componentName });
}

</script>

<style scoped>
.el-menu-vertical {
  height: 100%;
}
</style>