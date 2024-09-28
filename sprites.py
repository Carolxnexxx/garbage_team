from configuration import *
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        # Load the block image from the spritesheet using the provided coordinates
        self.image = self.game.terrain_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        # Load the ground image from the spritesheet using the provided coordinates
        self.image = self.game.terrain_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        # Load the ground image from the spritesheet using the provided coordinates
        self.image = self.game.house_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * 30
        self.y = y * 30

        self.width = 30
        self.height = 30

        self.x_change = 0
        self.y_change = 0

        # Load the player image from the spritesheet using the provided coordinates
        self.image = self.game.player_spritesheet.get_image(0, 10, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        pressed = pygame.key.get_pressed()

        self.x_change = 0  # Reset x and y changes before calculating new movement
        self.y_change = 0

        if pressed[pygame.K_LEFT]:
            self.x_change = -PLAYER_STEPS  # Move left
        if pressed[pygame.K_RIGHT]:
            self.x_change = PLAYER_STEPS  # Move right
        if pressed[pygame.K_UP]:
            self.y_change = -PLAYER_STEPS  # Move up
        if pressed[pygame.K_DOWN]:
            self.y_change = PLAYER_STEPS  # Move down

    def update(self):
        self.move()

        # Apply the movement to the player's position
        self.rect.x += self.x_change  # Apply horizontal movement
        self.rect.y += self.y_change  # Apply vertical movement

        # Reset changes after each update
        self.x_change = 0
        self.y_change = 0

        