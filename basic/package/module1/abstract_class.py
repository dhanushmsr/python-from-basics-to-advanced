from abc import ABC,abstractclassmethod
class password_check(ABC):
    @abstractclassmethod
    def pass_match(self):
        pass
    @abstractclassmethod
    def pass_accept(self):
        pass