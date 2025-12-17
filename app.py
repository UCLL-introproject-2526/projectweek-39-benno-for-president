import pygame
from math import sqrt
import random

pygame.init()


Player_lives = 3

class Player1:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True
    
    def alive(self):
        return self.__alive

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
        if self.__health <= 0:
            self.__alive = False

    def get_cords(self):
        return [self.__x, self.__y]
    
    def set_cords(self, list_inp):
        if isinstance(list_inp, list):
            if len(list_inp) != 2:
                raise ValueError("player 1 cords cannot be empty")
            self.__x = list_inp[0]
            self.__y = list_inp[1]
        else:
            raise ValueError("player 1 cords have to be list")
        
    def move(self, key):
        diag = self.__speed / sqrt(2)
        
        if key == "q":
            self.set_cords([self.get_cords()[0] - self.__speed,self.get_cords()[1]])
        if key == "d":
            self.set_cords([self.get_cords()[0] + self.__speed,self.get_cords()[1]])
        if key == "z":
            self.set_cords([self.get_cords()[0], self.get_cords()[1] - self.__speed])
        if key == "s":            
            self.set_cords([self.get_cords()[0], self.get_cords()[1] + self.__speed])
        if key == "sq":
            self.set_cords([self.get_cords()[0] - diag, self.get_cords()[1] + diag ])
        if key == "sd":
            self.set_cords([self.get_cords()[0] + diag, self.get_cords()[1] + diag ])
        if key == "zq":
            self.set_cords([self.get_cords()[0] - diag, self.get_cords()[1] - diag ])
        if key == "zd":
            self.set_cords([self.get_cords()[0] + diag, self.get_cords()[1] - diag ])
        

class Player2:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True

    def alive(self):
        return self.__alive

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
        if self.__health <= 0:
            self.__alive = False

    def get_cords(self):
        return [self.__x, self.__y]
    
    def set_cords(self, list_inp):
        if isinstance(list_inp, list):
            if len(list_inp) != 2:
                raise ValueError("player 2 cords cannot be empty")
            self.__x = list_inp[0]
            self.__y = list_inp[1]
        else:
            raise ValueError("player 2 cords have to be list")
    
    def move(self, key):
        diag = self.__speed / sqrt(2)
        
        if key == "left":
            self.set_cords([self.get_cords()[0] - self.__speed,self.get_cords()[1]])
        if key == "right":
            self.set_cords([self.get_cords()[0] + self.__speed,self.get_cords()[1]])
        if key == "up":
            self.set_cords([self.get_cords()[0], self.get_cords()[1] - self.__speed])
        if key == "down":            
            self.set_cords([self.get_cords()[0], self.get_cords()[1] + self.__speed])
        if key == "dl":
            self.set_cords([self.get_cords()[0] - diag, self.get_cords()[1] + diag ])
        if key == "dr":
            self.set_cords([self.get_cords()[0] + diag, self.get_cords()[1] + diag ])
        if key == "ul":
            self.set_cords([self.get_cords()[0] - diag, self.get_cords()[1] - diag ])
        if key == "ur":
            self.set_cords([self.get_cords()[0] + diag, self.get_cords()[1] - diag ])

