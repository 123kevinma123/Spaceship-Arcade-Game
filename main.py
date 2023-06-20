import pygame

#Intialization
pygame.init()

#Set width and height
width = 400
height = 600

#Set RGB + other constants
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
box_height, box_width = 30, 30
bullet_height, bullet_width = 10, 10
ship_x, ship_y = (width - box_width) / 2, height - box_height
x_bullet, y_bullet = (width - bullet_height) / 2, height

#Set display surface perimeters 
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spaceship Game")
WIN.fill(black)
clock = pygame.time.Clock()
info_obj = pygame.display.Info()

def update():
    pygame.draw.rect(WIN, red, pygame.Rect(ship_x, ship_y, box_width, box_height))

#Move to new class
def bullets():
    global y_bullet
    y_bullet -= 3
    pygame.draw.rect(WIN, white, pygame.Rect(x_bullet, 
                                             y_bullet, bullet_width, bullet_height))

#Move spaceship left
def move_left():
    global ship_x
    global x_bullet
    ship_x -= 10          
    x_bullet -= 10

#Move spaceship right
def move_right():
    global ship_x
    global x_bullet
    ship_x += 10
    x_bullet += 10

#Main function
def main():
    run = True
    hold_keyR = False
    hold_keyL = False
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
    
        #Left and Right hold
        if hold_keyL:
            move_left()
        if hold_keyR:
            move_right()

        WIN.fill(black)
        update()
        bullets()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()