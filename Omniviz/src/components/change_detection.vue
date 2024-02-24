<template>
  <div class="image-containers">
    <FileUpload
      :id="1"
      :base64_image="base64_image1"
      :filename="filename1"
      @update-values1_1="updateValues1"
    />
    <br />
    <FileUpload
      :id="2"
      :base64_image="base64_image2"
      :filename="filename2"
      @update-values1_2="updateValues2"
    />
  </div>
  <div class="show">
    <img
      v-if="base64_image"
      :src="`data:image/jpeg;base64,${base64_image}`"
      class="image"
    />
    <el-upload v-if="!base64_image" drag>
      <div class="el-upload__text">Text</div>
    </el-upload>
  </div>
  <Interpret
    :isCD="true"
    :filename1="filename1"
    :filename2="filename2"
    class="interpret"
    :options="options"
    :api="api"
    @update-values2="updateValues"
  />
</template>

<script setup>
import { ref } from "vue";
import FileUpload from "./upload.vue";
import Interpret from "./interpret.vue";

const base64_image1 = ref("");
const filename1 = ref("");
const base64_image2 = ref("");
const filename2 = ref("");
const base64_image = ref("");
const filename = ref("");

const options = [
  {
    value: "bit",
    label: "Bit",
  },
  {
    value: "Option2",
    label: "Option2",
  },
];
const api = "CD";

const updateValues1 = (updatedBase64Image, updatedFilename) => {
  base64_image1.value = updatedBase64Image;
  filename1.value = updatedFilename;
};
const updateValues2 = (updatedBase64Image, updatedFilename) => {
  base64_image2.value = updatedBase64Image;
  filename2.value = updatedFilename;
};
const updateValues = (updatedBase64Image, updatedFilename) => {
  base64_image.value = updatedBase64Image;
  filename.value = updatedFilename;
};
</script>

<style scoped>
.image-containers {
  display: flex;
  flex-direction: column;
  width: 300px;
  height: 300px;
}
.show {
  margin-top: 80px;
}
.el-upload-dragger .el-upload__text {
  height: 400px;
  width: 500px;
  color: transparent;
}
.interpret {
  display: flex;
  background-color: paleturquoise;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 15%;
}
.image {
  max-width: 90%;
  max-height: 90%;
}
</style>
