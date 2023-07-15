import pygame
import random

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
sprite_width, sprite_height = 50, 60
sprite_angle = 180

#put image into argument + type of enemy
class enemy(pygame.sprite.Sprite):
    def __init__(self, x_player, y_player):
        super().__init__()
        #self.x = random.randint(50, 350)
        self.x = 100
        self.y = 0
        self.image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c0.png")
        self.image = pygame.transform.scale(self.image, (sprite_width, sprite_height))
        self.image = pygame.transform.rotate(self.image, sprite_angle)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.slope = (self.y - y_player) // (self.x - x_player)

    #define suicide bomber
    #pauses a bit and launches themselves at player coordinates in diagonal
    def bat_bomber(self):
        if self.x <= 400 and self.x >= 0 and self.y >= 0 and self.y <= 600:
            self.x += 0.5
            self.y += self.slope // 2