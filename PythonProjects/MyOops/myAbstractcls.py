from abc import ABC, abstractmethod


class myclass(ABC):

    @abstractmethod
    def nonsence(self):
        pass



class Etc(myclass):

    def nonsence(self):
        print("woowwwwww")


obj = Etc()
obj.nonsence()
