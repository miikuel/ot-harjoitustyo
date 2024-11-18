import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
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

    def test_delete_all(self):
        user_repository.create(self.testuser_1)
        user_repository.create(self.testuser_2)
        all_users = user_repository.find_all()
        user_repository.delete_all()

        self.assertEqual(len(all_users), 0)

    def test_validate_with_existing_username(self):
        user_repository.create(self.testuser_1)
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("user_1", "password123")
        self.assertEqual(str(error.exception), "Username user_1 already exists")

    def test_validate_with_too_short_username(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("tes", "password123")
        self.assertEqual(str(error.exception), "Username must be at least 4 characters long")

    def test_validate_with_too_short_password(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("test_user123", "pass")
        self.assertEqual(str(error.exception), "Password must be at least 5 characters long")
    
    def test_validate_with_too_long_username(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("test_user123" * 5, "password123")
        self.assertEqual(str(error.exception), "Maximum length for username is 20 characters")

    def test_validate_with_too_long_password(self):
        with self.assertRaises(ValueError) as error:
            user_repository.validate_credentials("test_user123", "password123" * 5)
        self.assertEqual(str(error.exception), "Maximum length for password is 20 characters")

    def test_validate_with_valid_credentials(self):
        validation = user_repository.validate_credentials("user_1", "password123")
        self.assertEqual(validation, True)





