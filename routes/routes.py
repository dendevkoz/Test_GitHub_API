from config.settings import GITHUB_USERNAME, REPO_NAME


class Routes():

    CREATE_REPO = "/user/repos"
    AUTHORIZE = f"/users/{GITHUB_USERNAME}"
    GET_REPO = f"/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    DELETE_REPO = f"/repos/{GITHUB_USERNAME}/{REPO_NAME}"


routes = Routes()
