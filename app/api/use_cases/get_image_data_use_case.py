from .base_use_case import BaseUseCase
from api.repositories.get_image_data_repository import IGetImageDataRepository


class GetImageDataUseCase(BaseUseCase):
    """Represents the use case to get the tagged image data"""

    def __init__(self, repository: IGetImageDataRepository):
        super().__init__(repository)

    def execute(self):
        self.repository.get_image_data()
