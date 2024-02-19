from fastapi import APIRouter, status, File, UploadFile, HTTPException
from typing import Dict
from api.controllers import tag_image_controller

router = APIRouter(
    tags=["tag"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/health_check", status_code=200)
async def health_check() -> dict:
    return {"msg": "Tag route is working propperly"}


@router.post("/")
async def tag_image(image: UploadFile = File(...)) -> Dict:
    try:
        return tag_image_controller.tag_image(image)
    except HTTPException as ex:
        raise ex
