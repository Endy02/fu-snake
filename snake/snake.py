import pygame
from pygame.locals import *
import time
from snake.chicken import Chicken
from snake.jacob import Jacob

SIZE = 40

class Snake():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Bombo snake")
        pygame.mixer.init()
        self.background_sound()
        self.surface = pygame.display.set_mode((800,540))
        self.surface.fill((110, 110, 200))
        self.jacob = Jacob(self.surface, 1)
        self.jacob.draw()
        self.chicken = Chicken(self.surface)
        self.chicken.draw()
    
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE: 
            if y1 >= y2 and y1 < y2 + SIZE: 
                return True
            
        return False
    
    def score(self):
        font = pygame.font.SysFont('arial', 25)
        score = font.render(f"Score : {self.jacob.length}", True, (255, 255, 255))
        self.surface.blit(score, (650, 10))
        pygame.display.flip()
    
    def game_over(self):
        self.surface.fill((110, 110, 200))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.jacob.length}", True, (255, 255, 255))
        self.surface.blit(line1, (50, 200))
        lin2 = font.render("Press enter to try again. To exit press Escape", True, (255, 255, 255))
        self.surface.blit(lin2, (50, 250))
        pygame.display.flip()
        pygame.mixer.music.pause()
        
    def reset(self):
        self.jacob = Jacob(self.surface, 1)
        self.chicken = Chicken(self.surface)
        
    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.jacob.move_up()
                        if event.key == K_DOWN:
                            self.jacob.move_down()
                        if event.key == K_LEFT:
                            self.jacob.move_left()
                        if event.key == K_RIGHT:
                            self.jacob.move_right()
                        
                elif event.type == QUIT:
                    running = False
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()
                
            time.sleep(0.2)
            
    def sound(self, name):
        sound = pygame.mixer.Sound(f"assets/sounds/{name}.mp3")
        sound.set_volume(1)
        sound.play()
        
    def background_sound(self):
        pygame.mixer.music.load("assets/sounds/snake_song.mp3")
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(0.2)
            
    def play(self):
        self.jacob.walk()
        self.chicken.draw()
        self.score()
        if self.is_collision(self.jacob.x[0], self.jacob.y[0], self.chicken.x, self.chicken.y):
            self.sound("wow")
            self.jacob.increment()
            self.chicken.move()
        
        if not (0 <= self.jacob.x[0] <= 800 and 0 <= self.jacob.y[0] <= 500):
            self.sound('bruhh')
            raise "Hit the boundry error"
            
        for i in range(2, self.jacob.length):
            if self.is_collision(self.jacob.x[0], self.jacob.y[0], self.jacob.x[i], self.jacob.y[i]):
                self.sound("bruhh")
                raise "Game Over"

