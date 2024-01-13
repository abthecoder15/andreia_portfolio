import sys
import time
from logger import CustomLogger
from pygame.locals import *
from db_utils import Database
from db_config import DBConfig
from game import *

# Initialize the database object
db = Database(DBConfig)

# Log the database connection status
connection_status = "Successful" if db else "Failed"
CustomLogger.log_connection_success()

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants and initializations
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window = SCREEN_WIDTH, SCREEN_HEIGHT
START_TIME = pygame.time.get_ticks() // 1000  # Initial time in seconds
SPEED = 4

# Load the sounds
game_background_sound = pygame.mixer.Sound('../assets/sounds/game_background_sound.wav')
game_over_sound = pygame.mixer.Sound('../assets/sounds/game_over_sound.wav')
level_passed_sound = pygame.mixer.Sound('../assets/sounds/level_passed_sound.wav')
winner_sound = pygame.mixer.Sound('../assets/sounds/winner_sound.wav')

font = pygame.font.SysFont("Verdana", 30)

# Initialize Pygame and set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


def welcome_screen():
    title_font = pygame.font.SysFont("Verdana", 80)
    title_text = title_font.render("EpicCross Quest", True, BLACK)
    subtitle_font = pygame.font.SysFont("Verdana", 30)
    subtitle_text = subtitle_font.render("Press Enter to Start", True, BLACK)

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    return

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
        DISPLAYSURF.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 350))
        pygame.display.flip()
        FramePerSec.tick(FPS)


def game_over_screen(username):
    title_font = pygame.font.SysFont("Verdana", 80)
    title_text = title_font.render("Game Over", True, BLACK)
    subtitle_font = pygame.font.SysFont("Verdana", 30)
    subtitle_text = subtitle_font.render("Press Enter to try again", True, BLACK)

    characters = ["Player 1", "Player 2", "Player 3", "Player 4"]
    character_images = [pygame.transform.scale(pygame.image.load(f"../assets/images/player{i}.png"), (100, 100)) for i
                        in range(1, 5)]

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    character_selection_screen(username, DEFAULT_CHARACTER_IMAGE)  # Transition to Welcome Screen
                    return  # Exit the function after transitioning

        DISPLAYSURF.fill((255, 0, 0))
        DISPLAYSURF.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
        DISPLAYSURF.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 350))
        pygame.display.flip()
        FramePerSec.tick(FPS)


