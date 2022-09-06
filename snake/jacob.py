import pygame
from pygame.locals import *

SIZE = 40

class Jacob():
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("assets/images/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'
        
    def increment(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        
    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()
        
    def draw(self):
        self.parent_screen.fill((110, 110, 200))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
        
    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction = 'right'
        
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'