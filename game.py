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
        self.enemies = [
            Enemy(50, 600, 50, 50, 'assets/enemy.png', 3),
            Enemy(750, 400, 50, 50, 'assets/enemy.png', 3),
            Enemy(50, 200, 50, 50, 'assets/enemy.png', 3),
        ]

    def draw_objects(self):
        self.game_window.fill(self.color)
        self.game_window.blit(self.background_image.image, (self.background_image.x, self.background_image.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)


    def detect_collision(self, object):

        if object.y > (self.player.y + self.player.height) or self.player.y > (object.y + object.height):
            return False
        if object.x > (self.player.x + self.player.width) or self.player.x > (object.x + object.width):
            return False

        return True

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(enemy):
                return True

        if self.detect_collision(self.treasure):
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
            self.move_objects(player_direction)

            # update display
            self.draw_objects()

            if self.check_if_collided():
                return

            self.clock.tick(60)