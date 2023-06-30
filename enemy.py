import pygame
import random

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
sprite_width, sprite_height = 30, 30

class enemy:
    def __init__(self, speed):
        self.x = random.randint(50, 350)
        self.y = 0
        self.speed = speed

    #def update(self):
        #self.y += self.speed

    #ship sprites
    def ship_sprites(self):
        #pygame.draw.rect(WIN, red, pygame.Rect(ship_x, ship_y, box_width, box_height))
        sprite_image = pygame.image.load("C:\Users\123ke\Documents\GitHub\spaceship\enemy_sprite.png")
        sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
        WIN.blit(sprite_image, (self.x, self.y))