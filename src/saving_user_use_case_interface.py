from abc import ABC, abstractmethod

from src.User import User
from src.user_Repository_DTO import user_Repository_DTO


class saving_user_use_case_interface(ABC):

    @abstractmethod
    def execute(self, data: "User")->user_Repository_DTO:
        pass