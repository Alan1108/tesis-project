from .base_use_case import BaseUseCase
from api.repositories.tag_image_repository import ITagImageRepository


class TageImageUseCase(BaseUseCase):
    """Represents the use case to tag the image"""

    def __init__(self, repository: ITagImageRepository):
        super().__init__(repository)

    def execute(self):
        self.repository.tag_image()
