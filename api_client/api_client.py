import requests
from config.settings import GITHUB_API_URL
from allure import step


class ApiClient:
    def __init__(self):
        self.base_url = GITHUB_API_URL

    @step('POST-запрос к серверу')
    def post(self, route=None, data=None, headers=None, params=None, json=None):
        return requests.post(f'{self.base_url}{route}', data=data, json=json, headers=headers, params=params)

    @step('GET-запрос к серверу')
    def get(self, route=None, headers=None, params=None):
        return requests.get(f'{self.base_url}{route}', headers=headers, params=params)

    @step('PUT-запрос к серверу')
    def put(self, route=None, data=None, headers=None, params=None, json=None):
        return requests.put(f'{self.base_url}{route}', data=data, headers=headers, params=params, json=json)

    @step('PATCH-запрос к серверу')
    def patch(self, route=None, headers=None, params=None, json=None):
        return requests.patch(f'{self.base_url}{route}', json=json, headers=headers, params=params)

    @step('DELETE-запрос к серверу')
    def delete(self, route=None, headers=None, params=None):
        return requests.delete(f'{self.base_url}{route}', headers=headers, params=params)
