import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.color = (0, 0, 0)
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.background_image = GameObject(0, 0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 3)
        self.enemy = Enemy(50, 600, 50, 50, 'assets/enemy.png', 3)

    def draw_objects(self):
        self.game_window.fill(self.color)
        self.game_window.blit(self.background_image.image, (self.background_image.x, self.background_image.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
        pygame.display.update()

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height) or object_2.y > (object_1.y + object_1.height):
            return False
        if object_1.x > (object_2.x + object_2.width) or object_2.x > (object_1.x + object_1.width):
            return False

        return True


    def run_game_loop(self):
        player_direction = 0

        while True:

            # handle event
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            # execute logic

            self.player.move(player_direction, self.height)
            self.enemy.move(self.width)
            # update display
            self.draw_objects()

            if self.detect_collision(self.player, self.enemy):
                return
            elif self.detect_collision(self.player, self.treasure):
                return

            self.clock.tick(60)