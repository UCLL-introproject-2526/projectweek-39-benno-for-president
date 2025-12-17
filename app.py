import pygame
from math import sqrt
from math import tan
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
    def __init__(self, dmg, rpm, bullet_speed):
        self.set_dmg(dmg)
        self.set_rpm(rpm)
        self.set_bullet_speed(bullet_speed)


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

    def get_bullet_speed(self):
        return self.__bullet_speed
    
    def set_bullet_speed(self, value):
        if value < 0:
            raise ValueError("weapon bullet speed cannot be negative")
        self.__bullet_speed = value


class Bullet:
    def __init__(self, x, y, name, Weap, target, time1):
        self.__x = x
        self.__y = y
        self.__name = name
        self.set_target(target)
        self.__speed = Weap.get_bullet_speed()
        self.time1 = time1

    def get_cords(self):
        return [self.__x, self.__y]
    
    def get_name(self):
        return self.__name
    
    def get_target(self):
        return self.__target
    
    def set_target(self, value):
        self.__target = value
    
    def get_speed(self):
        return self.__speed

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
    def __init__(self, width, height, map_size):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0, 0, width, height)
        self.map_width = map_size[0]
        self.map_height = map_size[1]
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1
        self.safe_zone = 100



    def dist(self, a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    def update(self, player1, player2): 
        # cam_x = ((player1.get_cords()[0] + player2.get_cords()[0]) /2) #+ mouse_pos[0] ) / 3 #x & y cordinaat 3hoek spelers &muis
        # cam_y = ((player1.get_cords()[1] + player2.get_cords()[1]) /2) #+ mouse_pos[1] ) / 3


        # max_dist = max(self.dist((cam_x, cam_y),player1.get_cords()),
        #                self.dist((cam_x, cam_y),player2.get_cords()),
        #                )

        # target_zoom = 800 / (max_dist + 1)
        # self.zoom = max(0.7, min(1.3, target_zoom))

        # view_w = self.width / self.zoom
        # view_h = self.height / self.zoom
        # safe_x = self.safe_zone / self.zoom
        # safe_y = self.safe_zone / self.zoom
        
        # self.offset.x = cam_x - (self.width / 2)     #offset zodat het middelpunt van 2spelers & muis in het midden van camera is
        # self.offset.y = cam_y - (self.height / 2)

        # left   = self.offset.x + safe_x
        # right  = self.offset.x + view_w - safe_x
        # top    = self.offset.y + safe_y
        # bottom = self.offset.y + view_h - safe_y
    

        # for px, py in (player1.get_cords(), player2.get_cords()):

        #     if px < left:
        #         self.offset.x = px - safe_x
        #     elif px > right:
        #      self.offset.x = px + safe_x - view_w

        #     if py < top:
        #         self.offset.y = py - safe_y
        #     elif py > bottom:
        #         self.offset.y = py + safe_y - view_h

        # self.offset.x = max(0, min(self.offset.x, self.map_width - view_w))
        # self.offset.y = max(0, min(self.offset.y, self.map_height - view_h))

        # view_w = self.width / self.zoom
        # view_h = self.height / self.zoom

        # required_w = max(player1.get_cords()[0], player2.get_cords()[0]) - min(player1.get_cords()[0], player2.get_cords()[0]) + 2 * self.safe_zone
        # required_h = max(player1.get_cords()[1], player2.get_cords()[1]) - min(player1.get_cords()[1], player2.get_cords()[1]) + 2 * self.safe_zone

        # zoom_x = self.width / required_w
        # zoom_y = self.height / required_h

        # new_zoom = min(zoom_x, zoom_y, 1.3)
        # self.zoom = max(new_zoom, 0.7)

        # Haal de coördinaten van beide spelers
        p1 = player1.get_cords()
        p2 = player2.get_cords()

        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])

        min_x -= self.safe_zone
        max_x += self.safe_zone
        min_y -= self.safe_zone
        max_y += self.safe_zone

        required_w = max_x - min_x
        required_h = max_y - min_y
        zoom_x = self.width / required_w
        zoom_y = self.height / required_h
        self.zoom = max(0.7, min(1.3, min(zoom_x, zoom_y)))

        view_w = self.width / self.zoom
        view_h = self.height / self.zoom

        # Center tussen spelers of tegen mapranden
        center_x = (p1[0] + p2[0]) / 2
        center_y = (p1[1] + p2[1]) / 2

        self.offset.x = center_x - view_w / 2
        self.offset.y = center_y - view_h / 2

        # Clamp tegen mapranden
        self.offset.x = max(0, min(self.offset.x, self.map_width - view_w))
        self.offset.y = max(0, min(self.offset.y, self.map_height - view_h))


        # dx = max(0, p2[0] - (self.offset.x + view_w - safe_x), safe_x - (p1[0] - self.offset.x))
        # dy = max(0, p2[1] - (self.offset.y + view_h - safe_y), safe_y - (p1[1] - self.offset.y))
        # if dx > 0 or dy > 0:
        #     self.zoom = min(self.zoom, min(view_w / (view_w + dx), view_h / (view_h + dy)))


    def apply(self, x, y):          #mapcordinaten naar pccordinaten
        return (int((x - self.offset.x) * self.zoom), int((y- self.offset.y) * self.zoom))
    
    def screen_to_world(self, sx, sy):
        return (
            sx / self.zoom + self.offset.x,
            sy / self.zoom + self.offset.y
            )
    #screen_pos = cam.world_to_screen(*placed_object.pos)
    #screen.blit(sprite, screen_pos)



