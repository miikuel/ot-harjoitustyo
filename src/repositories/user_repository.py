from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    """Käyttäjään liittyvistä tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def create(self, user):
        """Tallentaa uuden käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-oliona.

        Returns:
            True jos tallennus onnistui ja muuten False
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                           (user.username, user.password))
            self.connection.commit()
            return True
        except:
            return False

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus
        Returns:
            Palauttaa User-olion, jos käyttäjä löytyy tietokannasta ja muuten None.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
        user = cursor.fetchone()

        if not user:
            return None
        return User(user["username"], user["password"], user["id"])

    def validate_credentials(self, username, password):
        """Validoi uuden käyttäjän käyttäjätunnuksen ja salasanan ennen luomista.

        Args:
        username: Käyttäjätunnus
        password: Salasana
        """
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
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return [User(user["username"], user["password"], user["id"]) for user in users]



user_repository = UserRepository(get_database_connection())
