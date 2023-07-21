import pygame
import math

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
green = (0, 255, 0)
red = (255, 0, 0)

#circular bullet properties
bullet_radius = 5
bullet_speed = 3
bullet_angle = 0  # Starting angle

class create_enemy_bullet:
    def __init__(self, x_bullet, y_bullet, speed, circle_bullet, x_ship, y_ship):
        self.x = x_bullet
        self.y = y_bullet
        self.speed = speed
        self.pattern_radius = 20
        self.cx = 0
        self.cy = 0
        self.pattern_center = (x_bullet, y_bullet)
        self.num_bullets = circle_bullet
        self.x_ship = x_ship
        self.y_ship = y_ship


    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, green, (self.x, self.y, 10, 10))
    
    def circle(self):
        global bullet_angle
        self.x = int(round(self.pattern_center[0] + self.pattern_radius * math.cos(math.radians(bullet_angle))))
        self.y = int(round(self.pattern_center[1] + self.pattern_radius * math.sin(math.radians(bullet_angle))))
        self.pattern_radius += self.speed 
        # Draw the bullet
        #pygame.draw.circle(WIN, red, (int(x), int(y)), bullet_radius)
        
        # Update the bullet angle for the next bullet
        bullet_angle += 360 // self.num_bullets

    def soldier(self):
        dx = self.x_ship - self.x
        dy = self.y_ship - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)      
        if distance > 10:
            dx /= distance
            dy /= distance

            next_x = self.x + dx * self.speed * 5
            next_y = self.y + dy * self.speed * 5

            # Update the current position with the interpolated position
            self.x = next_x
            self.y = next_y


