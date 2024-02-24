<template>
  <div class="image-container">
    <img
      id="upload-show"
      v-if="base64_image"
      :src="`data:image/jpeg;base64,${base64_image}`"
      alt="Image"
    />
    <el-upload
      v-if="!base64_image"
      class="upload"
      :on-success="uploadSuccess"
      drag
      :action="URL"
      :limit="1"
    >
      <br /><br />
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <br /><br />
      <template #tip>
        <div class="el-upload__tip">jpg/png/tif/bmp file</div>
      </template>
    </el-upload>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { UploadFilled } from "@element-plus/icons-vue";

const emit = defineEmits([
  "update-values1",
  "update-values1_1",
  "update-values1_2",
]);
const IP = "127.0.0.1";
const PORT = "8000";
const API = "/interpret/api/upload";
const URL = `http://${IP}:${PORT}${API}`;

const { base64_image, filename, id } = defineProps([
  "base64_image",
  "filename",
  "id",
]);
const local_base64_image = ref("");
const local_filename = ref("");
const uploadSuccess = (response) => {
  local_base64_image.value = response.base64_image;
  local_filename.value = response.filename;
  if (id == 1) {
    emit("update-values1_1", local_base64_image.value, local_filename.value);
  } else if (id == 2) {
    emit("update-values1_2", local_base64_image.value, local_filename.value);
  } else {
    emit("update-values1", local_base64_image.value, local_filename.value);
  }
};
</script>

<style scoped>
.image-container {
  width: 100%;
  aspect-ratio: 1 / 1;
}
#upload-show {
  height: fit-content;
  width: 100%;
}
</style>
