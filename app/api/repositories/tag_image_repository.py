from abc import ABCMeta, abstractclassmethod


class ITagImageRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def tag_image(self):
        raise NotImplementedError
