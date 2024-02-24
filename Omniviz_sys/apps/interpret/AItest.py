import random
import os.path as osp
from osgeo import gdal
import cv2
import numpy as np
import paddle
import paddlers as pdrs
from paddlers import transforms as T


MODEL_PATH = '../../RS/models/object_detection/faster_rcnn'
IMAGE_PATH = '../../../raw_images/202311290101.jpg'
OUTPUT_PATH = '../../../result/OD/202311290101.jpg'

p = pdrs.deploy.Predictor(model_dir=MODEL_PATH,
                          use_gpu=True)
detections = p.predict(img_file=IMAGE_PATH, topk=2)

# 读取图像
# dataset = gdal.Open(IMAGE_PATH)
# band = dataset.GetRasterBand(1)
# data = band.ReadAsArray()
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)
image = image.astype(np.uint16)

rgb_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint16)
rgb_image[:,:,0] = image
rgb_image[:,:,1] = image
rgb_image[:,:,2] = image

# 循环遍历检测结果并绘制边界框
for detection in detections:
    category = detection['category']
    bbox = detection['bbox']
    score = float(detection['score'])

    if score > 0.7:
        x, y, w, h = map(int, bbox)
        # 绘制边界框
        cv2.rectangle(rgb_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 使用绿色绘制边界框
        cv2.putText(rgb_image, category, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imwrite(OUTPUT_PATH + 'output.jpg', rgb_image)

# driver = gdal.GetDriverByName("GTiff")
# geotransform = dataset.GetGeoTransform()
# output_dataset = driver.Create(OUTPUT_PATH+'output.tif', dataset.RasterXSize, dataset.RasterYSize, dataset.RasterCount, gdal.GDT_UInt16)
# output_dataset.SetGeoTransform(geotransform)
# output_band = output_dataset.GetRasterBand(1)
# output_band.WriteArray(data)
# output_dataset = None
# dataset = None

