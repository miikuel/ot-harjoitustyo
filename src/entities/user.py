class User:

    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: merkkijono, joka kuvaa käyttäjän käyttäjänimeä.
        password: merkkijono, joka kuvaa käyttäjän salasanaa.
        id: käyttäjän yksilöivä id tietokannassa.
    """

    def __init__(self, username, password, user_id=None):
        self.username = username
        self.password = password
        self.id = user_id
