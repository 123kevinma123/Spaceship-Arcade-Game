import pygame

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
pink = (255, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
dark_red = (125,15,32)

class create_bullet:
    def __init__(self, x_bullet, y_bullet, speed):
        self.x = x_bullet
        self.y = y_bullet
        self.speed = speed
        #print(self.y)

    def update(self):
        self.y -= self.speed
        #print(self.y)

    def draw(self):
        pygame.draw.rect(WIN, red, (self.x, self.y, 4, 20))
        #sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/bullet.png")
        #sprite_image = pygame.transform.scale(sprite_image, (40, 20))
        #WIN.blit(sprite_image, (self.x, self.y))
