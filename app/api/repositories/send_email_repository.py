from abc import ABCMeta, abstractclassmethod
from api.models.email_model import EmailModel


class ISendEmailRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def send_email(self, email_info: EmailModel):
        raise NotImplementedError
