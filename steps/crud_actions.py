from api_client.api_client import ApiClient
from api_client.headers import Headers
from routes.routes import routes
from data.create_repo_dto import CreateRepositoryDto
from requests import Response


class ApiGitHubActions:
    '''Можно каждую операцию разделить по классу, но я решил Crud реализовать в одном классе.
    Знаю, что это не best practice.'''
    def __init__(self):
        self.client = ApiClient()

    def create_repository(self, data: dict = None) -> Response:
        if not data:
            data = CreateRepositoryDto().dict()
        response = self.client.post(route=routes.CREATE_REPO, json=data, headers=Headers().create_headers())
        return response

    def get_repository(self) -> Response:
        response = self.client.get(route=routes.GET_REPO, headers=Headers().create_headers())
        return response

    def delete_repository(self) -> Response:
        response = self.client.delete(route=routes.DELETE_REPO, headers=Headers().create_headers())
        return response
