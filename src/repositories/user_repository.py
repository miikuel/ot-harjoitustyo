from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create(self, user):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                           (user.username, user.password))
            self.connection.commit()
            return True
        except:
            return False

    def find_by_username(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        user = cursor.fetchone()

        if not user:
            return None
        return User(user["username"], user["password"], user["id"])

    def validate_credentials(self, username, password):
        if len(username) == 0 and len(password) == 0:
            raise ValueError("Käyttäjätunnus ja salasana ovat pakollisia kenttiä")
        if self.find_by_username(username):
            raise ValueError(f"Käyttäjätunnus {username} on jo olemassa")
        if len(username) < 4:
            raise ValueError("Käyttäjätunnuksen minimipituus on 4 merkkiä")
        if len(password) < 5:
            raise ValueError("Salasanan minimipituus on 5 merkkiä")
        if len(username) > 20:
            raise ValueError("Käyttäjätunnuksen maksimipituus on 20 merkkiä")
        if len(password) > 20:
            raise ValueError("Salasanan maksimipituus on 20 merkkiä")

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return [User(user["username"], user["password"], user["id"]) for user in users]



user_repository = UserRepository(get_database_connection())
