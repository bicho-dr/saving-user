from src.User import User
from src.saving_user_use_case_interface import saving_user_use_case_interface
from src.user_Repository_DTO import user_Repository_DTO
from src.user_saving_Repository_interface import saving_Repository_interface


class saving_user_use_case (saving_user_use_case_interface):

    def __init__(self, repository: saving_Repository_interface):
        self.repository = repository

    def execute(self, data: User)->user_Repository_DTO:
        return self.repository.save(data)
