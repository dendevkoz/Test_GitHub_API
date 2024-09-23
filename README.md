# GitHub API

Автоматический тест для проверки работы с GitHub API на языке Python.
 Тест создаёт, проверяет наличие и удаляет репозиторий на GitHub

### Как установить
- Создайте файл `.env` в корне проекта и записать в него настройки:
    ```python
    GITHUB_TOKEN = 'токен API'
    ```
    ```python
    GITHUB_USERNAME = 'имя пользователя GitHub'
    ```
    ```python
    REPO_NAME = 'имя репозитория'
    ```
- Создаём виртуальное окружение 
    ```python
    python -m venv venv
    ```
    Путь до корневой папки 
    ```python 
    venv/scripts/activate
    ```
- Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
    ```python
    pip install -r requirements.txt
    ```

### Запуск скрипта:
- Команда для запуска
    ```python
       python -m pytest
    ```