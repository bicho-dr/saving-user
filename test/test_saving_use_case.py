from src.User import User
from src.saving_use_case import saving_user_use_case


def test_execute_should_call_internal_save(mocker):
    # Arrange
    use_case = saving_user_use_case()
    save_spy = mocker.spy(use_case ,"execute")

    # Act
    use_case.execute()

    # Assert
    save_spy.assert_called_once()

def test_execute_use_case_should_be_called_once_with_data(mocker):
    # Arrange
    use_case = saving_user_use_case()
    data = User(first_name="Ali", last_name="Ahmed")
    save_spy = mocker.spy(use_case, "execute")

    # Act
    use_case.execute(data)

    # Assert
    save_spy.assert_called_once_with(data)