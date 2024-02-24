import { createRouter, createWebHashHistory } from 'vue-router';
import ObjectDetection from '../components/object_detection.vue';
import Classification from '../components/classification.vue';
import ChangeDetection from '../components/change_detection.vue';

const routes = [
  {
    path: '/',
    component: ObjectDetection,
    name: 'ObjectDetection',
  },
  {
    path: '/Classification',
    component: Classification,
    name: 'Classification',
  },
  {
    path: '/ChangeDetection',
    component: ChangeDetection,
    name: 'ChangeDetection',
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;