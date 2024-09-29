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

class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_x, img_y):
        self.game = game
        self._layer = HOUSE_LAYER
        self.groups = self.game.all_sprites
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
        self.groups = self.game.all_sprites
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
        self.groups = self.game.all_sprites
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
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 150
        self.height = 150

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
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 150
        self.height = 150

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
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 150
        self.height = 150

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

        self.x = x * 30
        self.y = y * 30

        self.width = 30
        self.height = 30

        self.x_change = 0
        self.y_change = 0

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
        
        # Check collision with blocks
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False, 
                                            pygame.sprite.collide_rect_ratio(0.85))  
        
        # Check collision with BombTree specifically
        bomb_tree_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                                        pygame.sprite.collide_rect_ratio(0.85))
        
        pine_tree_collide = pygame.sprite.spritecollide(self, self.game.all_sprites, False, 
                                                        pygame.sprite.collide_rect_ratio(0.85))

        for sprite in bomb_tree_collide:
            if isinstance(sprite, BombTree):
                sprite.transform_to_fire()  # Transform the tree into fire

                if pressed[pygame.K_LEFT]:                    
                    self.rect.x += PLAYER_STEPS
                elif pressed[pygame.K_RIGHT]:
                    self.rect.x -= PLAYER_STEPS
                elif pressed[pygame.K_UP]:
                    self.rect.y += PLAYER_STEPS
                elif pressed[pygame.K_DOWN]:
                    self.rect.y -= PLAYER_STEPS
                return  # Exit after processing the collision
        
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
            self.game.increase_health()
            self.trivia_game.draw_question()  # Call the trivia game
            
            # Prevent player from moving into the bomb tree
            if pressed[pygame.K_LEFT]:                    
                self.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
            return  # Exit after processing the collision




questions = [
    {
        "question": "Choose a renewable energy source:",
        "options": [
            "1. Natural gas",
            "2. Nuclear",
            "3. Coal",
            "4. Hydro electricity"
        ],
        "answer": 4
    },
    {
        "question": "How many tonnes of CO2 are emitted per year?",
        "options": [
            "1. 34 billion",
            "2. 100 million",
            "3. 63 billion",
            "4. 21 billion"
        ],
        "answer": 1
    },
    {
        "question": "The answer is 1",
        "options": [""],
        "answer": 1
    }
]
FONT_SIZE = 40
WIDTH, HEIGHT = 800, 600

class TriviaGame:
    def __init__(self, game):
        self.game = game
        self.current_question = 0
        self.score = 0
        self.font = pygame.font.SysFont('Arial', FONT_SIZE)

    def draw_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.game.screen.fill(WHITE)
            question_text = self.font.render(question_data["question"], True, BLACK)
            self.game.screen.blit(question_text, (50, 50))

            for i, option in enumerate(question_data["options"]):
                option_text = self.font.render(option, True, BLACK)
                self.game.screen.blit(option_text, (50, 150 + i * 50))

            pygame.display.flip()
            self.wait_for_answer()
        else:
            self.display_final_score()

    def wait_for_answer(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        selected_answer = event.key - pygame.K_0
                        if selected_answer == questions[self.current_question]["answer"]:
                            self.score += 1
                        self.current_question += 1
                        waiting = False
                        self.draw_question()  # Redraw the question or move to final score if done

    def display_final_score(self):
        self.game.screen.fill(WHITE)
        score_text = self.font.render(f"Your Score: {self.score}/{len(questions)}", True, BLACK)
        self.game.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)