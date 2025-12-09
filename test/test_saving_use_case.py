import pytest
from pytest_mock import mocker

from src.User import User
from src.saving_Repository import saving_Repository
from src.saving_use_case import saving_user_use_case

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
        repository = saving_Repository()
        save_spy = mocker.spy(repository, "save")
        use_case = saving_user_use_case(repository)


        # Act
        use_case.execute(user_test)

        # Assert
        save_spy.assert_called_once_with(user_test)

