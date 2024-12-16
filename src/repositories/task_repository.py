import re
from datetime import datetime
from database_connection import get_database_connection
from entities.task import Task

class TaskRepository():
    """Tehtäviin liittyvistä tietokantaoperaatioista vastaava luokka.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def create(self, task, user):
        """Tallentaa tehtävän tietokantaan.

        Args:
            task: Tallennettava tehtävä Task-oliona.
            user: Käyttäjä User-oliona.
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (topic, category, deadline, user_id) VALUES (?, ?, ?, ?)",
                       (task.topic, task.category, task.deadline, user.id))
        self.connection.commit()

    def find_all_by_user(self, user):
        """Palauttaa kaikki käyttäjän tehtävät.

        Args:
            user: Käyttäjä User-oliona.

        Returns:
            Palauttaa listan Task-olioita.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user.id, ))
        tasks = cursor.fetchall()
        return [Task(task["topic"], task["category"], task["deadline"],
                     task["id"], task["done"]) for task in tasks]

    def set_done(self, task_id):
        """Merkkaa tehtävän tehdyksi.

        Args:
            task_id: tehtävän yksilöivä id
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tasks set done = 1 WHERE id = ?", (task_id, ))
        self.connection.commit()

    def set_not_done(self, task_id):
        """Palauttaa tehtävän tekemättömäksi.

        Args:
            task_id: tehtävän yksilöivä id
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE tasks set done = 0 WHERE id = ?", (task_id, ))
        self.connection.commit()

    def validate_task(self, topic, category, deadline):
        """Validoi uuden tehtävän aiheen, kategorian ja määräpäivän ennen luomista.

        Args:
            topic: Merkkijonoarvo, joka kuvaa tehtävän aihetta.
            category: Merkkijonoarvo, joka kuvaa tehtävän kategoriaa.
            deadline: Merkkijonoarvo, joka kuvaa tehtävän määräpäivää.
        """
        if not topic and not category and not deadline:
            raise ValueError("Kaikki kentät ovat pakollisia")
        if not topic or len(topic.strip()) == 0:
            raise ValueError("Aihe ei saa olla tyhjä")
        if len(topic) > 100:
            raise ValueError("Aiheen maksimipituus on 100 merkkiä")
        if not category or len(category.strip()) == 0:
            raise ValueError("Kategoria ei saa olla tyhjä")
        if len(category) > 50:
            raise ValueError("Kategorian maksimipituus on 50 merkkiä")
        if not re.match(r"^\d{1,2}\.\d{1,2}\.\d{4}$", deadline):
            raise ValueError("Deadline tulee antaa muodossa \"d.m.yyyy\"")
        try:
            datetime.strptime(deadline, "%d.%m.%Y")
        except ValueError as error:
            raise ValueError("Deadline ei ole todellinen päivämäärä") from error


task_repository = TaskRepository(get_database_connection())
