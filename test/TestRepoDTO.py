import pytest
from pytest_mock import mocker

from src.user_Repository_DTO import user_Repository_DTO


class TestRepoDTO:

    def test_repo_dto_has_default_success_values(self):
        dto = user_Repository_DTO()

        assert dto.error is False
        assert dto.msg == "success"