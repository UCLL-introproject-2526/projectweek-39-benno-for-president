import pygame
from math import sqrt
from math import tan
import random
from player import Player1,Player2
from weapons import Weapon, Bullet
from enemy import Enemy
from camera import Camera
from health 

def main():
    # pygame setup
    pygame.init()
    
    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    

    # loop setup
    world_time = 0
    player1 = Player1([200,200], 5, 50)
    player2 = Player2([300,200], 5, 50)
    cam1 = Camera(1024,834, (2400,2400))
    rifle = Weapon(15, 0.7, 40)
    rifle_timer = 0
    name_rand = 0
    bullet_dict = {}
    fullscreen = False
    Player_lives = 3


    # sound:
    pygame.mixer.music.load('sounds/benno_song.ogg')
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

                # enforce map bounds
        if 50 > player1.get_cords()[0]:
            player1.set_cords([player1.get_cords()[0] + 5, player1.get_cords()[1]])
        if cam1.map_width - 125 < player1.get_cords()[0]:
            player1.set_cords([player1.get_cords()[0] - 5, player1.get_cords()[1]])
        if 45 > player1.get_cords()[1]:
            player1.set_cords([player1.get_cords()[0], player1.get_cords()[1] + 5])
        if cam1.map_height - 160 < player1.get_cords()[1]:
            player1.set_cords([player1.get_cords()[0], player1.get_cords()[1] - 5])
        

        if 50 > player2.get_cords()[0]:
            player2.set_cords([player2.get_cords()[0] + 5, player2.get_cords()[1]])
        if cam1.map_width - 125 < player2.get_cords()[0]:
            player2.set_cords([player2.get_cords()[0] - 5, player2.get_cords()[1]])
        if 45 > player2.get_cords()[1]:
            player2.set_cords([player2.get_cords()[0], player2.get_cords()[1] + 5])
        if cam1.map_height - 160 < player2.get_cords()[1]:
            player2.set_cords([player2.get_cords()[0], player2.get_cords()[1] - 5])
        
   
        screen.blit(heart,(cam1.width - 924, cam1.height - 734))

        # event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fullscreen = not fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode(screen_size)


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





    #  camera update dinges
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