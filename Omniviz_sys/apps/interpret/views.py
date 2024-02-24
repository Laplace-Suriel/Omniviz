from rest_framework.views import APIView
from rest_framework.response import Response
from osgeo import gdal, gdal_array
import datetime
import base64
import cv2
import json
import numpy as np
import paddlers as pdrs

MODEL_PATH = 'RS/models/'
IMAGE_PATH = '../raw_images/'
OUTPUT_PATH = '../result/'

class OD_Interpret(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        filename = json_data.get('filename')
        model = json_data.get('model')
        p = pdrs.deploy.Predictor(model_dir=MODEL_PATH+'object_detection/'+model, use_gpu=True)
        detections = p.predict(img_file=IMAGE_PATH+filename)
        image = cv2.imread(IMAGE_PATH+filename, cv2.IMREAD_UNCHANGED)

        rgb_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        rgb_image[:, :, 0] = image
        rgb_image[:, :, 1] = image
        rgb_image[:, :, 2] = image

        # 循环遍历检测结果并绘制边界框
        for detection in detections:
            category = detection['category']
            bbox = detection['bbox']
            score = float(detection['score'])

            if score > 0.2:
                x, y, w, h = map(int, bbox)
                # 绘制边界框
                cv2.rectangle(rgb_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(rgb_image, category, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imwrite(OUTPUT_PATH + 'OD/' + filename, rgb_image)
        _, encoded_image = cv2.imencode(".jpg", rgb_image)
        base64_image = base64.b64encode(encoded_image).decode("utf-8")
        return Response({'message': 'Success',
                         'base64_image': base64_image})


class Seg_Interpret(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        filename = json_data.get('filename')
        model = json_data.get('model')
        p = pdrs.deploy.Predictor(model_dir=MODEL_PATH+'classification/'+model, use_gpu=True)
        detections = p.predict(img_file=IMAGE_PATH+filename)

        lut = {
            0: (255, 0, 0),
            1: (0, 0, 255),
            2: (0, 255, 0),
            3: (255, 255, 0),
            4: (0, 0, 0),
            5: (255, 255, 255),
            6: (0, 255, 255),
            7: (255, 0, 255)
        }

        rgb_image = np.zeros((detections['label_map'].shape[0], detections['label_map'].shape[1], 3), dtype=np.uint8)

        max_label = np.max(detections['label_map'])

        for i in range(max_label + 1):
            color = lut[i]
            rgb_image[(detections['label_map'] == i)] = color

        cv2.imwrite(OUTPUT_PATH + 'Seg/' + filename, rgb_image)
        _, encoded_image = cv2.imencode(".jpg", rgb_image)
        base64_image = base64.b64encode(encoded_image).decode("utf-8")
        return Response({'message': 'Success',
                         'base64_image': base64_image})


class CD_Interpret(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        filename1 = json_data.get('filename1')
        filename2 = json_data.get('filename2')
        model = json_data.get('model')
        p = pdrs.deploy.Predictor(model_dir=MODEL_PATH+'change_detection/'+model, use_gpu=True)
        detections = p.predict(img_file=(IMAGE_PATH+filename1, IMAGE_PATH+filename2))

        data = (detections['label_map'] * 255).astype(np.uint8)
        cv2.imwrite(OUTPUT_PATH + 'CD/' + filename1, data)
        _, encoded_image = cv2.imencode(".jpg", data)
        base64_image = base64.b64encode(encoded_image).decode("utf-8")
        return Response({'message': 'Success',
                         'base64_image': base64_image})


class ImgUpload(APIView):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        extension = uploaded_file.name.split('.')[-1]
        current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        filename = f"{current_datetime}.{extension}"
        path = IMAGE_PATH + filename
        with open(path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        raster: np.ndarray
        if extension in ['tif', 'tiff']:
            dataset = gdal.Open(path)
            band_count = dataset.RasterCount
            raster = dataset.ReadAsArray()
            dataset = None

            if band_count > 3:
                raster = raster[3:0:-1, :, :]
            if raster.dtype != 'uint8':
                raster = cv2.normalize(raster, None, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                raster.astype(np.uint8)
            gdal_array.SaveArray(raster, path)
            if band_count != 1:
                raster = np.transpose(raster, (1, 2, 0))
        else:
            raster = cv2.imread(path)

        _, encoded_image = cv2.imencode(".jpg", raster)
        base64_image = base64.b64encode(encoded_image).decode("utf-8")

        return Response({'message': 'Success',
                         'base64_image': base64_image,
                         'filename': filename})
