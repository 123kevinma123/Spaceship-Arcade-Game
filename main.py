import time
import pygame
import random

from create_bullet import create_bullet
from create_enemy_bullet import create_enemy_bullet
from power_up import power_up
from enemy import enemy


#Intialization
pygame.init()

#Set width and height
width = 400
height = 600

#Set background
background_image = pygame.image.load("background2.png")
background_image = pygame.transform.scale(background_image, (width, height))
background_height = background_image.get_height()
background_y1 = 0
background_y2 = -background_height

#Set RGB + other constants

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255,140,0)
grey = (128, 128, 128)
silver = (192, 192, 192)
fire = (0, 42, 255)

sprite_width, sprite_height = 60, 60
bullet_height, bullet_width = 2, 13
ship_x, ship_y = (width - sprite_width) / 2, height - sprite_height
x_bullet, y_bullet = (width - bullet_width) / 2, height - sprite_height
bullet_speed, enemy_bullet_speed = -5, 8
speed_down, speed_up, speed_LR = 3.5, 4, 4
vertical_max = 0
scroll_speed = 2
bullets_arr = []
powerup_arr = []
enemy_bullets_arr = []
enemy_arr = pygame.sprite.Group()
bullet_spawn_interval, enemy_bullet_spawn_interval = 300, 100

#Set display surface perimeters 
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceship Game")
WIN.fill(black)
clock = pygame.time.Clock()
info_obj = pygame.display.Info()

#ship sprites
def ship_sprites(hold_keyR, hold_keyL, hold_keyU, hold_keyD):
    cross_delay = 0.15
    flame_delay = 0.001
    if hold_keyR:
        sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c1.png")
    elif hold_keyL:
        sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c2.png")
    elif hold_keyU:
        sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c3.png")
    elif hold_keyD:
        sprite_image = pygame.image.load("/Users/123ke/Documents/GitHub/spaceship/c4.png")
    else:
        #cross_index = (pygame.time.get_ticks() // int(cross_delay * 1000)) % 10  # glowing cross animation
        #flame_index = (pygame.time.get_ticks() // int(flame_delay * 1000)) % 3  # flame animation
        cross_index = -1
        sprite_image = pygame.image.load(f"/Users/123ke/Documents/GitHub/spaceship/c5_{cross_index + 1}.png")
        #flame_image = pygame.image.load(f"/Users/123ke/Documents/GitHub/spaceship/c6_{flame_index + 1}.png")
        #sprite_image.blit(flame_image, (0, 0))
        
    sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
    WIN.blit(sprite_image, (ship_x - 6, ship_y))

#Move spaceship left
def move_left():
    global ship_x, x_bullet
    if ship_x - speed_LR > 0:
        ship_x -= speed_LR          
        x_bullet -= speed_LR

#Move spaceship right
def move_right():
    global ship_x, x_bullet
    if ship_x + speed_LR < width - sprite_width:
        ship_x += speed_LR
        x_bullet += speed_LR

#Move spaceship up
def move_up():
    global ship_y, y_bullet
    if ship_y - speed_up > vertical_max:
        ship_y -= speed_up
        y_bullet -= speed_up

#Move spaceship down
def move_down():
    global ship_y, y_bullet
    if ship_y + speed_down < height - sprite_height:
        ship_y += speed_down
        y_bullet += speed_down

def movement(hold_keyL, hold_keyR, hold_keyU, hold_keyD):
        global scroll_speed
        if hold_keyL:
            move_left()
        if hold_keyR:
            move_right()
        if hold_keyU:
            move_up()
        if hold_keyD:
            move_down()

#bullet spawning
def bullet_spawn(bullet_spawn_timer, current_time_bullet):
    global x_bullet, bullets_arr
    if current_time_bullet - bullet_spawn_timer >= bullet_spawn_interval:
        shot = create_bullet(x_bullet, y_bullet, bullet_speed)
        bullets_arr.append(shot)
        bullet_spawn_timer = current_time_bullet

    for shot in bullets_arr:
        shot.update()
        shot.draw()
        if shot.y < 0:
            bullets_arr.remove(shot)

    return bullet_spawn_timer