def winner_screen1(points):
    title_font = pygame.font.SysFont("Verdana", 80)
    title_text = title_font.render("Congratulations!", True, BLACK)
    subtitle_font = pygame.font.SysFont("Verdana", 30)
    subtitle_line1 = subtitle_font.render("You Passed Level 1! On to level 2", True, BLACK)
    subtitle_line2 = subtitle_font.render(f"Points: {points}", True, BLACK)

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    return

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))

        subtitle_line1_pos = (SCREEN_WIDTH // 2 - subtitle_line1.get_width() // 2, 350)
        subtitle_line2_pos = (
            SCREEN_WIDTH // 2 - subtitle_line2.get_width() // 2,
            subtitle_line1_pos[1] + subtitle_line1.get_height() + 10)

        DISPLAYSURF.blit(subtitle_line1, subtitle_line1_pos)
        DISPLAYSURF.blit(subtitle_line2, subtitle_line2_pos)

        pygame.display.flip()
        FramePerSec.tick(FPS)


def winner_screen2(points2):
    title_font = pygame.font.SysFont("Verdana", 80)
    title_text = title_font.render("Congratulations!", True, BLACK)
    subtitle_font = pygame.font.SysFont("Verdana", 30)
    subtitle_line1 = subtitle_font.render("You Passed Level 2! On to level 3", True, BLACK)
    subtitle_line2 = subtitle_font.render(f"Points: {points2}", True, BLACK)

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    return

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))

        subtitle_line1_pos = (SCREEN_WIDTH // 2 - subtitle_line1.get_width() // 2, 350)
        subtitle_line2_pos = (
            SCREEN_WIDTH // 2 - subtitle_line2.get_width() // 2,
            subtitle_line1_pos[1] + subtitle_line1.get_height() + 10)

        DISPLAYSURF.blit(subtitle_line1, subtitle_line1_pos)
        DISPLAYSURF.blit(subtitle_line2, subtitle_line2_pos)

        pygame.display.flip()
        FramePerSec.tick(FPS)


def winner_screen3(points3, username, DEFAULT_CHARACTER_IMAGE):
    title_font = pygame.font.SysFont("Verdana", 80)
    title_text = title_font.render("Congratulations!", True, BLACK)
    subtitle_font = pygame.font.SysFont("Verdana", 30)
    subtitle_line1 = subtitle_font.render("You are the Winner!", True, BLACK)
    subtitle_line2 = subtitle_font.render(f"Total Points: {points + points2 + points3}", True, BLACK)
    subttitle_line3 = subtitle_font.render("Press Enter to play again or press Esc to exit ", True, BLACK)

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    # Perform actions for pressing Enter (you can modify this part)
                    print("Enter key pressed")
                    character_selection_screen(username, DEFAULT_CHARACTER_IMAGE)
                elif game_event.key == K_ESCAPE:
                    # Perform actions for pressing Esc (you can modify this part)
                    pygame.quit()
                    sys.exit()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))

        subtitle_line1_pos = (SCREEN_WIDTH // 2 - subtitle_line1.get_width() // 2, 350)
        subtitle_line2_pos = (
            SCREEN_WIDTH // 2 - subtitle_line2.get_width() // 2,
            subtitle_line1_pos[1] + subtitle_line1.get_height() + 10)

        DISPLAYSURF.blit(subtitle_line1, subtitle_line1_pos)
        DISPLAYSURF.blit(subtitle_line2, subtitle_line2_pos)
        DISPLAYSURF.blit(subttitle_line3, (SCREEN_WIDTH // 2 - subttitle_line3.get_width() // 2, 450))

        pygame.display.flip()
        FramePerSec.tick(FPS)


DEFAULT_CHARACTER_IMAGE = pygame.transform.scale(pygame.image.load("../assets/images/player1.png"), (40, 50))


def character_selection_screen(username, DEFAULT_CHARACTER_IMAGE):
    characters = ["Player 1", "Player 2", "Player 3", "Player 4"]
    character_images = [pygame.transform.scale(pygame.image.load(f"../assets/images/player{i}.png"), (100, 100)) for i
                        in range(1, 5)]

    selected_index = 0
    selection_made = False
    time_elapsed = 0  # Initialize the time elapsed variable
    chosen_character_image = None  # Initialize as None

    while not selection_made:
        DISPLAYSURF.fill(WHITE)

        # Display character options
        for i, (character_name, character_image) in enumerate(zip(characters, character_images)):
            x_position = i * 200 + 50
            y_position = SCREEN_HEIGHT // 2 - 50

            # Highlight box for selected character
            if i == selected_index:
                pygame.draw.rect(DISPLAYSURF, BLACK, (x_position - 5, y_position - 5, 110, 110), 2)

            # Render character and its name
            character_text = pygame.font.SysFont("Verdana", 16).render(character_name, True, BLACK)
            text_rect = character_text.get_rect(midtop=(x_position + 55, y_position))  # Adjust text position
            DISPLAYSURF.blit(character_text, text_rect)
            DISPLAYSURF.blit(character_image, (x_position, y_position))

            # Display message
        message_text = pygame.font.SysFont("Verdana", 30).render("Select your Character", True, BLACK)
        DISPLAYSURF.blit(message_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 - 130))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(character_images)
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(character_images)
                elif event.key == pygame.K_RETURN:
                    # Character selected, exit loop and set chosen character
                    chosen_character_image = pygame.transform.scale(character_images[selected_index], (40, 50))
                    selection_made = True

        # Increment the time elapsed
        time_elapsed += 1

        # After 10 seconds, if no selection made, proceed with default character
        if time_elapsed >= 600:  # Assuming 60 frames per second, 600 frames = 10 seconds
            print("No character chosen. Selecting default character...")
            chosen_character_image = DEFAULT_CHARACTER_IMAGE
            selection_made = True

        # Proceed to the game with the chosen or default character after the loop
    level_one_screen(username, chosen_character_image)


def level_one_screen(username, chosen_character_image):
    global points
    TIME_LIMIT_LEVEL_ONE = 30  # Define the time limit for Level 1
    points = 0

    # Game loop
    start_time = pygame.time.get_ticks()
    game_over = False
    points = 30  # Initial points before Level 1 starts
    points_deducted_per_second = 1  # Deduct 1 point per second
    previous_elapsed_time_seconds = 0

    # Game setup
    background = pygame.image.load("../assets/images/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font_small = pygame.font.SysFont("Verdana", 20)

    P1 = Player(chosen_character_image)
    P1.set_character(chosen_character_image)

    # Instantiate enemy instances and resize their images
    E1 = EnemyOne()
    E1.image = pygame.image.load("../assets/images/E1.png")
    E1.image = pygame.transform.scale(E1.image, (60, 60))

    E2 = Enemytwo()
    E2.image = pygame.image.load("../assets/images/E2.png")
    E2.image = pygame.transform.scale(E2.image, (40, 30))

    E3 = Enemythree()
    E3.image = pygame.image.load("../assets/images/E3.png")
    E3.image = pygame.transform.scale(E3.image, (40, 30))

    E4 = Enemyfour()
    E4.image = pygame.image.load("../assets/images/E4.png")
    E4.image = pygame.transform.scale(E4.image, (50, 40))

    # Creating Sprites Groups
    enemies = pygame.sprite.Group()
    enemies.add([E1, E2, E3, E4])

    all_sprites = pygame.sprite.Group()
    all_sprites.add([P1, E1, E2, E3, E4])

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Update game logic
        for entity in all_sprites:
            entity.move()

        # Get current time in milliseconds
        current_time = pygame.time.get_ticks()
        elapsed_time_milliseconds = current_time - start_time  # Calculate elapsed time in milliseconds
        elapsed_time_seconds = elapsed_time_milliseconds // 1000  # Convert elapsed time to seconds

        # Deduct points based on time elapsed
        points_to_deduct = (elapsed_time_seconds - previous_elapsed_time_seconds) * points_deducted_per_second
        points -= points_to_deduct  # Deduct points
        previous_elapsed_time_seconds = elapsed_time_seconds  # Update previous elapsed time

        # Ensure points don't go negative
        points = max(points, 0)

        # Check for collisions or time limit reached (30 seconds)
        if pygame.sprite.spritecollideany(P1, enemies) or elapsed_time_seconds >= 30:
            game_background_sound.stop()  # Stop the background sound
            game_over_sound.play()  # Play the game over sound
            game_over = True
            game_over_screen(username)

        # Render everything
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(background, (0, 0))

        for entity in all_sprites:
            if isinstance(entity, Player):
                DISPLAYSURF.blit(entity.image, (entity.rect.x, entity.rect.y - 10))
            else:
                DISPLAYSURF.blit(entity.image, entity.rect)

        # Check if the character reaches the bottom of the screen
        if P1.rect.bottom >= SCREEN_HEIGHT:
            game_background_sound.stop()  # Stop the background sound
            level_passed_sound.play()  # Play the level passed sound
            # Get the user's current highest score for this level
            current_higher_score = db.get_user_higher_score(username, level=1)

            # Log the previous score before potentially updating it
            CustomLogger.log_updated_score(username, 1, current_higher_score)

            # Compare the new score with the current highest score
            if current_higher_score is None or points > current_higher_score:
                # Update the HigherScoreLevel1 for the user only if the new score is greater
                db.update_user_score(username, points, level=1)

            winner_screen1(points)
            level_two_screen(username, chosen_character_image)

        # Render countdown timer
        time_remaining = TIME_LIMIT_LEVEL_ONE - elapsed_time_seconds
        timer_text = font_small.render(f"Time: {time_remaining}", True, BLACK)
        DISPLAYSURF.blit(timer_text, (10, 10))

        # Render points on the screen
        points_text = font_small.render(f"Points: {points}", True, BLACK)
        points_rect = points_text.get_rect()
        points_rect.topright = (SCREEN_WIDTH - 10, 10)
        DISPLAYSURF.blit(points_text, points_rect)

        # Check if the character has completed the level
        if time_remaining <= 0:  # Check if time limit has been reached
            winner_screen1(points)  # Display winner screen for level 1
            return level_two_screen(chosen_character_image)

        pygame.display.update()
        FramePerSec.tick(FPS)


def level_two_screen(username, chosen_character_image):
    global points2
    TIME_LIMIT_LEVEL_TWO = 20
    points2 = 20  # Initial points before Level 2 starts

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    # Exit the result screen
                    return chosen_character_image

            DISPLAYSURF.fill(WHITE)
            pygame.display.flip()
            FramePerSec.tick(FPS)

        # Game setup
        background = pygame.image.load("../assets/images/background.png")
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        font_small = pygame.font.SysFont("Verdana", 20)

        P1 = Player(chosen_character_image)
        P1.set_character(chosen_character_image)

        # Instantiate enemy instances and resize their images
        E1 = EnemyOne()
        E1.image = pygame.image.load("../assets/images/E1.png")
        E1.image = pygame.transform.scale(E1.image, (60, 60))

        E2 = Enemytwo()
        E2.image = pygame.image.load("../assets/images/E2.png")
        E2.image = pygame.transform.scale(E2.image, (40, 30))

        E3 = Enemythree()
        E3.image = pygame.image.load("../assets/images/E3.png")
        E3.image = pygame.transform.scale(E3.image, (40, 30))

        E4 = Enemyfour()
        E4.image = pygame.image.load("../assets/images/E4.png")
        E4.image = pygame.transform.scale(E4.image, (50, 40))

        # Creating Sprites Groups
        enemies = pygame.sprite.Group()
        enemies.add([E1, E2, E3, E4])

        all_sprites = pygame.sprite.Group()
        all_sprites.add([P1, E1, E2, E3, E4])

        # Game loop
        start_time = pygame.time.get_ticks()
        game_over = False
        points_deducted_per_second = 1  # Deduct 1 point per second
        previous_elapsed_time_seconds = 0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            # Update game logic
            for entity in all_sprites:
                entity.move()

            # Get current time in milliseconds
            current_time = pygame.time.get_ticks()
            elapsed_time_milliseconds = current_time - start_time  # Calculate elapsed time in milliseconds
            elapsed_time_seconds = elapsed_time_milliseconds // 1000  # Convert elapsed time to seconds

            # Deduct points based on time elapsed
            points_to_deduct = (elapsed_time_seconds - previous_elapsed_time_seconds) * points_deducted_per_second
            points2 -= points_to_deduct  # Deduct points
            previous_elapsed_time_seconds = elapsed_time_seconds  # Update previous elapsed time

            # Ensure points don't go negative
            points2 = max(points2, 0)

            # Check for collisions or time limit reached (20 seconds)
            if pygame.sprite.spritecollideany(P1, enemies) or elapsed_time_seconds >= 20:
                game_background_sound.stop()  # Stop the background sound
                game_over_sound.play()  # Play the game over sound
                game_over = True
                game_over_screen(username)

            # Render everything
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(background, (0, 0))

            for entity in all_sprites:
                if isinstance(entity, Player):
                    DISPLAYSURF.blit(entity.image, (entity.rect.x, entity.rect.y - 10))
                else:
                    DISPLAYSURF.blit(entity.image, entity.rect)

            # Check if the character reaches the bottom of the screen
            if P1.rect.bottom >= SCREEN_HEIGHT:
                game_background_sound.stop()  # Stop the background sound
                level_passed_sound.play()  # Play the level passed sound
                current_higher_score = db.get_user_higher_score(username, level=2)

                # Log the previous score before potentially updating it
                CustomLogger.log_updated_score(username, 2, current_higher_score)

                if current_higher_score is None or points2 > current_higher_score:
                    # Update the HigherScoreLevel2 for the user only if the new score is greater
                    db.update_user_score(username, points2, level=2)

                winner_screen2(points2)
                level_three_screen(username, chosen_character_image)
                return points2

            # Render countdown timer
            time_remaining = TIME_LIMIT_LEVEL_TWO - elapsed_time_seconds
            timer_text = font_small.render(f"Time: {time_remaining}", True, BLACK)
            DISPLAYSURF.blit(timer_text, (10, 10))

            # Render points on the screen
            points_text = font_small.render(f"Points: {points2}", True, BLACK)
            points_rect = points_text.get_rect()
            points_rect.topright = (SCREEN_WIDTH - 10, 10)
            DISPLAYSURF.blit(points_text, points_rect)

            pygame.display.update()
            FramePerSec.tick(FPS)


def level_three_screen(username, chosen_character_image):
    global points3
    TIME_LIMIT_LEVEL_THREE = 10
    points3 = 10

    characters = ["Player 1", "Player 2", "Player 3", "Player 4"]
    character_images = [pygame.transform.scale(pygame.image.load(f"../assets/images/player{i}.png"), (100, 100)) for i
                        in range(1, 5)]

    while True:
        for game_event in pygame.event.get():
            if game_event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif game_event.type == KEYDOWN:
                if game_event.key == K_RETURN:
                    # Exit the result screen
                    return chosen_character_image

            DISPLAYSURF.fill(WHITE)
            pygame.display.flip()
            FramePerSec.tick(FPS)

        # Game setup
        background = pygame.image.load("../assets/images/background.png")
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        font_small = pygame.font.SysFont("Verdana", 20)

        P1 = Player(chosen_character_image)
        P1.set_character(chosen_character_image)

        # Instantiate enemy instances and resize their images
        E1 = EnemyOne()
        E1.image = pygame.image.load("../assets/images/E1.png")
        E1.image = pygame.transform.scale(E1.image, (60, 60))

        E2 = Enemytwo()
        E2.image = pygame.image.load("../assets/images/E2.png")
        E2.image = pygame.transform.scale(E2.image, (40, 30))

        E3 = Enemythree()
        E3.image = pygame.image.load("../assets/images/E3.png")
        E3.image = pygame.transform.scale(E3.image, (40, 30))

        E4 = Enemyfour()
        E4.image = pygame.image.load("../assets/images/E4.png")
        E4.image = pygame.transform.scale(E4.image, (50, 40))

        # Creating Sprites Groups
        enemies = pygame.sprite.Group()
        enemies.add([E1, E2, E3, E4])  # Changed to pass as an iterable (list or tuple)

        all_sprites = pygame.sprite.Group()
        all_sprites.add([P1, E1, E2, E3, E4])

        # Rest of the game loop
        start_time = pygame.time.get_ticks()
        game_over = False
        points_deducted_per_second = 1  # Deduct 1 point per second
        previous_elapsed_time_seconds = 0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            # Update game logic
            for entity in all_sprites:
                entity.move()

            # Get current time in milliseconds
            current_time = pygame.time.get_ticks()
            elapsed_time_milliseconds = current_time - start_time  # Calculate elapsed time in milliseconds
            elapsed_time_seconds = elapsed_time_milliseconds // 1000  # Convert elapsed time to seconds

            # Deduct points based on time elapsed
            points_to_deduct = (elapsed_time_seconds - previous_elapsed_time_seconds) * points_deducted_per_second
            points3 -= points_to_deduct  # Deduct points
            previous_elapsed_time_seconds = elapsed_time_seconds  # Update previous elapsed time

            # Ensure points don't go negative
            points3 = max(points3, 0)

            # Check for collisions or time limit reached (10 seconds)
            if pygame.sprite.spritecollideany(P1, enemies) or elapsed_time_seconds >= 10:
                game_over_sound.play()  # Play the game over sound
                game_over = True
                game_over_screen(username)

            # Render everything
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(background, (0, 0))

            for entity in all_sprites:
                if isinstance(entity, Player):
                    DISPLAYSURF.blit(entity.image, (entity.rect.x, entity.rect.y - 10))
                else:
                    DISPLAYSURF.blit(entity.image, entity.rect)

            # Check if the character reaches the bottom of the screen
            if P1.rect.bottom >= SCREEN_HEIGHT:
                winner_sound.play()  # Play the winner sound
                # Get the user's current highest score for this level
                current_higher_score = db.get_user_higher_score(username, level=3)

                # Log the previous score before potentially updating it
                CustomLogger.log_updated_score(username, 3, current_higher_score)

                # Compare the new score with the current highest score
                if current_higher_score is None or points3 > current_higher_score:
                    # Update the HigherScoreLevel3 for the user only if the new score is greater
                    db.update_user_score(username, points3, level=3)

                # Trigger the update for TotalHigherScore after all level scores are updated
                total_higher_score = db.get_total_higher_score(username)
                if total_higher_score is not None:
                    db.update_total_higher_score(username)
                    CustomLogger.log_updated_total_score(username, total_higher_score)

                winner_screen3(points3, username, DEFAULT_CHARACTER_IMAGE)
                character_selection_screen(username, characters)

            # Render countdown timer
            time_remaining = TIME_LIMIT_LEVEL_THREE - elapsed_time_seconds
            timer_text = font_small.render(f"Time: {time_remaining}", True, BLACK)
            DISPLAYSURF.blit(timer_text, (10, 10))

            # Render points on the screen
            points_text = font_small.render(f"Points: {points3}", True, BLACK)
            points_rect = points_text.get_rect()
            points_rect.topright = (SCREEN_WIDTH - 10, 10)
            DISPLAYSURF.blit(points_text, points_rect)

            pygame.display.update()
            FramePerSec.tick(FPS)

        welcome_screen()


def choose_action_screen():
    screen_text = font.render("Press 'R' to Register or 'L' to Login", True, BLACK)

    # Initialize flags for registration and login
    register_pressed = False
    login_pressed = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    register_pressed = True
                elif event.key == K_l:
                    login_pressed = True

        if register_pressed:
            registration_screen()
            return  # Exit the function after registration_screen() finishes
        elif login_pressed:
            login_screen()
            return  # Exit the function after login_screen() finishes

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(screen_text, (SCREEN_WIDTH // 2 - screen_text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.update()


def registration_screen():
    username = ""
    password = ""
    username_entered = False
    registered = False
    MIN_LENGTH = 6
    MAX_LENGTH = 12

    username_text = font.render("Username:", True, BLACK)
    password_text = font.render("Password:", True, BLACK)

    # Determine font sizes for username and password input
    input_font_size = 25

    while True:
        username_input_font = pygame.font.SysFont("Verdana", input_font_size)
        username_input = username_input_font.render(username, True, BLACK)
        password_input = username_input_font.render("*" * len(password), True, BLACK)
        input_width = max(username_input.get_width(), password_input.get_width())
        if input_width < 6:  # Adjust this value to fit the text comfortably inside the box
            break
        input_font_size -= 1

    # Centering the text and boxes on the screen
    username_box_x = SCREEN_WIDTH // 2 - 30
    password_box_x = SCREEN_WIDTH // 2 - 30
    register_button_x = SCREEN_WIDTH // 2 - 70
    input_y = SCREEN_HEIGHT // 2 - 60

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN and not username_entered:
                    username_entered = True  # Move to password input after entering username
                elif event.key == K_RETURN and username_entered:
                    # Move to the login screen after entering both username and password
                    # Store the user in the database
                    if db.register_user(username, password):
                        CustomLogger.log_registration(username, password)
                        login_screen()
                        registered = True
                        print("Registration successful!")

                if event.key == K_BACKSPACE:
                    if not username_entered:
                        username = username[:-1]
                    else:
                        password = password[:-1]
                elif event.key != K_RETURN:  # Ensure only the Enter key isn't registered for password input
                    if not username_entered:
                        username += event.unicode
                    else:
                        password += event.unicode

        if len(username) < MIN_LENGTH:
            username = username[:MIN_LENGTH]
        elif len(username) > MAX_LENGTH:
            username = username[:MAX_LENGTH]

        if len(password) < MIN_LENGTH:
            password = password[:MIN_LENGTH]
        elif len(password) > MAX_LENGTH:
            password = password[:MAX_LENGTH]

        DISPLAYSURF.fill(WHITE)

        # Render username box
        pygame.draw.rect(DISPLAYSURF, BLACK, (username_box_x, input_y, 200, 40), 2)
        DISPLAYSURF.blit(username_text, (username_box_x - 170, input_y))
        username_input = username_input_font.render(username, True, BLACK)
        DISPLAYSURF.blit(username_input, (username_box_x + 10, input_y + 5))

        # Render password box
        pygame.draw.rect(DISPLAYSURF, BLACK, (password_box_x, input_y + 50, 200, 40), 2)
        DISPLAYSURF.blit(password_text, (password_box_x - 165, input_y + 50))
        password_input = username_input_font.render("*" * len(password), True, BLACK)
        DISPLAYSURF.blit(password_input, (password_box_x + 10, input_y + 55))

        # Calculate the text size to center it properly
        text_width, text_height = font.size("Press Enter to Register")

        # Calculate the x position to center the text
        text_x = register_button_x + (144 - text_width) // 2

        # Calculate the y position
        text_y = input_y + 125 + (50 - text_height) // 2

        # Render the text
        register_button = font.render("Press Enter to Register", True, BLACK)

        # Adjust the highlight box dimensions based on the text size
        highlight_width = text_width + 20  # Adding some padding
        highlight_height = text_height + 10  # Adding some padding

        pygame.draw.rect(DISPLAYSURF, (100, 149, 237),
                         (text_x - 10, text_y - 5, highlight_width, highlight_height))  # Blue highlight
        DISPLAYSURF.blit(register_button, (text_x, text_y))

        pygame.display.update()


def login_screen():
    username = ""
    password = ""
    password_entered = False
    MIN_LENGTH = 6
    MAX_LENGTH = 12

    username_text = font.render("Username:", True, BLACK)
    password_text = font.render("Password:", True, BLACK)

    input_font_size = 25
    while True:
        username_input_font = pygame.font.SysFont("Verdana", input_font_size)
        username_input = username_input_font.render(username, True, BLACK)
        password_input = username_input_font.render("*" * len(password), True, BLACK)
        input_width = max(username_input.get_width(), password_input.get_width())
        if input_width < 180:
            break
        input_font_size -= 1

    # Centering the interface
    username_box_x = SCREEN_WIDTH // 2 - 30
    password_box_x = SCREEN_WIDTH // 2 - 30
    login_button_x = SCREEN_WIDTH // 2 - 50
    input_y = SCREEN_HEIGHT // 2 - 60

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN and not password_entered:
                    password_entered = True  # Move to password input after entering username
                elif event.key == K_RETURN and password_entered:
                    # Check login credentials and proceed to welcome_screen if successful
                    if db.login_user(username, password):
                        CustomLogger.log_login(username)  # Log successful login
                        character_selection_screen(username,
                                                   DEFAULT_CHARACTER_IMAGE)  # Go to character selection screen
                        print("Login successful!")

                if event.key == K_BACKSPACE:
                    if not password_entered:
                        username = username[:-1]
                    else:
                        password = password[:-1]
                elif event.key != K_RETURN:  # Ensure only the Enter key isn't registered for password input
                    if not password_entered:
                        username += event.unicode
                    else:
                        password += event.unicode

        if len(username) < MIN_LENGTH:
            username = username[:MIN_LENGTH]
        elif len(username) > MAX_LENGTH:
            username = username[:MAX_LENGTH]

        if len(password) < MIN_LENGTH:
            password = password[:MIN_LENGTH]
        elif len(password) > MAX_LENGTH:
            password = password[:MAX_LENGTH]

        DISPLAYSURF.fill(WHITE)

        pygame.draw.rect(DISPLAYSURF, BLACK, (username_box_x, input_y, 200, 40), 2)
        DISPLAYSURF.blit(username_text, (username_box_x - 170, input_y))
        username_input = username_input_font.render(username, True, BLACK)
        DISPLAYSURF.blit(username_input, (username_box_x + 10, input_y + 5))

        pygame.draw.rect(DISPLAYSURF, BLACK, (password_box_x, input_y + 50, 200, 40), 2)
        DISPLAYSURF.blit(password_text, (password_box_x - 165, input_y + 50))
        password_input = username_input_font.render("*" * len(password), True, BLACK)
        DISPLAYSURF.blit(password_input, (password_box_x + 10, input_y + 55))

        # Calculate the text size to center it properly
        text_width, text_height = font.size("Press Enter to Login")

        # Calculate the x position to center the text
        text_x = login_button_x + (100 - text_width) // 2

        # Calculate the y position to center the text
        text_y = input_y + 125 + (50 - text_height) // 2

        # Render the text
        login_button = font.render("Press Enter to Login", True, BLACK)

        # Adjust the highlight box dimensions based on the text size
        highlight_width = text_width + 20  # Adding some padding
        highlight_height = text_height + 10  # Adding some padding

        # Adjust the x and y positions for the highlight box to center it with the text
        highlight_x = login_button_x + (100 - highlight_width) // 2
        highlight_y = input_y + 125 + (50 - highlight_height) // 2

        pygame.draw.rect(DISPLAYSURF, (100, 149, 237),
                         (highlight_x, highlight_y, highlight_width, highlight_height))  # Blue highlight
        DISPLAYSURF.blit(login_button, (text_x, text_y))

        pygame.display.update()


def authentication_flow():
    background_sound = pygame.mixer.Sound("../assets/sounds/game_background_sound.wav")
    background_sound.set_volume(0.1)
    background_sound.play(-1)
    # Call the welcome screen function
    welcome_screen()

    # Run the authentication flow
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        action = choose_action_screen()

        if action == "register":
            registration_screen()
        elif action == "login":
            chosen_character_image = character_selection_screen(DEFAULT_CHARACTER_IMAGE)

            if chosen_character_image:
                level_one_screen(chosen_character_image)  # Pass chosen_character_image to start_game
            else:
                # Handle no character chosen scenario
                print("No character chosen!")
                time.sleep(10)  # Wait for 10 seconds
                chosen_character_image = DEFAULT_CHARACTER_IMAGE
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    authentication_flow()
