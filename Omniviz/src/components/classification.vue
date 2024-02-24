<template>
  <FileUpload
    :id="0"
    class="upload"
    :base64_image="base64_image"
    :filename="filename"
    @update-values1="updateValues"
  />
  <Interpret
    :isCD="false"
    :filename="filename"
    @update-values2="updateValues"
    class="interpret"
    :options="options"
    :api="api"
  />
</template>

<script setup>
import { ref } from "vue";
import FileUpload from "./upload.vue";
import Interpret from "./interpret.vue";
const base64_image = ref("");
const filename = ref("");

const options = [
  {
    value: "deeplabv3p",
    label: "DeepLabV3P",
  },
  {
    value: "Option2",
    label: "Option2",
  },
];
const api = "Seg";

const updateValues = (updatedBase64Image, updatedFilename) => {
  base64_image.value = updatedBase64Image;
  filename.value = updatedFilename;
};
</script>

<style scoped>
.upload {
  margin-left: 185px;
  width: 650px;
  height:650px;
}

.interpret {
  display: flex;
  background-color: paleturquoise;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 15%;
}
</style>
