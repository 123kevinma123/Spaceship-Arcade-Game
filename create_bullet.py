import pygame

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)

class create_bullet:
    def __init__(self, x_bullet, speed):
        self.x = x_bullet
        self.y = 550
        self.trail = 550
        self.speed = speed

    def update(self):
        self.y -= self.speed
        self.trail -= self.speed

    def draw(self):
        pygame.draw.rect(WIN, white, (self.x, self.y, 2, 12))
        pygame.draw.rect(WIN, orange, (self.x, self.trail, 2, 12))