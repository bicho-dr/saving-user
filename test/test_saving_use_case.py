from pytest_mock import mocker

from src.User import User
from src.saving_Repository import saving_Repository
from src.saving_use_case import saving_user_use_case



def test_execute_should_call_internal_save(mocker):
    # Arrange
    mock_repository = mocker.Mock()
    use_case = saving_user_use_case(mock_repository)
    save_spy = mocker.spy(use_case ,"execute")
    data = User(first_name="Ali", last_name="Ahmed")

    # Act
    use_case.execute(data)

    # Assert
    save_spy.assert_called_once()

def test_execute_use_case_should_be_called_once_with_data(mocker):
    # Arrange
    mock_repository = mocker.Mock()
    use_case = saving_user_use_case(mock_repository)
    data = User(first_name="Ali", last_name="Ahmed")
    save_spy = mocker.spy(use_case, "execute")

    # Act
    use_case.execute(data)

    # Assert
    save_spy.assert_called_once_with(data)

def test_execute_should_call_repository_save_once_with_user(mocker):
    # Arrange
    mock_repository = mocker.Mock()
    use_case = saving_user_use_case(mock_repository)
    user = User(first_name="Ali", last_name="Ahmed")

    # Act
    use_case.execute(user)

    # Assert
    mock_repository.save.assert_called_once_with(user)


def test_execute_should_call_repository_save_spy(mocker):
    # Arrange
    repository = saving_Repository()
    save_spy = mocker.spy(repository, "save")
    use_case = saving_user_use_case(repository)

    user = User(first_name="Ali", last_name="Ahmed")

    # Act
    use_case.execute(user)

    # Assert
    save_spy.assert_called_once_with(user)

