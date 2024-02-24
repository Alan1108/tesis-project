from api.repositories.tag_image_repository import ITagImageRepository
from api.constants.constants import ClassColors
from api.config.env_vars import Variables
import cv2
from uuid import uuid4
import numpy as np
import base64
from http import HTTPStatus
from typing import List, Dict
from google.cloud import storage
from fastapi import UploadFile, HTTPException
from roboflow import Roboflow


class TagImageRepository(ITagImageRepository):
    def __init__(self):
        self.storage_client = storage.Client(project="tesis-aibm")
        self.bucket_name = "4697de56-3dd6-468a-8f26-75fb956069aa"
        self.blob_name = "image_to_be_tagged.jpg"

    def tag_image(self, image: UploadFile) -> tuple:
        try:
            rf = Roboflow(api_key=Variables().ROBO_API_KEY)
            project = rf.workspace(Variables().ROBO_WORKSPACE)\
                .project(Variables().ROBO_PROJECT_NAME)
            model = project.version(4).model
            file_url = self._store_image(image)

            prediction_data = model.predict(
                file_url,
                hosted=True,
                confidence=40,
                overlap=30
            ).json()

            cleaned_data = self._clean_data(
                prediction_data=prediction_data["predictions"]
            )
            new_image = self._draw_image(
                prediction_data=prediction_data["predictions"],
                image=image
            )
            image_base64 = base64.b64encode(new_image)
            return cleaned_data, image_base64
        except Exception as ex:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=str(ex)
            )

    def _store_image(self, image: UploadFile) -> str:
        blob_name = str(uuid4())
        bucket = self.storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_file(image.file)
        return blob.public_url

    def _draw_image(self, prediction_data, image: UploadFile) -> bytes:
        image.file.seek(0)
        content = image.file.read()
        nparr = np.fromstring(content, np.uint8)
        new_image_arr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        for bounding_box in prediction_data:
            color = next((diccionario["BGR"]
                          for diccionario in ClassColors.COLORS2
                          if diccionario["class"] == bounding_box["class"]),
                         None)
            x0 = bounding_box['x'] - bounding_box['width'] / 2
            x1 = bounding_box['x'] + bounding_box['width'] / 2
            y0 = bounding_box['y'] - bounding_box['height'] / 2
            y1 = bounding_box['y'] + bounding_box['height'] / 2

            start_point = (int(x0), int(y0))
            end_point = (int(x1), int(y1))
            new_image_arr = cv2.rectangle(
                new_image_arr,
                start_point,
                end_point,
                color=color,
                thickness=3
            )

        img_encode = cv2.imencode(".jpg", new_image_arr)[1]
        return img_encode.tobytes()

    def _clean_data(self, prediction_data) -> List[Dict]:
        class_count = {}
        for prediction in prediction_data:
            class_name = prediction["class"]
            if class_name not in class_count:
                class_count[class_name] = 0
            class_count[class_name] += 1
        clean_data = []
        total_detections = len(prediction_data)
        for class_name, ocurrences in class_count.items():
            clean_data.append({
                "class_name": class_name,
                "percentage": str(round((ocurrences*100.0)/total_detections)),
                "color": next((class_item["color_name"]
                              for class_item in ClassColors.COLORS2
                              if class_item["class"] == class_name),
                              None)
            })
        return clean_data
