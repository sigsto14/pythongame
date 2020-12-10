import pygame

pygame.init()

width = 800
height = 800
color = (204, 153, 255)
game_window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def run_game_loop():
    while True:

        # handle event
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                return


        # execute logic 
        # update display
        game_window.fill(color)
        pygame.display.update()

        clock.tick(60)

run_game_loop()
pygame.quit()
quit()