import pygame
from app import main


heart = pygame.image.load('sprites/hearts/l0_hearts1')

revive_count = [heart, heart, heart]

screen = pygame.display.set_mode(screen_size)
screen.blit(heart,(cam1.width - 924, cam1.height - 734))