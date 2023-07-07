import pygame
import random

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
sprite_width, sprite_height = 50, 60
sprite_angle = 180

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(50, 350)
        self.y = 0
        self.image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c0.png")
        self.image = pygame.transform.scale(self.image, (sprite_width, sprite_height))
        self.image = pygame.transform.rotate(self.image, sprite_angle)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y