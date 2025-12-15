import pygame


def create_main_surface():
    while True:
        pygame.display.set_mode(screen_size)

def draw_circle_on_surface(surface, color, center, radius):
    pygame.display.draw(surface = surface, color= color, center = center, radius = radius)

# Initialize Pygame
pygame.init()

# Tuple representing width and height in pixels
screen_size = (1024, 768)

# Create window with given size


draw_circle_on_surface(pygame.display.set_mode, (255,255,255), (512,348), 300)
create_main_surface()

