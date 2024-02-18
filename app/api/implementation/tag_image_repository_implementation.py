from api.repositories.tag_image_repository import ITagImageRepository
from api.constants.constants import ClassColors
import cv2
import os
import numpy as np
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
            rf = Roboflow(api_key=os.environ.get("ROBO_API_KEY"))
            project = rf.workspace(os.environ.get("ROBO_WORKSPACE"))\
                .project(os.environ.get("ROBO_PROJECT_NAME"))
            model = project.version(4).model
            file_url = self._store_image(image)

            prediction_data = model.predict(
                file_url,
                hosted=True,
                confidence=40,
                overlap=30
            ).json()

            self._delete_image()
            cleaned_data = self._clean_data(
                prediction_data=prediction_data["predictions"]
            )
            new_image = self._draw_image(
                prediction_data=prediction_data["predictions"],
                image=image
            )
            return cleaned_data, new_image
        except Exception as ex:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=str(ex)
            )

    def _store_image(self, image: UploadFile) -> str:
        bucket = self.storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(self.blob_name)
        blob.upload_from_file(image.file)
        return blob.public_url

    def _delete_image(self) -> None:
        bucket = self.storage_client.get_bucket(self.bucket_name)
        bucket.delete_blob(self.blob_name)

    def _draw_image(self, prediction_data, image: UploadFile) -> bytes:
        image.file.seek(0)
        content = image.file.read()
        nparr = np.fromstring(content, np.uint8)
        new_image_arr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        previous_class = ""
        color_count = 0
        color = ()
        previous_classes = []
        for bounding_box in prediction_data:
            if previous_class != bounding_box["class"] and\
                    bounding_box["class"] not in previous_classes:
                color = ClassColors.COLORS[color_count]
                color_count += 1

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
                color=(color[0]),
                thickness=3
            )

            """ new_image_arr = cv2.putText(
                new_image_arr,
                bounding_box["class"],
                (int(x0), int(y0) - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.4,
                color=(255, 255, 255),
                thickness=1
            ) """
            previous_class = bounding_box["class"]
            previous_classes.append(bounding_box["class"])
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
        color_counter = 0
        class_colors = ClassColors()
        for class_name, ocurrences in class_count.items():
            clean_data.append({
                "class_name": class_name,
                "percentage": str(round((ocurrences*100.0)/total_detections)),
                "color": class_colors.COLORS[color_counter][1]
            })
            color_counter += 1
        return clean_data
