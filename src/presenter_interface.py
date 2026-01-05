from abc import ABC, abstractmethod

from src.user_Repository_DTO import user_Repository_DTO

class presenter_interface(ABC):

    @abstractmethod
    def present(self, data: user_Repository_DTO) :
        pass