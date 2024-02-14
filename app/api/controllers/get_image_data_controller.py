import logging
from api.implementation.get_image_data_repository_implementation import (
    GetImageDataRepository
)

from api.use_cases.get_image_data_use_case import GetImageDataUseCase
from fastapi import HTTPException
from http import HTTPStatus


def get_image_data():
    try:
        get_image_data_repository = GetImageDataRepository()
        get_image_data_use_case = GetImageDataUseCase(
            get_image_data_repository
        )
        body = get_image_data_use_case.execute()
        return {
            "status": HTTPStatus.OK,
            "message": "Image info retrieved succesfully",
            "body": body
        }
    except Exception as ex:
        logging.error(msg={"error": str(ex)})
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )
