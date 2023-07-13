import pygame
import sys

pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (125,15,32)
scroll_speed = 2
width, height = 400, 600
sprite_width, sprite_height = 60, 60
ship_x, ship_y = (width - sprite_width) / 2, -sprite_height
ship_speed = 2
start_pos = 100
WIN = pygame.display.set_mode((width, height))

# Redirect standard output to console
sys.stdout = sys.__stdout__

#Set background
background_image = pygame.image.load("background2.png")
background_image = pygame.transform.scale(background_image, (width, height))
background_height = background_image.get_height()
background_y1 = 0
background_y2 = -background_height

#font
font_path2 = "/Users/123ke/Documents/GitHub/spaceship/font4.ttf"
font_path = "/Users/123ke/Documents/GitHub/spaceship/font4.ttf"
title_size = 50
font_size = 18
title_font = pygame.font.Font(font_path2, title_size)
custom_font = pygame.font.Font(font_path, font_size)
#title_font.set_bold(True)
#custom_font.set_bold(True)

instructions_text = custom_font.render("BEGIN", True, red)
instructions_rect = instructions_text.get_rect(center = (width // 2, height // 2 + 150))
quit_text = custom_font.render("Quit", True, red)
quit_rect = quit_text.get_rect(center = (width // 2, height // 2 + 180))

class start_page:
    def __init__(self):
        self.width = width
        self.height = height
        pygame.display.set_caption("Sequere lucem")

        self.start_page = True

        self.background_y1 = 0
        self.background_y2 = 0
        self.track = 0

    def handle_events(self, is_hover):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse = pygame.mouse.get_pos()
            if instructions_rect.collidepoint(mouse):
                is_hover = True
                self.track = 2
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_page = False
            elif not instructions_rect.collidepoint(mouse) and not quit_rect.collidepoint(mouse):
                is_hover = False
                self.track = 0
            elif quit_rect.collidepoint(mouse):
                is_hover = True
                self.track = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_page = False
            else:
                is_hover = False
                self.track = 0
            
        return is_hover

    def draw(self, is_hover):
        #cross
        sprite_image = pygame.image.load(f"/Users/123ke/Documents/GitHub/spaceship/cross.png")
        sprite_image = pygame.transform.scale(sprite_image, (150, 150))
        WIN.blit(sprite_image, (120, 250))

        #title text
        title_text = title_font.render("Sequere", True, red)
        title_rect = title_text.get_rect(center = (self.width // 2, self.height // 2 - 180))
        WIN.blit(title_text, title_rect)
        title_text2 = title_font.render("Lucem", True, red)
        title_rect2 = title_text2.get_rect(center = (self.width // 2, self.height // 2 - 130))
        WIN.blit(title_text2, title_rect2)

        #start/quit text
        if is_hover and self.track == 2:
            instructions_text = custom_font.render("BEGIN", True, white)
        else:
            instructions_text = custom_font.render("BEGIN", True, red)
        if is_hover and self.track == 1:
            quit_text = custom_font.render("QUIT", True, white)
        else:
            quit_text = custom_font.render("QUIT", True, red)
        
        instructions_rect = instructions_text.get_rect(center = (self.width // 2, self.height // 2 + 150))
        quit_rect = quit_text.get_rect(center = (self.width // 2, self.height // 2 + 180))

        WIN.blit(instructions_text, instructions_rect)
        WIN.blit(quit_text, quit_rect)

        pygame.display.flip()
    
    #scrolling background
    def background(self):
        global background_y1, background_y2
        background_y1 += scroll_speed
        background_y2 += scroll_speed
        if background_y1 >= background_height:
            background_y1 = -background_height
        if background_y2 >= background_height:
            background_y2 = -background_height
        WIN.blit(background_image, (0,background_y1))
        WIN.blit(background_image, (0, background_y2))
        self.background_y1 = background_y1
        self.background_y2 = background_y2

    #ship sprites
    def ship_sprites(self, ship_y):
        cross_index = -1
        sprite_image = pygame.image.load(f"/Users/123ke/Documents/GitHub/spaceship/c5_{cross_index + 1}.png")
        #flame_image = pygame.image.load(f"/Users/123ke/Documents/GitHub/spaceship/c6_{flame_index + 1}.png")
        #sprite_image.blit(flame_image, (0, 0))
        sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
        WIN.blit(sprite_image, (ship_x, ship_y))
    
    def run(self):
        is_hover = False
        while self.start_page:
            self.background()
            self.draw(is_hover)
            is_hover = self.handle_events(is_hover)
            clock = pygame.time.Clock()
            clock.tick(120)
