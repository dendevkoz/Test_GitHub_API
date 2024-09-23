import config.settings
from steps.crud_actions import ApiGitHubActions


class TestCrudGitHub:

    def test_check_authorize_via_github(self):
        create_repo = ApiGitHubActions().create_repository()
        assert create_repo.ok
        get_repo = ApiGitHubActions().get_repository()
        assert get_repo.ok
        assert get_repo.json()['name'] == config.settings.REPO_NAME
        delete_repo = ApiGitHubActions().delete_repository()
        assert delete_repo.status_code == 204
