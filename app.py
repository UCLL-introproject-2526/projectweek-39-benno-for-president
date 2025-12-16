import pygame
pygame.init()

class Enemy:
    def __init__(self, cords, speed, health, dmg):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.set_dmg(dmg)
    
    def get_cords(self):
        return [self.__x, self.__y]

    def set_cords(self, list_inp):
        if isinstance(list_inp, list):
            if len(list_inp) == 2:
                self.__x = list_inp[0]
                self.__y = list_inp[1]
        else: 
            raise ValueError("enemy cords cannot be empty and has to be list")


    def get_speed(self):
        return self.__speed
    
    def set_speed(self, value):
        if value < 0:
            raise ValueError("enemy speed cannot be negative")
        self.__speed = value

    def get_health(self):
        return self.__health
    
    def set_health(self, value):
        if value < 0:
            raise ValueError("enemy health cannot be negative")
        self.__health = value

    def get_dmg(self):
        return self.__dmg
    
    def set_dmg(self, value):
        if value < 0:
            raise ValueError("enemy dmg cannot be negative")
        self.__dmg = value

    def move(self, play_x, play_y):
        ...

    def hit(self, other):
        self.__health 


def main():
    

    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    background = pygame.image.load('sprites/icy_background.png').convert()

    # pygame.mixer.music.load('projectweek-39-benno-for-president/sounds/lobby_music.mp3')
    # pygame.mixer.music.play(-1, fade_ms=3000)

    benno_img = pygame.image.load('sprites/bigbenno_sprite.png').convert_alpha()
    benno_img = pygame.transform.smoothscale(benno_img, (100, 100))

    

    def render_frame(surface, xpos, ypos):
        benno_rect = benno_img.get_rect(center = (xpos, ypos))
        surface.blit(benno_img, benno_rect)

    xpos = 400
    ypos = 200
    
    run = True

    while run:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        

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