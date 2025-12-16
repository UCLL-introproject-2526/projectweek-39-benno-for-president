import pygame
pygame.init()

def main():
    

    screen_size = (800,400)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()


    def render_frame(surface, xpos, ypos):
        pygame.draw.circle(surface, (255,255,255), (xpos, ypos), 100)

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