def main():
    # loop setup
    world_time = 0
    player1 = Player1([200,200], 5, 50)
    player2 = Player2([300,200], 5, 50)
    cam1 = Camera(1024,834, (2400,2400))
    rifle = Weapon(15, 0.7, 40)
    rifle_timer = 0
    name_rand = 0
    bullet_dict = {}


    # pygame setup
    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    # sound:
    pygame.mixer.music.load('sounds/lobby_music.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)


    # sprites:
    background = pygame.image.load('sprites/icy_background.png').convert()

    player1_sprite_back = pygame.image.load('sprites/player1/dikkeelfsprite5.png').convert_alpha()
    player1_sprite_back = pygame.transform.smoothscale(player1_sprite_back, (75,75))

    player1_sprite_front = pygame.image.load('sprites/player1/dikkeelfsprite2.png').convert_alpha()
    player1_sprite_front = pygame.transform.smoothscale(player1_sprite_front, (75,75))

    player2_sprite_back = pygame.image.load('sprites/player2/kerstmanachterkant1.png').convert_alpha()
    player2_sprite_back = pygame.transform.smoothscale(player2_sprite_back, (75,75))

    player2_sprite_front = pygame.image.load('sprites/player2/kerstmanfront1.png').convert_alpha()
    player2_sprite_front = pygame.transform.smoothscale(player2_sprite_front, (75,75))
    
    # ------------
    p1img1 = pygame.image.load("sprites/player1/dikkeelfsprite1.png").convert_alpha()
    p1img1 = pygame.transform.smoothscale(p1img1, (75,75))
    
    p1img2 = pygame.image.load("sprites/player1/dikkeelfsprite2.png").convert_alpha()
    p1img2 = pygame.transform.smoothscale(p1img2, (75,75))
    
    p1img3 = pygame.image.load("sprites/player1/dikkeelfsprite3.png").convert_alpha()
    p1img3 = pygame.transform.smoothscale(p1img3, (75,75))
    
    p1img4 = pygame.image.load("sprites/player1/dikkeelfsprite4.png").convert_alpha()
    p1img4 = pygame.transform.smoothscale(p1img4, (75,75))
    
    p1img5 = pygame.image.load("sprites/player1/dikkeelfsprite5.png").convert_alpha()
    p1img5 = pygame.transform.smoothscale(p1img5, (75,75))
    
    p1img6 = pygame.image.load("sprites/player1/dikkeelfsprite6.png").convert_alpha()
    p1img6 = pygame.transform.smoothscale(p1img6, (75,75))
    
    p2img1 = pygame.image.load("sprites/player2/kerstmanachterkant1.png").convert_alpha()
    p2img1 = pygame.transform.smoothscale(p2img1, (75,75))
    
    p2img2 = pygame.image.load("sprites/player2/kerstmanachterkant0.png").convert_alpha()
    p2img2 = pygame.transform.smoothscale(p2img2, (75,75))
    
    p2img3 = pygame.image.load("sprites/player2/kerstmanachterkant2.png").convert_alpha()
    p2img3 = pygame.transform.smoothscale(p2img3, (75,75))
    
    p2img4 = pygame.image.load("sprites/player2/kerstmanfront1.png").convert_alpha()
    p2img4 = pygame.transform.smoothscale(p2img4, (75,75))

    p2img5 = pygame.image.load("sprites/player2/kerstmanfront0.png").convert_alpha()
    p2img5 = pygame.transform.smoothscale(p2img5, (75,75))

    p2img6 = pygame.image.load("sprites/player2/kerstmanfront2.png").convert_alpha()
    p2img6 = pygame.transform.smoothscale(p2img6, (75,75))

    player1fronts = [p1img1,
                    p1img2,
                    p1img3]
    
    player1backs = [p1img4,
                    p1img5,
                    p1img6]

    player2fronts = [p2img4,
                    p2img5,
                    p2img6]
    
    player2backs = [p2img1,
                    p2img2,
                    p2img3]
    
    current_frame_fr = 0
    current_frame_ba = 0
    current_frame_fr2 = 0
    current_frame_ba2 = 0
    animation_speed = 0.2
    face_me1 = False
    face_me2 = False

    # benno_img = pygame.image.load('sprites/bigbenno_sprite.png').convert_alpha()
    # benno_img = pygame.transform.smoothscale(benno_img, (100, 100))

    # game loop
    run = True
    while run:
        # variables
        world_time += 1/60
        rifle_timer += 1/60
        if rifle_timer >= rifle.get_rpm():
            rifle_delay = True
        else: rifle_delay = False

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

        # player 1 shooting
        if key[pygame.K_TAB] and rifle_delay == True:
            last_cursor = list(pygame.mouse.get_pos())
            bullet = Bullet(cam1.screen_to_world()[0], cam1.screen_to_world()[1], f"bullet{name_rand}", rifle, last_cursor, world_time)
            name_rand += 1
            bullet_spr = pygame.image.load("sprites/Bullet.png").convert_alpha()
            bullet_spr = pygame.transform.smoothscale(bullet_spr, (5,25))
            bullet_spr = pygame.transform.rotate(bullet_spr, tan((bullet.get_target()[0] - player1.get_cords()[0]) /bullet.get_target()[1] - player1.get_cords()[1] ))
            bullet_dict[bullet] = bullet_spr
            rifle_timer = 0
            

        # for bul, spr in bullet_dict.items():
        #     screen.blit(spr, [bul.get_cords()[0] + ] )



        # player 2
        key2 = pygame.key.get_pressed()
        if key2[pygame.K_DOWN] and key2[pygame.K_LEFT]:
            player2.move("dl")
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

        elif key2[pygame.K_DOWN] and key2[pygame.K_RIGHT]:
            player2.move("dr")
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