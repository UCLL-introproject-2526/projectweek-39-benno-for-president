import pygame
from pygame.display import flip
from time import sleep

# Initialize Pygame
pygame.init()

# Tuple representing width and height in pixels
screen_size = (1024, 768)

# Create window with given size
def create_main_surface():
    return type(pygame.display.set_mode(screen_size))

def buffer():
    while True:
        sleep(1/60)
        flip()
        
def render_frame(surface):
    while True:
        surface
        pygame.draw.circle(surface = surface, color = (0,255,255), center = (512, 384), radius = 200)
        buffer()

print(create_main_surface())
# render_frame(pygame.display.set_mode(screen_size))
