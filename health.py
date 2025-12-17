import pygame

heart = pygame.image.load('sprites/hearts/l0_hearts1')

revive_count = [heart, heart, heart]

screen = pygame.display.set_mode(screen_size)
screen.blit(heart,(900,0))