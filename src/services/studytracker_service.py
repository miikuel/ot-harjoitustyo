from entities.task import Task
from entities.user import User
from repositories.user_repository import user_repository
from repositories.task_repository import task_repository

class StudytrackerService():
    """Sovelluslogiikasta vastaa luokka."""

    def __init__(self):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun
        ja asettaa alkuarvot attribuuteille:
            user:
                Käyttäjää kuvaava muuttuja, johon sijoitetaan User-olio.
                Oletusarvoltaan None.
            user_repository:
                Oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
            task_repository:
                Oletusarvoltaan TaskRepository-olio.
                Olio, jolla on TaskRepository-luokkaa vastaavat metodit.
        """
        self.user = None
        self.user_repository = user_repository
        self.task_repository = task_repository

    def create_task(self, topic, category, deadline):
        """Luo uuden tehtävän.

        Args:
            topic: Merkkijonoarvo, joka kuvaa tehtävän aihetta.
            category: Merkkijonoarvo, joka kuvaa tehtävän kategoriaa.
            deadline: Merkkijonoarvo, joka kuvaa tehtävän määräpäivää.
        """
        self.task_repository.validate_task(topic, category, deadline)
        self.task_repository.create(Task(topic, category, deadline), self.user)

    def find_users_tasks(self):
        """Palauttaa kirjautuneen käyttäjän kaikki tehtävät.

        Returns:
            Palauttaa kirjautuneen käyttäjän kaikki tehtävät Task-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """
        return self.task_repository.find_all_by_user(self.user)

    def set_task_done(self, task_id):
        """Asettaa tehtävän tilan tehdyksi.
        Args:
            task_id: tehtävän yksilöivä id.
        """
        task_repository.set_done(task_id)

    def set_task_not_done(self, task_id):
        """Palauttaa tehtävän tilan tekemättömäksi.
        Args:
            task_id: tehtävän yksilöivä id.
        """
        task_repository.set_not_done(task_id)

    def create_user(self, username, password):
        """Luo uuden käyttäjän jos validointi onnistuu.
        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjätnimeä.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.
        Returns:
            Luotu käyttäjä User-oliona.
        """
        self.user_repository.validate_credentials(username, password)
        return self.user_repository.create(User(username, password))

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.
        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjänimeä.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        Raises:
            ValueError:
                Virhe, jos käyttäjätunnus tai salasana ovat virheelliset.
        """
        user = self.user_repository.find_by_username(username)
        if not user:
            raise ValueError(f"Käyttäjätunnusta {username} ei ole olemassa")
        if password != user.password:
            raise ValueError("Virheellinen käyttäjätunnus tai salasana")

        self.user = user

        return user

    def get_logged_user(self):
        """Paluttaa kirjautuneen käyttäjän.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        """
        return self.user

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self.user = None


studytracker_service = StudytrackerService()
