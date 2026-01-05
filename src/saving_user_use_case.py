from src.User import User
from src.user_saving_Repository_interface import saving_Repository_interface


class saving_user_use_case :

    def __init__(self, repository: saving_Repository_interface):
        self.repository = repository

    def execute(self, data: User):
        self.repository.save(data)
