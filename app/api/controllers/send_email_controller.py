import logging
from api.implementation.send_email_repository_implementation import (
    SendEmailRepository
)
from api.models.email_model import EmailModel
from api.use_cases.send_email_use_case import SendEmailUseCase
from fastapi import HTTPException
from http import HTTPStatus


def send_email(email_info: EmailModel):
    try:
        send_email_repository = SendEmailRepository()
        send_email_use_case = SendEmailUseCase(send_email_repository)
        body = send_email_use_case.execute(email_info=email_info)
        return {
            "status": HTTPStatus.OK,
            "message": "Email sent succesfully",
            "body": body
        }
    except Exception as ex:
        logging.error(msg={"error": str(ex)})
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )
