from abc import abstractmethod, ABC

from src.User import User
from src.user_Repository_DTO import user_Repository_DTO


class saving_Repository_interface(ABC):
    @abstractmethod
    def save(self, user: User) ->user_Repository_DTO:
        pass