import pygame

class GameObject:
    def __init__(self, x, y, width, height, path):
        image = pygame.image.load(path)
        self.image = pygame.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    
