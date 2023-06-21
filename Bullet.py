import pygame
import random

class Bullet:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.speed = 3

    def update(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))