import pygame

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
green = (0,100,0)
red = (255, 0, 0)

class create_enemy_bullet:
    def __init__(self, x_bullet, speed):
        self.x = x_bullet
        self.y = 45
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, red, (self.x, self.y, 2, 12))
