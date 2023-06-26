import pygame
import random

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)

class power_up:
    def __init__(self, speed):
        self.x = random.randint(50, 350)
        self.y = 0
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, white, (self.x, self.y, 10, 10))
