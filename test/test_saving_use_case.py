def test_execute_should_call_internal_save(mocker):
    # Arrange
    use_case = saving_user_use_case()
    save_spy = mocker.spy(use_case ,"execute")

    # Act
    use_case.execute()

    # Assert
    save_spy.assert_called_once()

class saving_user_use_case :
    def execute(self):
        pass