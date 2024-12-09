import unittest
from repositories.task_repository import task_repository
from entities.task import Task
from entities.user import User
from initialize_database import initialize_database


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.test_task_1 = Task("Viikkotehtävät", "Ohjelmistotekniikka", "5.11.2024")
        self.test_task_2 = Task("Harjoitustyö", "Ohjelmistotekniikka", "12.11.2024")
        self.test_user_1 = User("user_1", "password123", user_id=1)
        self.test_user_2 = User("user_2", "password456", user_id=2)

    def test_valid_create_input_does_not_raise_an_error(self):
        task_repository.create(self.test_task_1, self.test_user_1)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)

        self.assertEqual(len(users_tasks), 1)
        self.assertEqual(users_tasks[0].topic, self.test_task_1.topic)
        self.assertEqual(users_tasks[0].category, self.test_task_1.category)
        self.assertEqual(users_tasks[0].deadline, self.test_task_1.deadline)

    def test_find_tasks_returns_empty_list_with_incorrect_user(self):
        task_repository.create(self.test_task_1, self.test_user_1)
        users_tasks = task_repository.find_all_by_user(self.test_user_2)

        self.assertEqual(len(users_tasks), 0)

    def test_empty_topic_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("", "Ohjelmistotekniikka", "5.11.2024")
        self.assertEqual(str(error.exception), "Aihe ei saa olla tyhjä")

    def test_only_a_space_in_topic_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task(" ", "Ohjelmistotekniikka", "5.11.2024")
        self.assertEqual(str(error.exception), "Aihe ei saa olla tyhjä")

    def test_too_long_topic_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("a"*101, "Ohjelmistotekniikka", "5.11.2024")
        self.assertEqual(str(error.exception), "Aiheen maksimipituus on 100 merkkiä")

    def test_empty_category_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "", "5.11.2024")
        self.assertEqual(str(error.exception), "Kategoria ei saa olla tyhjä")

    def test_only_a_space_in_category_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", " ", "5.11.2024")
        self.assertEqual(str(error.exception), "Kategoria ei saa olla tyhjä")

    def test_too_long_category_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "o"*51, "5.11.2024")
        self.assertEqual(str(error.exception), "Kategorian maksimipituus on 50 merkkiä")

    def test_empty_deadline_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "Ohjelmistotekniikka", "")
        self.assertEqual(str(error.exception), "Deadline tulee antaa muodossa \"d.m.yyyy\"")

    def test_only_a_space_in_deadline_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "Ohjelmistotekniikka", " ")
        self.assertEqual(str(error.exception), "Deadline tulee antaa muodossa \"d.m.yyyy\"")

    def test_incorrect_deadline_format_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "Ohjelmistotekniikka", "1-12-2024")
        self.assertEqual(str(error.exception), "Deadline tulee antaa muodossa \"d.m.yyyy\"")

    def test_non_existing_date_raises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("Viikkotehtävät", "Ohjelmistotekniikka", "1.13.2024")
        self.assertEqual(str(error.exception), "Deadline ei ole todellinen päivämäärä")

    def test_user_can_set_task_done(self):
        task_repository.create(self.test_task_1, self.test_user_1)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)

        self.assertEqual(len(users_tasks), 1)
        self.assertEqual(users_tasks[0].done, False)

        task_repository.set_done(users_tasks[0].task_id)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)
        self.assertEqual(users_tasks[0].done, True)

    def test_all_fields_emptyraises_an_error(self):
        with self.assertRaises(ValueError) as error:
            task_repository.validate_task("", "", "")
        self.assertEqual(str(error.exception), "Kaikki kentät ovat pakollisia")

    def test_user_can_set_task_not_done(self):
        task_repository.create(self.test_task_1, self.test_user_1)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)

        self.assertEqual(len(users_tasks), 1)
        self.assertEqual(users_tasks[0].done, False)

        task_repository.set_done(users_tasks[0].task_id)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)
        self.assertEqual(users_tasks[0].done, True)

        task_repository.set_not_done(users_tasks[0].task_id)
        users_tasks = task_repository.find_all_by_user(self.test_user_1)
        self.assertEqual(users_tasks[0].done, False)
