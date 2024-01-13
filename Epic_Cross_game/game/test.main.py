import unittest
import mysql.connector
from main import *
from game import *
sys.path.append("../database/db_config")
sys.path.append("../game/main")
sys.path.append("../game/game")


def validate_username_length(username):
    MIN_LENGTH = 6
    MAX_LENGTH = 12
    if MIN_LENGTH <= len(username) <= MAX_LENGTH:
        return True
    else:
        return False


def validate_password_length(password):
    MIN_LENGTH = 6
    MAX_LENGTH = 12
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return True
    else:
        return False


# Test Registration and Login inputs
class TestRegistrationInput(unittest.TestCase):
    def test_username_password_length_min(self):
        username = "12345"
        password = "12345"
        self.assertFalse(validate_username_length(username))
        self.assertFalse(validate_password_length(password))

    def test_username_password_length_max(self):
        username = "123456789012345678901"
        password = "123456789012345678901"
        self.assertFalse(validate_username_length(username))
        self.assertFalse(validate_password_length(password))


class TestLoginInput(unittest.TestCase):
    def test_username_password_length_min(self):
        username = "12345"
        password = "12345"
        self.assertFalse(validate_username_length(username))
        self.assertFalse(validate_password_length(password))

    def test_username_password_length_max(self):
        username = "123456789012345678901"
        password = "123456789012345678901"
        self.assertFalse(validate_username_length(username))
        self.assertFalse(validate_password_length(password))


# Test database connection
class TestMySQLConnection(unittest.TestCase):
    def test_database_connection(self):
        try:
            conn = mysql.connector.connect()
            self.assertIsNotNone(conn)
            conn.close()  # Close the connection after the test
        except Exception as e:
            self.fail(f"Database connection failed with error: {str(e)}")


# Test enemies movements

# ... (Enemy class definitions)
E1 = EnemyOne()
E2 = Enemytwo()
E3 = Enemythree()
E4 = Enemyfour()


class TestEnemies(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_enemy_one_movement(self):
        enemy_one = EnemyOne()
        initial_rect = enemy_one.rect.copy()

        # Move the enemy
        enemy_one.move()

        # Check if the enemy has moved to the right
        self.assertGreater(enemy_one.rect.left, initial_rect.left)

    def test_enemy_two_movement(self):
        enemy_two = Enemytwo()
        initial_rect = enemy_two.rect.copy()

        # Move the enemy
        enemy_two.move()

        # Check if the enemy has moved to the right
        self.assertGreater(enemy_two.rect.left, initial_rect.left)

    def test_enemy_three_movement(self):
        enemy_three = Enemythree()
        initial_rect = enemy_three.rect.copy()

        # Move the enemy
        enemy_three.move()

        # Check if the enemy has moved to the right
        self.assertGreater(enemy_three.rect.left, initial_rect.left)

    def test_enemy_four_movement(self):
        enemy_four = Enemyfour()
        initial_rect = enemy_four.rect.copy()

        # Move the enemy
        enemy_four.move()

        # Check if the enemy has moved to the right
        self.assertGreater(enemy_four.rect.left, initial_rect.left)

    def test_enemy_reset(self):
        enemy_one = EnemyOne()
        enemy_one.rect.left = 100  # Simulate moving the enemy to the right

        # Reset the enemy
        enemy_one.reset()

        # Check if the enemy is reset to the initial position on the left
        self.assertEqual(enemy_one.rect.left, 0)
        self.assertEqual(enemy_one.rect.centery, 271)