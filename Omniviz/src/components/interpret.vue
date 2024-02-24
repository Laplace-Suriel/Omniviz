<template>
  <div class="ip">
    <el-select
      v-model="model_value"
      class="select"
      placeholder="选择模型"
      size="large"
    >
      <el-option
        v-for="item in props.options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
    <br /><br /><br />
    <el-button
      class="button"
      type="primary"
      round
      @click="
        () => {
          interpret();
        }
      "
      >解 译</el-button
    >
  </div>
</template>

<script setup>
import { ref } from "vue";

const model_value = ref("");

const emit = defineEmits(["update-values2"]);
const props = defineProps([
  "filename",
  "options",
  "api",
  "isCD",
  "filename1",
  "filename2",
]);
const local_base64_image = ref("");
async function interpret() {
  const IP = "127.0.0.1";
  const PORT = "8000";
  const API = "/interpret/api/" + props.api;
  const URL = `http://${IP}:${PORT}${API}`;
  const data = {
    model: model_value.value,
    filename: props.filename,
  };
  const data_cd = {
    model: model_value.value,
    filename1: props.filename1,
    filename2: props.filename2,
  };
  try {
    let response;
    if (props.isCD) {
      response = await fetch(URL, {
        method: "POST",
        body: JSON.stringify(data_cd),
      });
    } else {
      response = await fetch(URL, {
        method: "POST",
        body: JSON.stringify(data),
      });
    }
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const responseData = await response.json();
    local_base64_image.value = responseData.base64_image;
    emit("update-values2", local_base64_image.value, props.filename);
  } catch (error) {
    console.error("Error fetching data:", error);
    return null;
  }
}
</script>

<style scoped>
.ip {
  background-image: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);
}
.button {
  width: 50%;
  height: 8%;
  font-size: 18px;
}
.select {
  width: 100%;
  height: 10%;
  margin-top: 300px;
}
</style>
