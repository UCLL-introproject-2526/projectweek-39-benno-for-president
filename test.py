import pygame
from pygame.display import flip
from time import sleep

# Initialize Pygame
pygame.init()

# Tuple representing width and height in pixels
screen_size = (1024, 768)

# Create window with given size
def create_main_surface():
    while True:
        surface = pygame.display.set_mode(screen_size)
        pygame.draw.circle(surface = surface, color = (255,255,255), center = (512, 384), radius = 200)
        buffer()

def buffer():
    while True:
        sleep(1/60)
        flip()
        

create_main_surface()