#enemy bullet spawning
def enemy_bullet_spawn(enemy_bullet_spawn_timer, current_time_enemy_bullet):
    global x_bullet, enemy_bullets_arr, enemy_bullet_spawn_interval
    if current_time_enemy_bullet - enemy_bullet_spawn_timer >= enemy_bullet_spawn_interval:
        for enemy_bot in enemy_arr:
            shot = create_enemy_bullet(enemy_bot.x + 18, enemy_bullet_speed)
            enemy_bullets_arr.append(shot)
        enemy_bullet_spawn_timer = current_time_enemy_bullet

    for shot in enemy_bullets_arr:
        shot.update()
        shot.draw()
        if shot.y > 600:
            enemy_bullets_arr.remove(shot)

    return enemy_bullet_spawn_timer


#powerup spawning
def powerup_spawn(powerup_spawn_timer, current_time_powerup):
    global powerup_arr
    powerup_spawn_interval = 1500
    if current_time_powerup - powerup_spawn_timer >= powerup_spawn_interval:
        upgrade = power_up(bullet_speed)
        powerup_arr.append(upgrade)
        powerup_spawn_timer = current_time_powerup

    for upgrade in powerup_arr:
        upgrade.update()
        upgrade.draw()
        if upgrade.y > 600:
            powerup_arr.remove(upgrade)

    return powerup_spawn_timer

#enemy spawning
def enemy_spawn(enemy_spawn_timer, current_time_enemy):
    enemy_spawn_interval = 2000
    if current_time_enemy - enemy_spawn_timer >= enemy_spawn_interval:
        new_enemy = enemy()
        collision = False
        for enemy_bot in enemy_arr: #checks if sprite will collide with anything in the group
            if pygame.sprite.collide_rect(enemy_bot, new_enemy):
                collision = True
                break
    
        if not collision: #add sprite to group if not
            enemy_arr.add(new_enemy)
            enemy_spawn_timer = current_time_enemy

    for enemy_bot in enemy_arr:
        WIN.blit(enemy_bot.image, (enemy_bot.x, enemy_bot.y))

    return enemy_spawn_timer

#scrolling background
def background():
    global background_y1, background_y2
    background_y1 += scroll_speed
    background_y2 += scroll_speed
    if background_y1 >= background_height:
        background_y1 = -background_height
    if background_y2 >= background_height:
        background_y2 = -background_height
    WIN.blit(background_image, (0,background_y1))
    WIN.blit(background_image, (0, background_y2))

#Main function
def main():
    global x_bullet, scroll_speed
    run = True
    hold_keyR, hold_keyL, hold_keyU, hold_keyD = False, False, False, False
    bullet_spawn_timer = pygame.time.get_ticks()
    powerup_spawn_timer = pygame.time.get_ticks()
    enemy_spawn_timer = pygame.time.get_ticks()
    enemy_bullet_spawn_timer = pygame.time.get_ticks()

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
                if event.key == pygame.K_UP:
                    #scroll_speed = 4
                    hold_keyU = True
                if event.key == pygame.K_DOWN:
                    #scroll_speed = 1
                    hold_keyD = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hold_keyR = False
                if event.key == pygame.K_LEFT:
                    hold_keyL = False
                if event.key == pygame.K_UP:
                    #scroll_speed = 2
                    hold_keyU = False
                if event.key == pygame.K_DOWN:
                    #scroll_speed = 2
                    hold_keyD = False
    
        movement(hold_keyL, hold_keyR, hold_keyU, hold_keyD)

        background()

        ship_sprites(hold_keyR, hold_keyL, hold_keyU, hold_keyD)

        #bullet spawning
        current_time_bullet = pygame.time.get_ticks()
        bullet_spawn_timer = bullet_spawn(bullet_spawn_timer, current_time_bullet)
        
        #powerup spawning
        #current_time_powerup = pygame.time.get_ticks()
        #powerup_spawn_timer = powerup_spawn(powerup_spawn_timer, current_time_powerup)

        #enemy spawning
        current_time_enemy = pygame.time.get_ticks()
        enemy_spawn_timer = enemy_spawn(enemy_spawn_timer, current_time_enemy)

        #enemy bullet spawning
        current_time_enemy_bullet = pygame.time.get_ticks()
        #enemy_bullet_spawn_timer = enemy_bullet_spawn(enemy_bullet_spawn_timer, current_time_enemy_bullet)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()