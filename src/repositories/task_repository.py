import re
from datetime import datetime
from database_connection import get_database_connection
from entities.task import Task

class TaskRepository():
    def __init__(self, connection):
        self.connection = connection

    def create(self, task, user):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tasks (topic, category, deadline, user_id) VALUES (?, ?, ?, ?)",
                       (task.topic, task.category, task.deadline, user.id))
        self.connection.commit()

    def find_all_by_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user.id, ))
        tasks = cursor.fetchall()
        return [Task(task["topic"], task["category"], task["deadline"], task["id"]) for task in tasks]

    def set_done(self, task):
        pass

    def delete(self, task):
        pass

    def validate_task(self, topic, category, deadline):
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
        except ValueError as e:
            raise ValueError("Deadline ei ole todellinen päivämäärä") from e


task_repository = TaskRepository(get_database_connection())
