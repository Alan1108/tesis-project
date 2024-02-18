from fastapi import APIRouter, status, File, UploadFile, HTTPException
from fastapi.responses import Response

import json

from api.controllers import tag_image_controller

router = APIRouter(
    tags=["tag"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/health_check", status_code=200)
async def health_check() -> dict:
    return {"msg": "Tag route is working propperly"}


@router.post("/", response_class=Response)
async def tag_image(image: UploadFile = File(...)) -> Response:
    try:
        result = tag_image_controller.tag_image(image)
        return Response(
            content=result["body"]["image"],
            headers={
                "X-prediction-data": json.dumps(result["body"]["data"])
            },
            media_type="image/jpeg",
            status_code=result["status"]
        )
    except HTTPException as ex:
        raise ex
