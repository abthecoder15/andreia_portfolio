import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    def __init__(self, character_images):
        super().__init__()
        SPEED = 4
        self.character_images = character_images
        character_images = pygame.transform.scale(character_images, (10, 10))
        self.image_index = 0
        self.current_direction = "right"  # Initializing direction to start with
        self.speed = SPEED  # Assuming SPEED is defined globally

    def set_character(self, character):
        self.image = character
        self.rect = self.image.get_rect()
        self.rect.center = (20, 120)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.current_direction = "left"
        elif pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.current_direction = "right"
        elif pressed_keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.current_direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.current_direction = "down"


class EnemyOne(pygame.sprite.Sprite):
    SPEED = 3
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/E1.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.width = 10
        self.rect.height = 10
        self.reset()

    SCREEN_WIDTH = 800  # Replace with the actual screen width value

    def move(self):
        SPEED = 4
        self.rect.move_ip(SPEED, 0)  # Move horizontally to the right
        if self.rect.right > SCREEN_WIDTH:
            self.reset()

    def reset(self):
        # Reset x-coordinate and set to a new starting position on the y-axis
        self.rect.left = 0
        self.rect.centery = 271

class Enemytwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/E2.png")
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()
        self.reset()

    def move(self):
        SPEED = 4
        self.rect.move_ip(SPEED, 0)  # Move horizontally to the right
        if self.rect.right > SCREEN_WIDTH:
            self.reset()

    def reset(self):
        # Reset x-coordinate and set to a new starting position on the y-axis
        self.rect.left = 0
        self.rect.centery = 200

class Enemythree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/E3.png")
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()
        self.reset()

    def move(self):
        SPEED = 2.7
        self.rect.move_ip(SPEED, 0)  # Move horizontally to the right
        if self.rect.right > SCREEN_WIDTH:
            self.reset()

    def reset(self):
        # Reset x-coordinate and set to a new starting position on the y-axis
        self.rect.left = 0
        self.rect.centery = 385


class Enemyfour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/E4.png")
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.reset()

    def move(self):
        SPEED = 4.5
        self.rect.move_ip(SPEED, 0)  # Move horizontally to the right
        if self.rect.right > SCREEN_WIDTH:
            self.reset()

    def reset(self):
        # Reset x-coordinate and set to a new starting position on the y-axis
        self.rect.left = 0
        self.rect.centery = 480