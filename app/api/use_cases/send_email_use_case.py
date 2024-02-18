from .base_use_case import BaseUseCase
from api.models.email_model import EmailModel
from api.repositories.send_email_repository import ISendEmailRepository


class SendEmailUseCase(BaseUseCase):
    """Represents the use case to send the email from contact form"""

    def __init__(self, repository: ISendEmailRepository):
        super().__init__(repository)

    def execute(self, email_info: EmailModel):
        self.repository.send_email(email_info=email_info)
        return email_info
