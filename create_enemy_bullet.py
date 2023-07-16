import pygame
import math

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
green = (0,100,0)
red = (255, 0, 0)

#circular bullet properties
bullet_radius = 5
bullet_speed = 3
bullet_angle = 0  # Starting angle

class create_enemy_bullet:
    def __init__(self, x_bullet, y_bullet, speed, circle_bullet):
        self.x = x_bullet
        self.y = y_bullet
        self.speed = speed
        self.pattern_radius = 20
        self.cx = 0
        self.cy = 0
        self.pattern_center = (x_bullet, y_bullet)
        self.num_bullets = circle_bullet


    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, red, (self.x, self.y, 10, 10))
    
    def circle(self):
        global bullet_angle
        self.x = int(round(self.pattern_center[0] + self.pattern_radius * math.cos(math.radians(bullet_angle))))
        self.y = int(round(self.pattern_center[1] + self.pattern_radius * math.sin(math.radians(bullet_angle))))
        self.pattern_radius += self.speed 
        # Draw the bullet
        #pygame.draw.circle(WIN, red, (int(x), int(y)), bullet_radius)
        
        # Update the bullet angle for the next bullet
        bullet_angle += 360 // self.num_bullets
