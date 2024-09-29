from configuration import *
import sys
import pygame
from sprites import *
pygame.font.init()

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert_alpha()
    def get_image(self, x,y, width, height):
        sprite = pygame.Surface([width, height], pygame.SRCALPHA)  # Allows transparency
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(RED) 
        
        return sprite

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png') 
        self.house_spritesheet = Spritesheet('assets/images/house.png') 
        self.fish_spritesheet = Spritesheet('assets/images/fish.png') 
        self.wall_spritesheet = Spritesheet('assets/images/wall.png') 
        self.doorP1_spritesheet = Spritesheet('assets/images/doorP1.png') 
        self.doorP2_spritesheet = Spritesheet('assets/images/doorP2.png') 
        self.doorP3_spritesheet = Spritesheet('assets/images/doorP3.png') 
        self.earthP1_spritesheet = Spritesheet('assets/images/earthP1.png')
        self.earthP2_spritesheet = Spritesheet('assets/images/earthP2.png')
        self.earthP3_spritesheet = Spritesheet('assets/images/earthP3.png')
        self.player_spritesheet = Spritesheet('assets/images/player.png') 
        self.castlefloor_spritesheet = Spritesheet('assets/images/castlefloor.png') 
        self.factory_spritesheet = Spritesheet('assets/images/factory.png')
        self.bomb_tree_spritesheet = Spritesheet('assets/images/bomb_tree.png')
        self.pine_tree_spritesheet = Spritesheet('assets/images/pine_tree.png')
        self.fire_spritesheet = Spritesheet('assets/images/fire.png')  # Load fire image
        self.running = True
        self.trivia_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT)) 
        self.trivia_game = TriviaGame(self) 

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "G":
                    Ground(self, j, i, 0, 0)  # Grass block
                elif column == "W":
                    Block(self, j, i, 22, 0)  # Water block
                elif column == "I":
                    Block(self, j, i, 44, 0)  # Ice block
                elif column == "D":
                    Ground(self, j, i, 66, 0) # Dirt block
                elif column == "S":
                    Ground(self, j, i, 90, 0)  # Sand block
                elif column == "A":
                    Wall(self, j, i, 0, 0)
                elif column == "1":
                    WaterDoor1(self, j, i, 0, 0)
                elif column == "2":
                    IceDoor1(self, j, i, 0, 0)
                elif column == "3":
                    WoodDoor1(self, j, i, 0, 0)
                elif column == "C":
                    CastleFloor(self, j, i,0,0)
                elif column == "B":
                    BombTree(self, j, i, 0, 0)
                elif column == "T":
                    PineTree(self, j, i, 0, 0)
                elif column == "P":
                    self.player = Player(self, j, i, 0, 0, self.trivia_game)

        
        self.house = House(self, 7, 15, 0, 0)
        self.factory = Factory(self, 18, 20, 0, 0)
        self.fish = Fish(self, 22, 10, 0, 0)
        self.earthP1 = EarthP1(self, 1, 1, 40, 40)
        self.earthP2 = EarthP2(self, 32, 2, 40, 40)
        self.earthP3 = EarthP3(self, 28, 21, 40, 40)
                
            
    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() # important for collision
        self.createTileMap()
    
    def update(self):
        self.all_sprites.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw(self):
        self.screen.fill(RED) 
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
