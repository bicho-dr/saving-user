from abc import abstractmethod, ABC

from src.User import User


class saving_Repository_interface(ABC):
    @abstractmethod
    def save(self, user: User):
        pass