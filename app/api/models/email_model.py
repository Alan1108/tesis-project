from pydantic import BaseModel


class EmailModel(BaseModel):
    to_email: str
    email_subject: str
    email_message: str
