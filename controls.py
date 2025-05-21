import pygame

class Controls:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.up = keys[pygame.K_UP]
        self.down = keys[pygame.K_DOWN]
        self.left = keys[pygame.K_LEFT]
        self.right = keys[pygame.K_RIGHT]