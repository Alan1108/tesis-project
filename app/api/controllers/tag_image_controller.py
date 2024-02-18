import logging
from fastapi import HTTPException, UploadFile
from http import HTTPStatus
from api.implementation.tag_image_repository_implementation import (
    TagImageRepository
)
from api.use_cases.tag_image_use_case import TageImageUseCase


def tag_image(image: UploadFile):
    try:
        tag_image_repository = TagImageRepository()
        tag_image_use_case = TageImageUseCase(
            tag_image_repository
        )
        clean_data, new_image = tag_image_use_case.execute(image=image)
        return {
            "status": HTTPStatus.OK,
            "message": "Image tagged succesfully",
            "body": {
                "data": clean_data,
                "image": new_image
            }
        }
    except HTTPException as ex:
        logging.error(msg={"error": ex.detail})
        raise ex
