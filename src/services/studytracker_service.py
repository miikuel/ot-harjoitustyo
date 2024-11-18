from entities.task import Task
from entities.user import User
from repositories.user_repository import user_repository

class StudytrackerService():

    def __init__(self):
        self.user = None
        self.user_repository = user_repository

    def create_user(self, username, password):
        self.user_repository.validate_credentials(username, password)
        new_user = self.user_repository.create(User(username, password))
        return new_user
    
    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if not user:
            raise ValueError(f"Username {username} does not exists")
        if password != user.password:
            raise ValueError(f"Invalid username or password")
        
        self.user = user

        return user
    
    def get_logged_user(self):
        return self.user
    
    def logout(self):
        self.user = None

studytracker_service = StudytrackerService()


