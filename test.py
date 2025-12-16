def main():
    import pygame

    pygame.init()

    screen_size = (800,400)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    pygame.mixer.music.load('projectweek-39-benno-for-president/sounds/background.ogg')
    pygame.mixer.music.play(-1)

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
     




    pygame.display.flip()
    clock.tick(60)

    pygame.quit()


main()