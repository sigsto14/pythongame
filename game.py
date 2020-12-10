import pygame

class Game:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.color = (0, 0, 0)
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load('assets/background.png')
        self.background_image = pygame.transform.scale(background_image, (self.width, self.height))
        treasure = pygame.image.load('assets/treasure.png')
        self.treasure = pygame.transform.scale(treasure, (50, 50))

    def draw_objects(self):
        self.game_window.fill(self.color)
        self.game_window.blit(self.background_image, (0, 0))
        self.game_window.blit(self.treasure, (375, 50))
        pygame.display.update()

    def run_game_loop(self):
        while True:

            # handle event
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    return

            # execute logic 
            # update display
            self.draw_objects()

            self.clock.tick(60)