import pygame
import random

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
sprite_width, sprite_height = 40, 50
sprite_angle = 180

class enemy:
    def __init__(self):
        self.x = random.randint(50, 350)
        self.y = 0

    #def update(self):
        #self.y += self.speed

    #ship sprites
    def ship_sprites(self):
        #pygame.draw.rect(WIN, red, pygame.Rect(ship_x, ship_y, box_width, box_height))
        sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/spaceship_sprite.png")
        sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
        rotated_sprite = pygame.transform.rotate(sprite_image, sprite_angle)
        WIN.blit(rotated_sprite, (self.x, self.y))