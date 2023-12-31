import time
import pygame
import random
import sys

from create_bullet import create_bullet
from create_enemy_bullet import create_enemy_bullet
from enemy import enemy
from start_page import start_page

# Redirect standard output to console
sys.stdout = sys.__stdout__

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
bullet_width, bullet_height = 4, 20
start_var = 100
ship_x, ship_y = (width - sprite_width) / 2, height + sprite_height
x_bullet, y_bullet = (width - bullet_width) / 2, height - sprite_height - start_var - 10
bullet_speed, enemy_bullet_speed = 10, 8
speed_down, speed_up, speed_LR = 3, 3, 2
vertical_max = 0
scroll_speed = 2
bullets_arr = []
enemy_bullets_arr = []
enemy_arr = pygame.sprite.Group()
bullet_spawn_interval, enemy_bullet_spawn_interval = 80, 100
spawn_x = 100

bat_arr = []
circle_arr = []
circle_bullets_arr = []
soldier_arr = []
soldier_bullets_arr = []

#Set display surface perimeters 
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sequere lucem")
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
    WIN.blit(sprite_image, (ship_x, ship_y))

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
        if hold_keyL:
            move_left()
        if hold_keyR:
            move_right()
        if hold_keyU:
            move_up()
        if hold_keyD:
            move_down()

def bullet_spawn(bullet_spawn_timer, current_time_bullet, x_bullet, score):
    bullet_count = 1
    bullet_spawn_distance = 8
    bullets_to_remove = []  #store bullets to be removed
    y_coord = [[y_bullet],
               [y_bullet, y_bullet],
               [y_bullet + 10, y_bullet, y_bullet + 10],
               [y_bullet + 15, y_bullet, y_bullet, y_bullet + 15],
               [y_bullet + 20, y_bullet + 10, y_bullet, y_bullet + 10, y_bullet + 20]] #stores y coordinate variations
    count = 0
    if current_time_bullet - bullet_spawn_timer >= bullet_spawn_interval:
        if score >= 200 and score < 300:
            bullet_count = 2
            x_bullet += bullet_spawn_distance // 2
        elif score >= 300 and score < 400:
            bullet_count = 3
            x_bullet += bullet_spawn_distance
        elif score >= 400 and score < 500:
            bullet_count = 4
            x_bullet += bullet_spawn_distance * 3 // 2
        elif score >= 500:
            bullet_count = 5
            x_bullet += bullet_spawn_distance * 2
        
        for _ in range(bullet_count):  #spawn bullets based on score
            shot = create_bullet(x_bullet, y_coord[bullet_count- 1][count], bullet_speed)
            bullets_arr.append(shot)
            x_bullet -= bullet_spawn_distance
            count += 1                

        bullet_spawn_timer = current_time_bullet

    for shot in bullets_arr:
        shot.update()
        shot.draw()
        if shot.y < 0:
            bullets_to_remove.append(shot)  #add bullets to be removed to the separate list

    #remove bullets that need to be removed
    for shot in bullets_to_remove:
        bullets_arr.remove(shot)

    return bullet_spawn_timer

#enemy bullet spawning
def enemy_bullet_spawn2(enemy_bullet_spawn_timer, current_time_enemy_bullet):
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

#enemy spawning 
def enemy_spawn(enemy_spawn_timer, current_time_enemy):
    global spawn_x
    enemy_spawn_interval = 2000
    spawn_y = 0
    if spawn_x < 400:
        spawn_x += 200
    if current_time_enemy - enemy_spawn_timer >= enemy_spawn_interval:
        new_enemy = enemy(ship_x, ship_y, spawn_x, spawn_y)
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

#circle bullet spawning test
def circle_bullet_spawn(circle_bullet_spawn_timer, current_time_circle_bullet):
    global x_bullet, circle_bullets_arr
    circle_bullet_spawn_interval = 1000
    bullets_to_remove = []  # Store bullets to be removed
    circle_bullet = 24
    if current_time_circle_bullet - circle_bullet_spawn_timer >= circle_bullet_spawn_interval:
        for enemy_bot in circle_arr:
            for _ in range(circle_bullet):
                shot = create_enemy_bullet(enemy_bot.x + 30, enemy_bot.y + 30, 1, circle_bullet, ship_x, ship_y)
                circle_bullets_arr.append(shot)
        circle_bullet_spawn_timer = current_time_circle_bullet

    for shot in circle_bullets_arr:
        shot.circle()
        shot.draw()
        if shot.y > 2000 or shot.y < -1000 or shot.x > 1000 or shot.x < -1000:
            bullets_to_remove.append(shot)  #add bullets to be removed to the separate list

    #remove bullets that need to be removed
    for shot in bullets_to_remove:
       circle_bullets_arr.remove(shot)
    return circle_bullet_spawn_timer

#enemy circle spawner
def circle_spawn(circle_spawn_timer, current_time_circle):
    circle_spawn_interval = 5000
    if current_time_circle - circle_spawn_timer >= circle_spawn_interval:
        circleL = enemy(ship_x, ship_y, 60, 150, 1)
        circleR = enemy(ship_x, ship_y, 270, 150, 2)
        if len(circle_arr) != 2:
            circle_arr.append(circleL)
            circle_arr.append(circleR)
        circle_spawn_timer = current_time_circle

    for enemy_bot in circle_arr:
        if enemy_bot.pos == 1:
            enemy_bot.ball_right()
        else:
            enemy_bot.ball_left()
        WIN.blit(enemy_bot.image, (enemy_bot.x + 5, enemy_bot.y + 5))

    #add remove function
    return circle_spawn_timer

