import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Bullet properties
bullet_radius = 5
bullet_speed = 3
bullet_angle = 0  # Starting angle

# Circular pattern properties
pattern_center = (width // 2, height // 2)
pattern_radius = 100
num_bullets = 12

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    # Draw circular bullet pattern
    for _ in range(num_bullets):
        # Calculate bullet position around the circle
        x = int(round(pattern_center[0] + pattern_radius * math.cos(math.radians(bullet_angle))))
        y = int(round(pattern_center[1] + pattern_radius * math.sin(math.radians(bullet_angle))))
        
        # Draw the bullet
        pygame.draw.circle(screen, red, (int(x), int(y)), bullet_radius)
        
        # Update the bullet angle for the next bullet
        bullet_angle += 360 / num_bullets

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()