import logging
import smtplib
import os
from http import HTTPStatus
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api.repositories.send_email_repository import ISendEmailRepository
from api.models.email_model import EmailModel

from fastapi import HTTPException


class SendEmailRepository(ISendEmailRepository):
    def send_email(self, email_info: EmailModel):
        try:
            message = MIMEMultipart()
            message["To"] = email_info.to_email
            message["From"] = os.environ.get("SMTP_MAIL")
            message["Subject"] = email_info.email_subject

            messageText = MIMEText(email_info.email_message)
            message.attach(messageText)

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo('Gmail')
            server.starttls()
            server.login(
                user=os.environ.get("SMTP_MAIL"),
                password=os.environ.get("SMTP_PASS")
            )
            fromaddr = os.environ.get("SMTP_MAIL")
            toaddrs = email_info.to_email
            server.sendmail(fromaddr, toaddrs, message.as_string())
            server.quit()

        except Exception as ex:
            logging.error(msg={"error": str(ex)})
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=str(ex)
            )
