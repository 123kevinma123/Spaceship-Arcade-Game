import pygame
import sys

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
scroll_speed = 2
width, height = 400, 600
sprite_width, sprite_height = 60, 60
ship_x, ship_y = (width - sprite_width) / 2, -sprite_height
ship_speed = 2
start_pos = 100
#Set background
background_image = pygame.image.load("background2.png")
background_image = pygame.transform.scale(background_image, (width, height))
background_height = background_image.get_height()
background_y1 = 0
background_y2 = -background_height

WIN = pygame.display.set_mode((width, height))


class start_page:
    def __init__(self):
        self.width = width
        self.height = height
        pygame.display.set_caption("Spaceship Game")

        self.font = pygame.font.Font(None, 36)

        self.start_page = True

        self.background_y1 = 0
        self.background_y2 = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_page = False

    def draw(self):
        # Draw title text
        title_text = self.font.render("Spaceship Game", True, red)
        title_rect = title_text.get_rect(center = (self.width // 2, self.height // 2 - 50))
        WIN.blit(title_text, title_rect)

        # Draw instructions text
        instructions_text = self.font.render("Press SPACE to start", True, red)
        instructions_rect = instructions_text.get_rect(center = (self.width // 2, self.height // 2 + 50))
        WIN.blit(instructions_text, instructions_rect)

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
        while self.start_page:
            self.background()
            self.handle_events()
            self.draw()
            clock = pygame.time.Clock()
            clock.tick(120)
