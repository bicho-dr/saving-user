from src.User import User
from src.user_Repository_DTO import user_Repository_DTO


class user_saving_Repository:
    def save(self, user: User)->user_Repository_DTO:
        # TODO: Repositor mySql
        return user_Repository_DTO()