#enemy bat spawner
def bat_spawn(bat_spawn_timer, current_time_bat):
    bat_spawn_interval = 1000
    if current_time_bat - bat_spawn_timer >= bat_spawn_interval:
        bat = enemy(ship_x, ship_y, 0, 0, 1)
        bat2 = enemy(ship_x, ship_y, 340, 0, 2)
        #if len(bat_arr) != 10:
        bat_arr.append(bat)
        bat_arr.append(bat2)
        bat_spawn_timer = current_time_bat

    for enemy_bot in bat_arr:
        enemy_bot.bat_bomber()
        WIN.blit(enemy_bot.image, (enemy_bot.x, enemy_bot.y))

    return bat_spawn_timer

#soldier bullet spawning test
def soldier_bullet_spawn(soldier_bullet_spawn_timer, current_time_soldier_bullet):
    global x_bullet, soldier_bullets_arr
    soldier_bullet_spawn_interval = 1000
    bullets_to_remove = []  # Store bullets to be removed
    circle_bullet = 24
    if current_time_soldier_bullet - soldier_bullet_spawn_timer >= soldier_bullet_spawn_interval:
        for enemy_bot in soldier_arr:
            for _ in range(circle_bullet):
                shot = create_enemy_bullet(enemy_bot.x, enemy_bot.y, 1, circle_bullet, ship_x, ship_y)
                soldier_bullets_arr.append(shot)
        soldier_bullet_spawn_timer = current_time_soldier_bullet

    for shot in soldier_bullets_arr:
        shot.soldier()
        shot.draw()
        if shot.y > 2000 or shot.y < -1000 or shot.x > 1000 or shot.x < -1000:
            bullets_to_remove.append(shot)  #add bullets to be removed to the separate list

    #remove bullets that need to be removed
    for shot in bullets_to_remove:
       soldier_bullets_arr.remove(shot)
    return soldier_bullet_spawn_timer
#Main function
def main():
    global x_bullet, y_bullet, scroll_speed, background_y1, background_y2, ship_y, spawn_x
    run, shoot = True, False
    score = 0
    transition_speed = 2.5
    hold_keyR, hold_keyL, hold_keyU, hold_keyD = False, False, False, False
    bullet_spawn_timer = pygame.time.get_ticks()
    enemy_spawn_timer = pygame.time.get_ticks()
    enemy_bullet_spawn_timer = pygame.time.get_ticks()
    
    soldier_spawn_timer = pygame.time.get_ticks()
    soldier_bullet_spawn_timer = pygame.time.get_ticks()

    circle_spawn_timer = pygame.time.get_ticks()
    circle_bullet_spawn_timer = pygame.time.get_ticks()
    
    bat_spawn_timer = pygame.time.get_ticks()
    

    shoot_timer = 0
    shoot_delay = 400
    count = 0

    #start menu
    start = start_page()
    start.run()
    background_y1 = start.background_y1
    background_y2 = start.background_y2


    if spawn_x < 400:
        spawn_x += 200

    soldier = enemy(ship_x, ship_y, 200, 100, 1)
    soldier_arr.append(soldier)

    #main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

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
        
        background()
        
        if ship_y > (height - sprite_height - start_var) and shoot == False:
            ship_sprites(hold_keyR, hold_keyL, hold_keyU, hold_keyD)
            ship_y -= transition_speed
        else:
            shoot = True
            if count == 0:
                shoot_timer = pygame.time.get_ticks()
                count += 1

        current_shoot_timer = pygame.time.get_ticks()
        
        if shoot and current_shoot_timer - shoot_timer > shoot_delay:
            #bullet spawning
            movement(hold_keyL, hold_keyR, hold_keyU, hold_keyD)

            current_time_bullet = pygame.time.get_ticks()
            bullet_spawn_timer = bullet_spawn(bullet_spawn_timer, current_time_bullet, x_bullet, 500)
            ship_sprites(hold_keyR, hold_keyL, hold_keyU, hold_keyD)
        elif shoot and current_shoot_timer - shoot_timer < shoot_delay:
            ship_sprites(hold_keyR, hold_keyL, hold_keyU, hold_keyD)

        #enemy spawning
        current_time_enemy = pygame.time.get_ticks()
        #enemy_spawn_timer = enemy_spawn(enemy_spawn_timer, current_time_enemy)

        #circle bullet spawning
        current_time_circle_bullet = pygame.time.get_ticks()
        #circle_bullet_spawn_timer = circle_bullet_spawn(circle_bullet_spawn_timer, current_time_circle_bullet)
        
        #circle enemy spawning
        current_time_circle = pygame.time.get_ticks()
        #circle_spawn_timer = circle_spawn(circle_spawn_timer, current_time_circle)
        
        #bat spawning
        current_time_bat = pygame.time.get_ticks()
        #bat_spawn_timer = bat_spawn(bat_spawn_timer, current_time_bat)
        
        #soldier bullet spawning
        current_time_soldier_bullet = pygame.time.get_ticks()
        #soldier_bullet_spawn_timer = soldier_bullet_spawn(soldier_bullet_spawn_timer, current_time_soldier_bullet)
        
        
        #need to trash bullets and stuff after they move off screen 
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()

main()