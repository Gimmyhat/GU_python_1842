from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def fabric(self):
        return self.height * 2 + 0.3


class Summary:
    def __init__(self, *args):
        self.__subobjects = args

    @property
    def fabric(self):
        res = 0
        for subobject in self.__subobjects:
            res += subobject.fabric
        return res


coat1 = Coat(27)
suit1 = Suit(2)
clothes = Summary(coat1, suit1)
print(f'Общий расход ткани составит {clothes.fabric:.2f} м2')
