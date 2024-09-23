from config.settings import GITHUB_TOKEN


class Headers:
    def __init__(self, token=GITHUB_TOKEN):
        self.token = token
        self.api_version = '2022-11-28'  # it was taken from https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28

    def create_headers(self) -> dict:
        header = {"Authorization": f"Bearer {GITHUB_TOKEN}",
                  "X-GITHUB-Api-Version": self.api_version,
                  "Accept": "application/vnd.github.v3+json"}
        return header
