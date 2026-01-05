from abc import ABC, abstractmethod

from src.User import User


class saving_user_use_case_interface(ABC):

    @abstractmethod
    def execute(self, data: "User"):
        pass