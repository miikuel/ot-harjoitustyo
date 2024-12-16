import unittest
from services.studytracker_service import studytracker_service
from initialize_database import initialize_database


class TestStudytrackerService(unittest.TestCase):

    def setUp(self):
        initialize_database()

    def test_user_can_create_account_and_log_in_and_log_out(self):
        self.assertIsNone(studytracker_service.get_logged_user())
        studytracker_service.create_user("test_user", "password123")
        studytracker_service.login("test_user", "password123")
        self.assertIsNotNone(studytracker_service.get_logged_user())
        self.assertEqual(studytracker_service.user.username, "test_user")
        studytracker_service.logout()
        self.assertIsNone(studytracker_service.get_logged_user())

    def test_invalid_credentials_in_login_throw_error(self):
        studytracker_service.create_user("test_user", "password123")
        with self.assertRaises(ValueError) as error:
            studytracker_service.login("test_user2", "password123")
        self.assertEqual(str(error.exception), "Käyttäjätunnusta test_user2 ei ole olemassa")
        with self.assertRaises(ValueError) as error:
            studytracker_service.login("test_user", "password12345")
        self.assertEqual(str(error.exception), "Virheellinen käyttäjätunnus tai salasana")
        studytracker_service.logout()

    def test_create_task_set_done_and_not_done(self):
        studytracker_service.create_user("test_user", "password123")
        studytracker_service.login("test_user", "password123")
        self.assertEqual(len(studytracker_service.find_users_tasks()), 0)
        studytracker_service.create_task("Loppupalautus", "Ohjelmistotekniikka", "22.12.2024")
        self.assertEqual(len(studytracker_service.find_users_tasks()), 1)
        self.assertEqual(studytracker_service.find_users_tasks()[0].done, 0)
        task_id = studytracker_service.find_users_tasks()[0].task_id
        studytracker_service.set_task_done(task_id)
        self.assertEqual(studytracker_service.find_users_tasks()[0].done, 1)
        studytracker_service.set_task_not_done(task_id)
        self.assertEqual(studytracker_service.find_users_tasks()[0].done, 0)
