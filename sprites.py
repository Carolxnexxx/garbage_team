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
    def init(self,game,x,y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change= 0
        self.y_change= 0

        self.image = self.image.load()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.x_change = self.x_change - STEPS
        if pressed[pygame.K_RIGHT]:
            self.x_change = self.x_change + STEPS
        if pressed[pygame.K_UP]:
            self.y_change = self.y_change - STEPS
        if pressed[pygame.K_DOWN]:
            self.y_change = self.y_change + STEPS

    def update(self):
        self.move()
        self.collide()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        self.rect.x = 0
        self.rect.y = 0

    def collide(self):
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self,self.game.blocks, False, pygame.sprite.collide_rect_ratio(0.5))
        if collide:
            self.game.block.collide = True
            if pressed[pygame.K_LEFT]:
                self.x_change = self.x_change + STEPS
            if pressed[pygame.K_RIGHT]:
                self.x_change = self.x_change - STEPS
            if pressed[pygame.K_UP]:
                self.y_change = self.y_change + STEPS
            if pressed[pygame.K_DOWN]:
                self.y_change = self.y_change - STEPS