import pygame
import random


SIZE = 40

class Chicken():
    def __init__(self, parent_screen):
        self.image = pygame.image.load("assets/images/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(1, 19) * SIZE
        self.y = random.randint(1, 12) * SIZE