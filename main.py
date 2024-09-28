from configuration import *
import sys
import pygame
from sprites import *

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert_alpha()
    def get_image(self, x,y, width, height):
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)  # Allows transparency
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK) 
        
        return sprite

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png') 
        self.house_spritesheet = Spritesheet('assets/images/house.png') 
        self.player_spritesheet = Spritesheet('assets/images/player.png') 
        self.running = True

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "G":
                    Block(self, j, i, 0, 0)  # Grass block
                elif column == "W":
                    Block(self, j, i, 22, 0)  # Water block
                elif column == "I":
                    Block(self, j, i, 44, 0)  # Ice block
                elif column == "D":
                    Block(self, j, i, 66, 0) # Dirt block
                elif column == "S":
                    Block(self, j, i, 90, 0)  # Sand block
                elif column == "H":
                    House(self, j, i, 18, 12)
                elif column == "P":
                    self.player = Player(self,j,i)
            
    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.createTileMap()
    
    def update(self):
        self.all_sprites.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw(self):
        self.screen.fill(BLACK) 
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()
