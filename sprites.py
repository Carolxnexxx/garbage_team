from configuration import *
import pygame

global crash

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


        for sprite in puzzle_collide:
            if isinstance(sprite, (EarthP1, EarthP2, EarthP3)):
                sprite.kill()
                self.puzzle += 1
                print(f"Puzzle pieces collected: {self.puzzle}")
                if self.puzzle == 3:
                    self.display_winner_screen()
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
        
        for sprite in collide:
            for block in collide:
                if isinstance(block, House):
                    self.trivia_game.draw_question("House: Renewables & Recycling")
                elif isinstance(block, Factory):
                    self.trivia_game.draw_question("Factory: Greenhouse Gas Emissions & CO2 Emissions")
                elif isinstance(block, Fish):
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
    
    def display_winner_screen(self):
        font = pygame.font.SysFont('Arial', 80)
        text = font.render("You Won!", True, BLACK)
        self.game.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Update display and wait for 3 seconds
        pygame.display.flip()
        pygame.time.wait(3000)

        # After displaying the "You Won" screen, you can quit the game
        pygame.quit()



questions = {
    "Factory: Greenhouse Gas Emissions & CO2 Emissions": [
        {
            "question": "How many metric tons of CO2 were released, globally, in 2022?",
            "options": [
                "A) 65.43 billion",
                "B) 37.15 billion",
                "C) 103.23 billion",
                "D) 23.12 billion"
            ],
            "answer": 1  # Correct answer key
        },
        {
            "question": "Which of the following lists do NOT only contain greenhouse gases?",
            "options": [
                "A) Carbon dioxide (CO2), Methane (CH4), Nitrous Oxide (N2O), Water vapour (H2O)",
                "B) Carbon dioxide (CO2), Nitrous Oxide (N2O), Argon (Ar), Methane (CH4)",
                "C) Methane (CH4), Nitrous Oxide (N2O), Hydrofluorocarbons (HFCs), Nitrogen trifluoride (NF3)",
                "D) Hydrofluorocarbons (HFCs), Sulfur hexafluoride (SF6), Nitrous Oxide (N2O), Methane (CH4)"
            ],
            "answer": 2
        },
        {
            "question": "Where do hydrofluorocarbons (HFCs) come from?",
            "options": [
                "A) Refrigerators",
                "B) Air conditioners",
                "C) Insulating foams",
                "D) All of the above"
            ],
            "answer": 4
        }
    ],
    
    "House: Renewables & Recycling": [
        {
            "question": "What is biomass? What can it be used for?",
            "options": [
                "A) Biomass refers to organic material that comes from plants and animals that can be burned directly for heat or converted to liquid and gaseous fuels.",
                "B) Biomass is a fashion trend involving clothing made exclusively from recycled plastic.",
                "C) Biomass is a type of plastic used to make disposable utensils.",
                "D) Biomass refers to a method of creating electricity using solar panels."
            ],
            "answer": 1
        },
        {
            "question": "Choose the renewable energy source:",
            "options": [
                "A) Natural gas",
                "B) Nuclear energy",
                "C) Coal",
                "D) Biomass"
            ],
            "answer": 4
        },
        {
            "question": "Should you use renewable energy instead of non-renewable energy?",
            "options": [
                "A) ABSOLUTELY 100%",
                "B) No",
                "C) Too expensive; no.",
                "D) Ehhhh, maybe later."
            ],
            "answer": 1
        }
    ],
    
    "Fish: pH Levels of the Water, Declining Fish, Water and Climate Change": [
        {
            "question": "What is too high of a pH for coral to survive?",
            "options": [
                "A) 8.5",
                "B) 8.3",
                "C) 7.3",
                "D) 8.7"
            ],
            "answer": 1
        },
        {
            "question": "Why are wetlands, oceans, lakes and bodies of water important?",
            "options": [
                "A) Protecting and improving water quality",
                "B) Providing fish and wildlife with sufficient amounts of tomatoes",
                "C) Lakes are essential for providing Wi-Fi signals to nearby towns and cities.",
                "D) Lakes are essential for generating wind power by simply existing as large bodies of water."
            ],
            "answer": 1
        },
        {
            "question": "What are the consequences of rising sea levels?",
            "options": [
                "A) Saltwater Intrusion: Rising seas can cause saltwater to infiltrate freshwater aquifers, affecting drinking water supplies and agriculture.",
                "B) Decreased storms: Rising sea levels lead to decreased storm activity and milder weather overall.",
                "C) Increase in fish population: As sea levels rise, fish populations thrive due to increased water space.",
                "D) Agriculture boost: Rising sea levels will lead to an increase in land available for farming due to the flooding of urban areas."
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
        if category in questions:
            if self.current_question < len(questions):
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
            else:
                self.display_final_score(category)

    def wait_for_answer(self, category):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        selected_answer = event.key - pygame.K_0
                        if selected_answer == questions[category][self.current_question]["answer"]:
                            self.score += 1
                        self.current_question += 1
                        waiting = False
                        self.draw_question(category)


    def display_final_score(self):
        self.game.screen.fill(WHITE)
        score_text = self.font.render(f"Your Score: {self.score}/{len(questions)}", True, BLACK)
        self.game.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)