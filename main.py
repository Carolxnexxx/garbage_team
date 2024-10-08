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
        self.earthP2_spritesheet = Spritesheet('assets/images/earthP2.png')
        self.earthP3_spritesheet = Spritesheet('assets/images/earthP3.png')
        self.fish_spritesheet = Spritesheet('assets/images/fish.png')
        self.bomb_tree_spritesheet = Spritesheet('assets/images/bomb_tree.png')
        self.pine_tree_spritesheet = Spritesheet('assets/images/pine_tree.png')
        self.garbage_spritesheet = Spritesheet('assets/images/garbage.png')
        self.grass_spritesheet = Spritesheet('assets/images/grass.png')
        self.fire_spritesheet = Spritesheet('assets/images/fire.png')  # Load fire image
        self.key1_spritesheet = Spritesheet('assets/images/key1.png')
        self.key2_spritesheet = Spritesheet('assets/images/key2.png')
        self.key3_spritesheet = Spritesheet('assets/images/key3.png')

        self.running = True
        self.trivia_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT)) 
        self.trivia_game = TriviaGame(self) 

        # Temperature/health Bar
        self.health_bar_height = 10  # Initial temperature
        self.health_bar_max_height = 70  # Max height of the health bar
        self.health_bar_width = 15  # Width of the health bar
        self.health_bar_x = WIN_WIDTH - 50  # Position of the bar (right side of the screen)
        self.health_bar_y = 20  # Y position based on max height

        self.state = "start_screen" 

    def increase_health(self):
        if self.health_bar_height + 10 <= self.health_bar_max_height:
            self.health_bar_height += 10
        else:
            self.health_bar_height = self.health_bar_max_height

    def decrease_health(self):
        if self.health_bar_height -5 <= self.health_bar_max_height:
            self.health_bar_height -= 5
        else:
            self.health_bar_height = 0   


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
                elif column == "R":
                    Garbage(self, j, i, 0, 0)
                elif column == "6":
                    self.player = Player(self, j, i, 0, 0, self.trivia_game)

        self.key1 = Key1(self, 0, 0.5, 0, 0)
        self.key2 = Key2(self, 38, 4, 0, 0)
        self.key3 = Key3(self, 38, 20, 0, 0)
        self.house = House(self, 7, 15, 0, 0)
        self.factory = Factory(self, 18, 20, 0, 0)
        self.fish = Fish(self, 22, 10, 0, 0)
        self.earthP1 = EarthP1(self, 1, 1, 0, 0)
        self.earthP2 = EarthP2(self, 32, 6, 0, 0)
        self.earthP3 = EarthP3(self, 31, 21, 0, 0)
                
            
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
            if self.state == "start_screen":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.state = "lore_screen"
            elif self.state == "lore_screen":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.state = "main_game" 
            elif self.state == "end_screen":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.health_bar_height = 10
                    self.state = "main_game"

    def draw_start_screen(self):
        game_over_image = pygame.image.load("assets/images/start.png")
        game_over_image = pygame.transform.scale(game_over_image, (WIN_WIDTH, WIN_HEIGHT))
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()

    def draw_lore_screen(self):
        game_over_image = pygame.image.load("assets/images/lore.png")
        game_over_image = pygame.transform.scale(game_over_image, (WIN_WIDTH, WIN_HEIGHT))
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()
    
    def draw_end_screen(self):
        game_over_image = pygame.image.load("assets/images/gameover.png")
        game_over_image = pygame.transform.scale(game_over_image, (WIN_WIDTH, WIN_HEIGHT))
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()

    def draw_win_screen(self):
        game_over_image = pygame.image.load("assets/images/winner.png")
        game_over_image = pygame.transform.scale(game_over_image, (WIN_WIDTH, WIN_HEIGHT))
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(7000)
        pygame.quit()

    def draw(self):
        self.screen.fill(RED) 
        self.all_sprites.draw(self.screen)

        # Temperature/Health bar
        pygame.draw.rect(self.screen, WHITE, (self.health_bar_x, self.health_bar_y, self.health_bar_width, self.health_bar_max_height))
        fill_y = self.health_bar_y + (self.health_bar_max_height - self.health_bar_height)
        pygame.draw.rect(self.screen, RED, (self.health_bar_x, fill_y, self.health_bar_width, self.health_bar_height))

        # Game Over
        if self.health_bar_height >= self.health_bar_max_height:
            self.state = "end_screen"
            # print("Game Over")
            # self.running = False

        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        while self.running:
            self.events()
            if self.state == "start_screen":
                self.draw_start_screen()  # Show start screen
            elif self.state == "lore_screen":
                self.draw_lore_screen()
            elif self.state == "main_game":
                self.update()
                self.draw()
            elif self.state == "end_screen":
                self.draw_end_screen()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()
