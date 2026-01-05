import pytest
from pytest_mock import mocker

from src.User import User
from src.user_Repository_DTO import user_Repository_DTO
from src.user_saving_Repository import user_saving_Repository
from src.saving_user_use_case import saving_user_use_case

@pytest.mark.parametrize(
        "user_test",
        [
            User("Ahmed", "Fares"),
            User("Ali", "Mansour"),
            User("Amjed", "Hassan"),
            User("Farid", "Othman"),
            User("Youssef", "Nader"),
            User("Bachir", "dridi"),
            User("mohammed", "ziad"),
            User("islam", "Hala"),
            User("sami", "anis"),
            User("aymen", "Nouri"),

        ],
    )

class TestSavingUseCase :


    def test_execute_should_call_internal_save(self ,mocker, user_test):
        # Arrange
        mock_repository = mocker.Mock()
        use_case = saving_user_use_case(mock_repository)
        save_spy = mocker.spy(use_case ,"execute")


        # Act
        use_case.execute(user_test)

        # Assert
        save_spy.assert_called_once()



    def test_execute_use_case_should_be_called_once_with_data(self ,mocker , user_test):
        # Arrange
        mock_repository = mocker.Mock()
        use_case = saving_user_use_case(mock_repository)
        save_spy = mocker.spy(use_case, "execute")

        # Act
        use_case.execute(user_test)

        # Assert
        save_spy.assert_called_once_with(user_test)


    def test_execute_should_call_repository_save_once_with_user(self ,mocker ,user_test):
        # Arrange
        mock_repository = mocker.Mock()
        use_case = saving_user_use_case(mock_repository)

        # Act
        use_case.execute(user_test)

        # Assert
        mock_repository.save.assert_called_once_with(user_test)



    def test_execute_should_call_repository_save_spy(slfe ,mocker , user_test):
        # Arrange
        repository = user_saving_Repository()
        save_spy = mocker.spy(repository, "save")
        use_case = saving_user_use_case(repository)


        # Act
        use_case.execute(user_test)

        # Assert
        save_spy.assert_called_once_with(user_test)

    def test_user_saving_repo_returns_repo_dto(slfe, mocker, user_test):
        repo = user_saving_Repository()

        result = repo.save(user_test)

        assert result.error is False
        assert result.msg == "success"

    def test_execute_use_case_should_be_return_user_Repository_DTO(slfe, mocker, user_test):
        Repository = user_saving_Repository()
        use_case = saving_user_use_case(Repository)

        result = use_case.execute(user_test)

        assert isinstance(result, user_Repository_DTO)
        assert result.error is False
        assert result.msg == "success"