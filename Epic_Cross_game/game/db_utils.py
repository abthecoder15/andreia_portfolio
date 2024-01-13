import mysql.connector
import hashlib


class Database:
    def __init__(self, config):
        self.db = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        self.cursor = self.db.cursor()

    def close_connection(self):
        self.cursor.close()
        self.db.close()

# Add decorator
    @staticmethod
    def close_connection_decorator(func):
        def wrapper(*args, **kwargs):
            db_instance = args[0]
            result = func(*args, **kwargs)
            db_instance.close_connection()
            return result

        return wrapper


    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            sql = "INSERT INTO Players (Username, PasswordHash, HigherScoreLevel1, HigherScoreLevel2, HigherScoreLevel3, TotalHigherScore) VALUES (%s, %s, %s, %s, %s, %s)"
            initial_score = 0  # Initial score for a new user
            values = (username, hashed_password, initial_score, initial_score, initial_score, initial_score)
            self.cursor.execute(sql, values)
            self.db.commit()
            return True  # Registration successful
        except mysql.connector.Error as err:
            print("Error:", err)
        return False  # Registration failed

    def login_user(self, username, password):
        hashed_password = self.hash_password(password)

        try:
            sql = "SELECT * FROM Players WHERE Username = %s AND PasswordHash = %s"
            values = (username, hashed_password)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()

            if result:
                return True  # Authentication successful
            return False  # Authentication failed
        except mysql.connector.Error as err:
            print("Error:", err)
        return False  # Failed to authenticate

    def get_game_levels(self):
        try:
            self.cursor.execute("SELECT LevelName, TimerSeconds FROM GameLevels")
            levels_info = self.cursor.fetchall()
            return levels_info
        except mysql.connector.Error as err:
            print("MySQL error:", err)
            return None  # Return None on error

    def update_user_score(self, username, new_score, level):
        try:
            # Get the user's current highest score for the specified level
            current_higher_score = self.get_user_higher_score(username, level)

            # Construct the column name based on the level
            column_name = f"HigherScoreLevel{level}"

            # Compare the new score with the current highest score
            if current_higher_score is None or new_score > current_higher_score:
                # Update the HigherScore for the specified level only if the new score is greater
                sql = f"UPDATE Players SET {column_name} = %s WHERE Username = %s"
                values = (new_score, username)
                self.cursor.execute(sql, values)
                self.db.commit()
                return True  # Higher score updated successfully
        except mysql.connector.Error as err:
            print("Error:", err)
        return False  # Failed to update higher score

    def get_user_higher_score(self, username, level):
        try:
            # Construct the column name based on the level
            column_name = f"HigherScoreLevel{level}"

            sql = f"SELECT {column_name} FROM Players WHERE Username = %s"
            values = (username,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Return the current highest score for the specified level
            else:
                return None  # User not found or no score recorded for the specified level
        except mysql.connector.Error as err:
            print("Error:", err)
            return None  # Return None on error or no result

    def get_total_higher_score(self, username):
        try:
            sql = "SELECT SUM(HigherScoreLevel1 + HigherScoreLevel2 + HigherScoreLevel3) AS TotalHigherScore FROM Players WHERE Username = %s"
            values = (username,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Return the total higher score
            else:
                return None  # User not found or no score recorded
        except mysql.connector.Error as err:
            print("Error:", err)
            return None  # Return None on error or no result

    def update_total_higher_score(self, username):
        try:
            total_higher_score = self.get_total_higher_score(username)
            if total_higher_score is not None:
                sql = "UPDATE Players SET TotalHigherScore = %s WHERE Username = %s"
                values = (total_higher_score, username)
                self.cursor.execute(sql, values)
                self.db.commit()
                return True  # TotalHigherScore updated successfully
        except mysql.connector.Error as err:
            print("Error:", err)
        return False  # Failed to update TotalHigherScore
