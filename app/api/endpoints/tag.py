from fastapi import APIRouter, status, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from http import HTTPStatus
from typing import Dict

from api.controllers import get_image_data_controller
from api.controllers import tag_image_controller

router = APIRouter(
    tags=["tag"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/health_check", status_code=200)
async def health_check() -> dict:
    return {"msg": "Tag route is working propperly"}


@router.post("/")
async def tag_image(image: UploadFile = File()) -> StreamingResponse:
    try:
        tag_image_controller.tag_image()
        return StreamingResponse(content=None, media_type="image/jpeg")
    except HTTPException as ex:
        ex.detail = "Not implemented yet"
        ex.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        raise ex


@router.post("/image_data")
async def get_image_data(image: UploadFile = File()) -> Dict:
    try:
        get_image_data_controller.get_image_data()
        return {}
    except HTTPException as ex:
        ex.detail = "Not implemented yet"
        ex.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        raise ex
