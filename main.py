import pygame
import random

from create_bullet import create_bullet

#Intialization
pygame.init()

#Set width and height
width = 400
height = 600

#Set RGB + other constants
black = (0, 0, 0)
red = (255, 0, 0)
sprite_width, sprite_height = 40, 50
bullet_height, bullet_width = 5, 5
ship_x, ship_y = (width - sprite_height) / 2, height - sprite_height
x_bullet, y_bullet = (width - bullet_height) / 2, height
bullet_speed, ship_speed = 7, 8

#Set display surface perimeters 
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceship Game")
WIN.fill(black)
clock = pygame.time.Clock()
info_obj = pygame.display.Info()


#ship sprites
def ship_sprites():
    #pygame.draw.rect(WIN, red, pygame.Rect(ship_x, ship_y, box_width, box_height))
    sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/spaceship_sprite.png")
    sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
    WIN.blit(sprite_image, (ship_x + 2, ship_y))

#Move spaceship left
def move_left():
    global ship_x, x_bullet
    if ship_x - ship_speed > 0:
        ship_x -= ship_speed          
        x_bullet -= ship_speed

#Move spaceship right
def move_right():
    global ship_x, x_bullet
    if ship_x + ship_speed < width - sprite_height:
        ship_x += ship_speed
        x_bullet += ship_speed

#Main function
def main():
    global x_bullet
    run = True
    hold_keyR, hold_keyL, hold_keyU, hold_keyD = False, False, False, False
    bullet_spawn_timer = pygame.time.get_ticks()
    bullet_spawn_interval = 70
    bullets_arr = []

    #main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hold_keyR = True
                if event.key == pygame.K_LEFT:
                    hold_keyL = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hold_keyR = False
                if event.key == pygame.K_LEFT:
                    hold_keyL = False
    
        #Left, Right, Up, Down, hold
        if hold_keyL:
            move_left()
        if hold_keyR:
            move_right()

        WIN.fill(black)

        #bullet spawning
        current_time = pygame.time.get_ticks()
        if current_time - bullet_spawn_timer >= bullet_spawn_interval:
            shot = create_bullet(x_bullet, bullet_speed)
            bullets_arr.append(shot)
            bullet_spawn_timer = current_time

        for shot in bullets_arr:
            shot.update()
            shot.draw()
        
        ship_sprites()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()