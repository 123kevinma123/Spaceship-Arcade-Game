import math
import pygame
import random
import sys

WIN = pygame.display.set_mode((400, 600))
white = (255, 255, 255)
orange = (255,140,0)
sprite_width, sprite_height = 60, 60
sprite_angle = 180

# Redirect standard output to console
sys.stdout = sys.__stdout__

#put image into argument + type of enemy
class enemy(pygame.sprite.Sprite):
    def __init__(self, x_player, y_player, spawn_x, spawn_y, pos):
        super().__init__()
        #self.x = random.randint(50, 350)
        self.x = spawn_x
        self.y = spawn_y
        self.playerx = x_player
        self.playery = y_player
        self.image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c0.png")
        self.image = pygame.transform.scale(self.image, (sprite_width, sprite_height))
        self.image = pygame.transform.rotate(self.image, sprite_angle)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.slope = 0
        if self.x - x_player != 0:
            self.slope = (y_player - self.y) / (x_player - self.x)
        #self.distance = math.sqrt((y_player - self.y)**2 + (x_player - self.x)**2)
        self.speed = 3
        #self.scale_factor = self.speed / self.distance
        self.temp = False
        self.temp2 = False
        self.pos = pos

    #define suicide bomber
    #pauses a bit and launches themselves at player coordinates in diagonal
    def bat_bomber(self):
        if -60 <= self.x <= 400 and -60 <= self.y <= 600:
            dx = self.playerx - self.x
            dy = self.playery - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)      
        if distance > 10:
            dx /= distance
            dy /= distance
            self.x += dx * self.speed
            self.y += dy * self.speed
            self.rect.x = self.x
            self.rect.y = self.y


    #define soldier --> maybe make into stationary turret?
    #launches volleys of bullets at a time, recalibrate slope after each set of bullets?
    #spawn 5 bullets, each with a slightly lower y value, timer for bullet spawn interval --> readjust player coordinates for next bullet
    def soldier(self):
        if self.x <= 400 and self.x >= 0 and self.y >= 0 and self.y <= 600:
            self.x += 0.5
            self.y += self.slope // 2

    #define explody ball thing
    #spawns from both sides of screen and lanuches bullets in a circular pattern
    def ball_right(self):
        self.y = 150
        if self.x <= 400:
            self.x += 0.2
        self.rect.x = self.x
        self.rect.y = self.y

    def ball_left(self):
        self.y = 150
        if self.x >= -100:
            self.x -= 0.2
        self.rect.x = self.x
        self.rect.y = self.y
        
        