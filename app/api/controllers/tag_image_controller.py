import logging
from api.implementation.tag_image_repository_implementation import (
    TagImageRepository
)

from api.use_cases.tag_image_use_case import TageImageUseCase
from fastapi import HTTPException
from http import HTTPStatus


def tag_image():
    try:
        tag_image_repository = TagImageRepository()
        tag_image_use_case = TageImageUseCase(
            tag_image_repository
        )
        body = tag_image_use_case.execute()
        return {
            "status": HTTPStatus.OK,
            "message": "Image tagged succesfully",
            "body": body
        }
    except Exception as ex:
        logging.error(msg={"error": str(ex)})
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )
