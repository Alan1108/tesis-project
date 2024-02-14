from api.repositories.get_image_data_repository import IGetImageDataRepository


class GetImageDataRepository(IGetImageDataRepository):
    def get_image_data(self):
        raise NotImplementedError
