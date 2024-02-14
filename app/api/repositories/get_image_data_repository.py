from abc import ABCMeta, abstractclassmethod


class IGetImageDataRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def get_image_data(self):
        raise NotImplementedError
