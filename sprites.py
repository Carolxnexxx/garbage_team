from configuration import *
import pygame

global crash
key = "none"
fishKey = False
houseKey = False
factoryKey = False

class Key1(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.key1_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Key2(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.key2_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Key3(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.key3_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

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

        self.image = self.game.terrain_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
class BombTree(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.bomb_tree_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def transform_to_fire(self):
        fire_image = self.game.fire_spritesheet.get_image(0, 0, self.width, self.height)  
        self.image = fire_image

class PineTree(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.pine_tree_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Garbage(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.garbage_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def transform_to_grass(self):
        grass_image = self.game.grass_spritesheet.get_image(0, 0, self.width, self.height)  
        self.image = grass_image

class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.house_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Factory(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.factory_spritesheet.get_image(img_x, img_y, self.width, self.height)

        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Fish(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        scale_factor = 2.5

        self.image = self.game.fish_spritesheet.get_image(img_x, img_y, self.width, self.height)

        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Wall(pygame.sprite.Sprite): # wall of the puzzle domains
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        # Load the ground image from the spritesheet using the provided coordinates
        self.image = self.game.wall_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class WaterDoor1(pygame.sprite.Sprite): # wall of the puzzle domains
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
        self.image = self.game.doorP1_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class IceDoor1(pygame.sprite.Sprite): # wall of the puzzle domains
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
        self.image = self.game.doorP2_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class WoodDoor1(pygame.sprite.Sprite): # wall of the puzzle domains
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
        self.image = self.game.doorP3_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class CastleFloor(pygame.sprite.Sprite):  # Wall of the puzzle domains
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.castlefloor_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class EarthP1(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = PLAYER_LAYER + 1  # Adjust layer to ensure visibility
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 90
        self.height = 80

        scale_factor = 1.5 # Adjust scale factor for better visibility

        self.image = self.game.earthP1_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class EarthP2(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = PLAYER_LAYER + 1
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 100
        self.height = 80

        scale_factor = 1.5 # Adjust scale factor for better visibility

        self.image = self.game.earthP2_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class EarthP3(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = PLAYER_LAYER + 1
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 100
        self.height = 100

        scale_factor = 1.5 # Adjust scale factor for better visibility

        self.image = self.game.earthP3_spritesheet.get_image(img_x, img_y, self.width, self.height)
        self.image = pygame.transform.scale(self.image, (self.width * scale_factor, self.height * scale_factor))

        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y, trivia_game):
        self.game = game
        self.trivia_game = trivia_game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.health_increased = False
        self.health_decreased = False

        self.puzzle = 0

        # Load the player image from the spritesheet using the provided coordinates
        self.image = self.game.player_spritesheet.get_image(0, 0, self.width, self.height)
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

        self.collide_block()

    def collide_block(self):
        pressed = pygame.key.get_pressed()
        
        # Check collision with 
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False, 
                                            pygame.sprite.collide_rect_ratio(0.85))  
        
        # Check collision with BombTree specifically
        bomb_tree_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                                        pygame.sprite.collide_rect_ratio(0.85))
        
        pine_tree_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                                        pygame.sprite.collide_rect_ratio(0.85))
    
        garbage_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                              pygame.sprite.collide_rect_ratio(0.85))
        
        puzzle_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                              pygame.sprite.collide_rect_ratio(0.85))
        
        door_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                              pygame.sprite.collide_rect_ratio(0.85))

        wall_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                              pygame.sprite.collide_rect_ratio(0.85))

        for sprite in wall_collide:
            if isinstance(sprite, Wall):
                if pressed[pygame.K_LEFT]:                    
                    self.rect.x += PLAYER_STEPS
                if pressed[pygame.K_RIGHT]:
                    self.rect.x -= PLAYER_STEPS
                if pressed[pygame.K_UP]:
                    self.rect.y += PLAYER_STEPS
                if pressed[pygame.K_DOWN]:
                    self.rect.y -= PLAYER_STEPS
                return

        for sprite in puzzle_collide:
            if isinstance(sprite, (EarthP1, EarthP2, EarthP3)):
                sprite.kill()
                self.puzzle += 1
                print(f"Puzzle pieces collected: {self.puzzle}")
                if self.puzzle == 3:
                    self.game.draw_win_screen()
                    print("YOU WIN")
                    return
                return

        for sprite in garbage_collide:
            if isinstance(sprite, Garbage):
                if not self.health_decreased:
                    sprite.transform_to_grass()
                    self.game.decrease_health()
                    self.health_decreased = True
                return  

        for sprite in bomb_tree_collide:
            if isinstance(sprite, BombTree):
                if not self.health_increased:  # Only increase health once per collision
                    sprite.transform_to_fire()  # Transform the tree into fire
                    self.game.increase_health()
                    self.health_increased = True
                if pressed[pygame.K_LEFT]:                    
                    self.rect.x += PLAYER_STEPS
                elif pressed[pygame.K_RIGHT]:
                    self.rect.x -= PLAYER_STEPS
                elif pressed[pygame.K_UP]:
                    self.rect.y += PLAYER_STEPS
                elif pressed[pygame.K_DOWN]:
                    self.rect.y -= PLAYER_STEPS
                return  # Exit after processing the collision
        self.health_increased = False
        self.health_decreased = False
        
        for sprite in pine_tree_collide:
            if isinstance(sprite, PineTree):
                if pressed[pygame.K_LEFT]:                    
                    self.rect.x += PLAYER_STEPS
                elif pressed[pygame.K_RIGHT]:
                    self.rect.x -= PLAYER_STEPS
                elif pressed[pygame.K_UP]:
                    self.rect.y += PLAYER_STEPS
                elif pressed[pygame.K_DOWN]:
                    self.rect.y -= PLAYER_STEPS
                return  # Exit after processing the collision
        
        for sprite in door_collide:
            if isinstance(sprite, WaterDoor1):
                
                if fishKey == False:
                    if pressed[pygame.K_LEFT]:                    
                        self.rect.x += PLAYER_STEPS
                    elif pressed[pygame.K_RIGHT]:
                        self.rect.x -= PLAYER_STEPS
                    elif pressed[pygame.K_UP]:
                        self.rect.y += PLAYER_STEPS
                    elif pressed[pygame.K_DOWN]:
                        self.rect.y -= PLAYER_STEPS
                    return

            elif isinstance(sprite, IceDoor1):
                
                if factoryKey == False:
                    if pressed[pygame.K_LEFT]:                    
                        self.rect.x += PLAYER_STEPS
                    elif pressed[pygame.K_RIGHT]:
                        self.rect.x -= PLAYER_STEPS
                    elif pressed[pygame.K_UP]:
                        self.rect.y += PLAYER_STEPS
                    elif pressed[pygame.K_DOWN]:
                        self.rect.y -= PLAYER_STEPS
                    return
                
            elif isinstance(sprite, WoodDoor1):
                
                if houseKey == False:
                    if pressed[pygame.K_LEFT]:                    
                        self.rect.x += PLAYER_STEPS
                    elif pressed[pygame.K_RIGHT]:
                        self.rect.x -= PLAYER_STEPS
                    elif pressed[pygame.K_UP]:
                        self.rect.y += PLAYER_STEPS
                    elif pressed[pygame.K_DOWN]:
                        self.rect.y -= PLAYER_STEPS
                    return 
                
        
        for sprite in collide:
            for block in collide:
                if isinstance(block, House):
                    print("trivia house")
                    self.trivia_game.draw_question("House: Renewables & Recycling")
                elif isinstance(block, Factory):
                    print("trivia factory")
                    self.trivia_game.draw_question("Factory: Greenhouse Gas Emissions & CO2 Emissions")
                elif isinstance(block, Fish):
                    print("trivia fish")
                    self.trivia_game.draw_question("Fish: pH Levels of the Water, Declining Fish, Water and Climate Change")
            
            if pressed[pygame.K_LEFT]:                    
                self.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
            return 
    

questions = {
    "Factory: Greenhouse Gas Emissions & CO2 Emissions": [
        {
            "question": "How many metric tons of CO2 were released, globally, in 2022?",
            "options": [
                "1) 65.43 billion",
                "2) 37.15 billion",
                "3) 103.23 billion",
                "4) 23.12 billion"
            ],
            "answer": 2  # Correct answer key
        },
        {
            "question": "Which of the following lists do NOT only contain greenhouse gases?",
            "options": [
                "1) CO2, CH4, N2O, H2O",
                "2) CO2, N2O, Ar, CH4",
                "3) CH4, N2O, HFCs, NF3",
                "4) HFCs, SF6, N2O, CH4"
            ],
            "answer": 2
        },
        {
            "question": "Where do hydrofluorocarbons (HFCs) come from?",
            "options": [
                "1) Refrigerators",
                "2) Air conditioners",
                "3) Insulating foams",
                "4) All of the above"
            ],
            "answer": 4
        }
    ],
    
    "House: Renewables & Recycling": [
        {
            "question": "What is biomass? What can it be used for?",
            "options": [
                "1) Organic material from plants and animals that can be burned for heat or converted to liquid and gaseous fuels.",
                "2) Biomass is a fashion trend involving clothing made exclusively from recycled plastic.",
                "3) Biomass is a type of plastic used to make disposable utensils.",
                "4) Biomass refers to a method of creating electricity using solar panels."
            ],
            "answer": 1
        },
        {
            "question": "Choose the renewable energy source:",
            "options": [
                "1) Natural gas",
                "2) Nuclear energy",
                "3) Coal",
                "4) Biomass"
            ],
            "answer": 4
        },
        {
            "question": "Should you use renewable energy instead of non-renewable energy?",
            "options": [
                "1) ABSOLUTELY 100%",
                "2) No",
                "3) Too expensive; no.",
                "4) Ehhhh, maybe later."
            ],
            "answer": 1
        }
    ],
    
    "Fish: pH Levels of the Water, Declining Fish, Water and Climate Change": [
        {
            "question": "What is too high of a pH for coral to survive?",
            "options": [
                "1) 8.5",
                "2) 8.3",
                "3) 7.3",
                "4) 8.7"
            ],
            "answer": 4
        },
        {
            "question": "Why are wetlands, oceans, lakes and bodies of water important?",
            "options": [
                "1) Protecting and improving water quality",
                "2) Providing fish and wildlife with sufficient amounts of tomatoes",
                "3) Lakes are essential for providing Wi-Fi signals to nearby towns and cities.",
                "4) Lakes are essential for generating wind power by simply existing as large bodies of water."
            ],
            "answer": 1
        },
        {
            "question": "What are the consequences of rising sea levels?",
            "options": [
                "1) Saltwater Intrusion",
                "2) Decreased storms",
                "3) Increase in fish population",
                "4) Agriculture boost"
            ],
            "answer": 1
        }
    ]
}

FONT_SIZE = 30
WIDTH, HEIGHT = 800, 600

class TriviaGame:
    def __init__(self, game):
        self.game = game
        self.current_question = 0
        self.score = 0
        self.initial_font_size = FONT_SIZE
        self.font = pygame.font.SysFont('Arial', self.initial_font_size)
    
    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + ' '
            width, _ = font.size(test_line)

            if width <= max_width:
                current_line = test_line  # If it fits, add the word
            else:
                lines.append(current_line.strip())
                current_line = word + ' '
        if current_line:
            lines.append(current_line.strip())

        return lines

    def adjust_font(self, text, max_width):
        font_size = self.initial_font_size
        
        wrapped_text = []

        while font_size > 10:  # Set a minimum font size
            font = pygame.font.SysFont('Arial', font_size)
            wrapped_text = self.wrap_text(text, font, max_width)
        
        # Check if the total height of the wrapped text fits in the surface height
            total_height = sum(font.get_height() for _ in wrapped_text)

            if total_height <= 450:  # Check against your surface height
                return font, wrapped_text  # Return the fitting font and wrapped text
            font_size -= 1  # Decrease font size
            
        return pygame.font.SysFont('Arial', 10), self.wrap_text(text, pygame.font.SysFont('Arial', 10), max_width)
            
    
    def draw_question(self, category):
        global key
        print(key)
        if category in questions:
            print("Category in questions")
            print(category)
            if category == "Fish: pH Levels of the Water, Declining Fish, Water and Climate Change":
                key = "fish"
                print("yess",key)
            elif category == "Factory: Greenhouse Gas Emissions & CO2 Emissions":
                key = "factory"
                print("yess",key)
            elif category == "House: Renewables & Recycling":
                key = "house"
                print("yess",key)
            if self.current_question < len(questions):
                print("self current question < len quesitons")
                print(self.current_question)
                question_data = questions[category][self.current_question]

                quiz_surface = pygame.Surface((640, 480))  
                quiz_surface.fill(WHITE)
                self.game.screen.blit(quiz_surface, (100, 60))  # Position the quiz box

            # Render the question
                question_font, wrapped_question = self.adjust_font(question_data["question"], 600)
                y_offset = 120

                for line in wrapped_question:
                    question_text = question_font.render(line, True, BLACK)
                    question_rect = question_text.get_rect(center=(400, y_offset))  # Center the line
                    self.game.screen.blit(question_text, question_rect)
                    y_offset += question_font.get_height()  # Move down for the next line

            # Render the options
                option_y = y_offset + 20  # Start options below the question
                for i, option in enumerate(question_data["options"]):
                    option_font, wrapped_option = self.adjust_font(option, 550)

                    for line in wrapped_option:
                        option_text = option_font.render(line, True, BLACK)
                        option_rect = option_text.get_rect(topleft=(120, option_y))  # Adjust the y-position
                        self.game.screen.blit(option_text, option_rect)
                        option_y += option_font.get_height()  # Move down for the next line

                pygame.display.flip()
                self.wait_for_answer(category)
            # else:
            #     self.display_final_score()
            #     print("display score 1")

    def wait_for_answer(self, category):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        selected_answer = event.key - pygame.K_0
                        correct_answer = questions[category][self.current_question]["answer"]

                        if selected_answer == correct_answer:
                            self.score += 1
                            feedback_text = "Correct!"
                        else:
                            feedback_text = "Incorrect, Correct answer is number " + str(correct_answer)
                                

                        self.display_feedback(feedback_text)  # Display feedback

                        # Increment question only if there are more questions
                        self.current_question += 1
                        if self.current_question < len(questions[category]):
                            self.draw_question(category)
                        else:
                            self.display_final_score()
                            print("display score 2")
                            self.current_question = 0

                    waiting = False       
    
    def display_feedback(self, feedback_text):
        feedback_area = pygame.Surface((6, 45))  # Adjust size based on your needs
        feedback_area.fill(WHITE)  # Fill with the background color
        self.game.screen.blit(feedback_area, (100, 300))  # Position the feedback area

        feedback_font = pygame.font.SysFont('Arial', 30)
        feedback_surface = feedback_font.render(feedback_text, True, BLACK)
        feedback_rect = feedback_surface.get_rect(center=(400, 80))  # Center in the feedback area
        self.game.screen.blit(feedback_surface, feedback_rect)

        pygame.display.flip()  # Update the display
        pygame.time.wait(1000)


    def display_final_score(self):
        global fishKey
        global houseKey
        global factoryKey
        if self.score == 3:
            print("KEY UNLOCKED:",key)
            if key == "fish":
                print("key is fish")
                fishKey = True
            elif key == "house":
                print("key is house")
                houseKey = True
            elif key == "factory":
                print("key is factory")
                factoryKey = True
        else:
            print("try again")
        quiz_surface = pygame.Surface((640, 480))
        quiz_surface.fill(WHITE) 
        self.game.screen.blit(quiz_surface, (100, 60))
        score_text = self.font.render(f"Your Score: {self.score}/{len(questions)}", True, BLACK)
        self.game.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        self.score = 0
        pygame.time.wait(3000)