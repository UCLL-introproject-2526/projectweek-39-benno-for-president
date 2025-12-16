import pygame
pygame.init()

def main():
    

    screen_size = (800,400)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    pygame.mixer.music.load('projectweek-39-benno-for-president/sounds/lobby_music.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)

    benno_img = pygame.image.load('projectweek-39-benno-for-president/sprites/bigbenno_sprite.png').convert_alpha()
    benno_img = pygame.transform.smoothscale(benno_img, (100, 100))

    def render_frame(surface, xpos, ypos):
        rect = benno_img.get_rect(center=(xpos, ypos))
        surface.blit(benno_img, rect)

    xpos = 400
    ypos = 200
    
    run = True

    while run:
        screen.fill((0,0,0))



        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            xpos += 5
        if key[pygame.K_q]:
            xpos -= 5
        if key[pygame.K_s]:
            ypos += 5
        if key[pygame.K_z]:
            ypos -= 5



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        
        render_frame(screen, xpos, ypos)
    

        clock.tick(60)
        pygame.display.flip()
    
    pygame.quit()


main()