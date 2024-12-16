import unittest
from repositories.user_repository import user_repository
from entities.user import User
from initialize_database import initialize_database


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.testuser_1 = User("user_1", "password123")
        self.testuser_2 = User("user_2", "password456")

    def test_create_user(self):
        user_repository.create(self.testuser_1)
        all_users = user_repository.find_all()

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, self.testuser_1.username)

    def test_find_by_existing_username(self):
        user_repository.create(self.testuser_1)
        user_1 = user_repository.find_by_username(self.testuser_1.username)
        self.assertEqual(user_1.username, self.testuser_1.username)

    def test_find_by_non_existing_username(self):
        user_repository.create(self.testuser_1)
        no_user = user_repository.find_by_username("testuser1")
        self.assertEqual(no_user, None)

    def test_find_all(self):
        user_repository.create(self.testuser_1)
        user_repository.create(self.testuser_2)
        all_users = user_repository.find_all()

        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].username, self.testuser_1.username)
        self.assertEqual(all_users[1].username, self.testuser_2.username)

    def test_validate_with_existing_username(self):
        user_repository.create(self.testuser_1)
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("user_1", "password123")
        self.assertEqual(str(error.exception),
                         "Käyttäjätunnus user_1 on jo olemassa")

    def test_validate_with_too_short_username(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("tes", "password123")
        self.assertEqual(str(error.exception),
                         "Käyttäjätunnuksen minimipituus on 4 merkkiä")

    def test_validate_with_too_short_password(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("test_user123", "pass")
        self.assertEqual(str(error.exception),
                         "Salasanan minimipituus on 5 merkkiä")

    def test_validate_with_too_long_username(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials(
                "test_user123" * 5, "password123")
        self.assertEqual(str(error.exception),
                         "Käyttäjätunnuksen maksimipituus on 20 merkkiä")

    def test_validate_with_too_long_password(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials(
                "test_user123", "password123" * 5)
        self.assertEqual(str(error.exception),
                         "Salasanan maksimipituus on 20 merkkiä")

    def test_all_fields_emptyraises_an_error(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("", "")
        self.assertEqual(str(error.exception), "Käyttäjätunnus ja salasana ovat pakollisia kenttiä")
