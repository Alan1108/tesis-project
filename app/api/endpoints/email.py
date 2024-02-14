from fastapi import APIRouter, status, HTTPException
from typing import Dict
from api.controllers import send_email_controller
from api.models.email_model import EmailModel
from http import HTTPStatus

router = APIRouter(
    tags=["email"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/health_check", status_code=200)
async def health_check() -> dict:
    return {"msg": "Email route is working propperly"}


@router.post("/")
async def send_email(
    email_info: EmailModel,
) -> Dict:
    try:
        return send_email_controller.send_email(email_info=email_info)
    except HTTPException as ex:
        return {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "error": str(ex)
        }
