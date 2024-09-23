from pydantic import BaseModel
from config.settings import REPO_NAME, GITHUB_BASE_URL
from faker import Faker

fake = Faker()


class CreateRepositoryDto(BaseModel):
    name: str = REPO_NAME
    description: str = fake.catch_phrase()
    homepage: str = GITHUB_BASE_URL
    private: bool = False
    has_issues: bool = False
    has_projects: bool = False
    has_wiki: bool = False


