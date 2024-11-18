class UserRepository:
    def __init__(self):
        self.users = []


    def create(self, user):
        self.users.append(user)

    def find_by_username(self, username):  
        for user in self.users:
            print(user.username)
            if user.username == username:
                return user
        return None
    
    def validate_credentials(self, username, password):
        if self.find_by_username(username):
            raise ValueError(f"Username {username} already exists")
        if len(username) < 4:
            raise ValueError("Username must be at least 4 characters long")
        if len(password) < 5:
            raise ValueError("Password must be at least 5 characters long")
        if len(username) > 20:
            raise ValueError("Maximum length for username is 20 characters")
        if len(password) > 20:
            raise ValueError("Maximum length for password is 20 characters")
        return True
        
    def delete_all(self):
        while self.users:
            self.users.pop()

    def find_all(self):
        return self.users


    
user_repository = UserRepository()
