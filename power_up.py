import pygame

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)

class power_up:
    def __init__(self, x_bullet, speed):
        self.x = x_bullet
        self.y = 0
        self.speed = speed

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, white, (self.x, self.y, 2, 12))
