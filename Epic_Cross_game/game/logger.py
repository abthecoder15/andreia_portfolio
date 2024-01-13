import logging


# Set up the logger
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CustomLogger:
    @staticmethod
    def log_connection_success():
        logger.info('Database connected successfully!')

    @staticmethod
    def log_registration(username, hashed_password):
        logger.info(f"Registered username: {username}, Hashed password: {hashed_password}")

    @staticmethod
    def log_login(username):
        logger.info(f"Logged in: {username}")

    @staticmethod
    def log_updated_score(username, level, higher_score):
        logger.info(f"Score updated: HigherScoreLevel{level} - Username: {username}, Score: {higher_score}")

    @staticmethod
    def log_updated_total_score(username, total_score):
        logger.info(f"Total score updated - Username: {username}, Total Score: {total_score}")