class Weapon:
    def __init__(self, dmg, rpm, spread):
        self.set_dmg(dmg)
        self.set_rpm(rpm)
        self.set_spread(spread)


    def get_dmg(self):
        return self.__dmg

    def set_dmg(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("weapon dmg cannot be negative")
            self.__dmg = value
        else:
            raise ValueError("weapon dmg must be int")
            
    def get_rpm(self):
        return self.__rpm
    
    def set_rpm(self, value):
        if value < 0:
            raise ValueError("weapon rpm cannot be negative")
        self.__rpm = value


    def get_spread(self):
        return self.__spread
    
    def set_spread(self, value):
        if value < 0:
            raise ValueError("weapon spread cannot be negative")
        self.__spread = value

class Enemy:
    def __init__(self, cords, speed, health, dmg):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.set_dmg(dmg)
        self.__alive = True
    
    def get_cords(self):
        return [self.__x, self.__y]

    def set_cords(self, list_inp):
        if not isinstance(list_inp, list):
            if not  len(list_inp) == 2:
                raise ValueError("enemy cords cannot be empty and has to be list")
            
        self.__x = list_inp[0]
        self.__y = list_inp[1]

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

    def get_alive(self):
        return self.__alive

    def get_closest(self, player1, player2):
        if sqrt((self.__x - player1.get_cords[0])**2 + (self.__y - player1.get_cords[1])**2) < sqrt((self.__x - player2.get_cords[0])**2 + (self.__y - player2.get_cords[1])**2):
            return player1
        else:
            return player2

    def move(self, player):
        if self.__x < player.get_cords[0]:
            self.__x =+ self.get_speed()
        else:
            self.__x =- self.get_speed()

        if self.__y < player.get_cords[1]:
            self.__y =+ self.get_speed()
        else:
            self.__y =- self.get_speed()


    def hit(self, other):
        diff = max(0, self.__health - other.get_dmg())
        self.set_health(diff)
        if self.__health <= 0:
            self.__alive = False


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0, 0, width, height)
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1

    def dist(self, a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    def update(self, player1, player2): 
        mouse_pos = list(pygame.mouse.get_pos())
        cam_x = (player1.get_cords()[0] + player2.get_cords()[0] /2) #+ mouse_pos[0] ) / 3 #x & y cordinaat 3hoek spelers &muis
        cam_y = (player1.get_cords()[1] + player2.get_cords()[1] /2) #+ mouse_pos[1] ) / 3

        self.offset.x = cam_x - self.width / 2      #offset zodat het middelpunt van 2spelers & muis in het midden van camera is
        self.offset.y = cam_y - self.height / 2


        max_dist = max(self.dist((cam_x, cam_y),player1.get_cords()),
                       self.dist((cam_x, cam_y),player2.get_cords()),
                       )

        target_zoom = 400 / (max_dist + 1)
        #target_zoom = 800 / (max_dist + 1)

        self.zoom = max(0.5, min(1.3, target_zoom))

    def apply(self, x, y):          #mapcordinaten naar pccordinaten
        return ((x - self.offset.x) * self.zoom, (y- self.offset.y) * self.zoom)
    


player1 = Player1([400,200], 5, 50)
player2 = Player2([600,200], 5, 50)
cam1 = Camera(1024,834)


def main():
    # pygame setup
    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    # sound:
    pygame.mixer.music.load('sounds/lobby_music.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)


    # sprites:
    background = pygame.image.load('sprites/icy_background.png').convert()

    player1_sprite_back = pygame.image.load('sprites/player1/kerstmanachterkant1.png')
    player1_sprite_front = pygame.image.load('sprites/player1/kerstmanfront1.png')

    player2_sprite_back = pygame.image.load('sprites/player2/dikkeelfsprite5.png')
    player2_sprite_front = pygame.image.load('sprites/player2/dikkeelfsprite2.png')

    player1fronts = [pygame.image.load("sprites/player1/kerstmanfront1.png").convert_alpha(),
                          pygame.image.load("sprites/player1/kerstmanfront0.png").convert_alpha(),
                          pygame.image.load("sprites/player1/kerstmanfront2.png").convert_alpha(),]
    
    player1backs = [pygame.image.load("sprites/player1/kerstmanachterkant1.png").convert_alpha(),
                          pygame.image.load("sprites/player1/kerstmanachterkant0.png").convert_alpha(),
                          pygame.image.load("sprites/player1/kerstmanachterkant2.png").convert_alpha(),]
    player2fronts = [pygame.image.load("sprites/player2/dikkeelfsprite1.png").convert_alpha(),
                          pygame.image.load("sprites/player2/dikkeelfsprite2.png").convert_alpha(),
                          pygame.image.load("sprites/player2/dikkeelfsprite3.png").convert_alpha(),]
    
    player2backs = [pygame.image.load("sprites/player2/dikkeelfsprite4.png").convert_alpha(),
                          pygame.image.load("sprites/player2/dikkeelfsprite5.png").convert_alpha(),
                          pygame.image.load("sprites/player2/dikkeelfsprite6.png").convert_alpha(),]
    
    current_frame_fr = 0
    current_frame_ba = 0
    current_frame_fr2 = 0
    current_frame_ba2 = 0
    animation_speed = 0.09
    face_me1 = False
    face_me2 = False

    # benno_img = pygame.image.load('sprites/bigbenno_sprite.png').convert_alpha()
    # benno_img = pygame.transform.smoothscale(benno_img, (100, 100))

    # game loop
    run = True
    while run:
        # camera
        cam1.update(player1, player2)


        # animation initialisatie
        movingfront = False
        movingback = False
        movingfront2 = False
        movingback2 = False

        # scherm tekenen
        screen.fill((0,0,0))
        screen_pos = cam1.apply(0,0)
        if cam1.zoom != 1.0:
            new_width = int(background.get_width() * cam1.zoom)
            new_height = int(background.get_height() * cam1.zoom)
            scaled_screen = pygame.transform.scale(background, (new_width, new_height))
            screen.blit(scaled_screen, screen_pos)
        else:
            screen.blit(background, screen_pos)
        

        # player 1
        key = pygame.key.get_pressed()
        if key[pygame.K_s] and key[pygame.K_q]:
            player1.move("sq")
            movingfront = True
            face_me1 = True
            #screen.blit(player1fronts[int(current_frame_fr)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1fronts[int(current_frame_fr)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_s] and key[pygame.K_d]:
            player1.move("sd")
            movingfront = True
            face_me1 = True
            #screen.blit(player1fronts[int(current_frame_fr)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1fronts[int(current_frame_fr)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_z] and key[pygame.K_q]:
            player1.move("zq")
            movingback = True
            face_me1 = False
            #screen.blit(player1backs[int(current_frame_ba)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1backs[int(current_frame_ba)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_z] and key[pygame.K_d]:
            player1.move("zd")
            movingback = True
            face_me1 = False
            #screen.blit(player1backs[int(current_frame_ba)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1backs[int(current_frame_ba)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_d]:
            player1.move("d")
            movingfront = True
            #screen.blit(player1fronts[int(current_frame_fr)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1fronts[int(current_frame_fr)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_q]:
            player1.move("q")
            movingfront = True
            #screen.blit(player1fronts[int(current_frame_fr)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1fronts[int(current_frame_fr)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_s]:
            player1.move("s")
            movingfront = True
            face_me1 = True
            #screen.blit(player1fronts[int(current_frame_fr)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1fronts[int(current_frame_fr)]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key[pygame.K_z]:
            player1.move("z")
            movingback = True
            face_me1 = False
            #screen.blit(player1backs[int(current_frame_ba)], player1.get_cords())
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player1backs[int(current_frame_ba)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        
        else:
            pos = player1.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            if face_me1:
                sprite = player1_sprite_front
            else:
                sprite = player1_sprite_back
    
        if cam1.zoom != 1.0:
            new_width = int(sprite.get_width() * cam1.zoom)
            new_height = int(sprite.get_height() * cam1.zoom)
            scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
            screen.blit(scaled_sprite, screen_pos)
        else:
            screen.blit(sprite, screen_pos)

        # player 2
        key2 = pygame.key.get_pressed()
        if key2[pygame.K_DOWN] and key2[pygame.K_LEFT]:
            player2.move("dl")
            movingback2 = True
            face_me2 = True
            #screen.blit(player2fronts[int(current_frame_fr2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2fronts[int(current_frame_fr2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_DOWN] and key2[pygame.K_RIGHT]:
            player2.move("dr")
            movingback2 = True
            face_me2 = True
            #screen.blit(player2fronts[int(current_frame_fr2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2fronts[int(current_frame_fr2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_UP] and key2[pygame.K_LEFT]:
            player2.move("ul")
            movingback2 = True
            face_me2 = False
            #screen.blit(player2backs[int(current_frame_ba2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2backs[int(current_frame_ba2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_UP] and key2[pygame.K_RIGHT]:
            player2.move("ur")
            movingback2 = True
            face_me2 = False
            #screen.blit(player2backs[int(current_frame_ba2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2backs[int(current_frame_ba2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)
        elif key2[pygame.K_RIGHT]:
            player2.move("right")
            movingfront2 = True
            #screen.blit(player2fronts[int(current_frame_fr2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2fronts[int(current_frame_fr2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_LEFT]:
            player2.move("left")
            movingfront2 = True
            #screen.blit(player2fronts[int(current_frame_fr2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2fronts[int(current_frame_fr2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_DOWN]:
            player2.move("down")
            movingfront2 = True
            face_me2 = True
            #screen.blit(player2fronts[int(current_frame_fr2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2fronts[int(current_frame_fr2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)

        elif key2[pygame.K_UP]:
            player2.move("up")
            movingback2 = True
            face_me2 = False
            #screen.blit(player2backs[int(current_frame_ba2)], player2.get_cords())
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            sprite = player2backs[int(current_frame_ba2)]
            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
                screen.blit(scaled_sprite, screen_pos)
            else:
                screen.blit(sprite, screen_pos)
        
        else:
            pos = player2.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            if face_me2:
                sprite = player2_sprite_front
            else:
                sprite = player2_sprite_back
    
        if cam1.zoom != 1.0:
            new_width = int(sprite.get_width() * cam1.zoom)
            new_height = int(sprite.get_height() * cam1.zoom)
            scaled_sprite = pygame.transform.scale(sprite, (new_width, new_height))
            screen.blit(scaled_sprite, screen_pos)
        else:
            screen.blit(sprite, screen_pos)
        # animation handler 1
        if movingfront:
            current_frame_fr += animation_speed
            if current_frame_fr >= len(player1fronts):
                current_frame_fr = 0
        else:
            current_frame_fr = 0

        if movingback:
            current_frame_ba += animation_speed
            if current_frame_ba >= len(player1backs):
                current_frame_ba = 0
        else:
            current_frame_ba = 0
        
        # animation handler 2
        if movingfront2:
            current_frame_fr2 += animation_speed
            if current_frame_fr2 >= len(player2fronts):
                current_frame_fr2 = 0
        else:
            current_frame_fr2 = 0

        if movingback2:
            current_frame_ba2 += animation_speed
            if current_frame_ba2 >= len(player2backs):
                current_frame_ba2 = 0
        else:
            current_frame_ba2 = 0

        

        # event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        clock.tick(60)
        pygame.display.flip()
    
    pygame.quit()


main()



    # def render_frame(surface, xpos, ypos):
    #     benno_rect = benno_img.get_rect(center = [xpos, ypos])
    #     surface.blit(benno_img, benno_rect)

    # xpos = 400
    # ypos = 200


    #  render_frame(screen, xpos, ypos)