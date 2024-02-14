from api.repositories.tag_image_repository import ITagImageRepository


class TagImageRepository(ITagImageRepository):
    def tag_image(self):
        raise NotImplementedError
