from entities.task import Task
from entities.user import User
from repositories.user_repository import user_repository
from repositories.task_repository import task_repository

class StudytrackerService():

    def __init__(self):
        self.user = None
        self.user_repository = user_repository
        self.task_repository = task_repository

    def create_task(self, topic, category, deadline):
        self.task_repository.validate_task(topic, category, deadline)
        self.task_repository.create(Task(topic, category, deadline), self.user)

    def find_users_tasks(self):
        return self.task_repository.find_all_by_user(self.user)

    def create_user(self, username, password):
        self.user_repository.validate_credentials(username, password)
        return self.user_repository.create(User(username, password))

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if not user:
            raise ValueError(f"Käyttäjätunnusta {username} ei ole olemassa")
        if password != user.password:
            raise ValueError("Virheellinen käyttäjätunnus tai salasana")

        self.user = user

        return user

    def get_logged_user(self):
        return self.user

    def logout(self):
        self.user = None


studytracker_service = StudytrackerService()
