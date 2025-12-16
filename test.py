import pygame

def main():
    pygame.init()

    screen_size = (800,400)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.flip()
    clock.tick(60)
    pygame.quit()


main()