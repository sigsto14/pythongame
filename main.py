import pygame

pygame.init()

width = 800
height = 800
color = (0, 0, 0)
game_window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

background_image = pygame.transform.scale(pygame.image.load('assets/background.png'), (width, height))
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
        game_window.blit(background_image, (0,0))
        pygame.display.update()

        clock.tick(60)

run_game_loop()
pygame.quit()
quit()