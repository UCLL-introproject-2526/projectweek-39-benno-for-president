import pygame
from math import sqrt
from math import tan
import random
from player import Player1,Player2
from weapons import Weapon, Bullet
from enemy import Enemy
from camera import Camera


def main():
    # pygame setup
    pygame.init()
    
    pygame.display.set_caption("Benno vs Santa")
    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    

    # loop setup
    world_time = 0
    world_time2 = 0
    player1 = Player1([200,200], 100, 50) #speed was 3
    player2 = Player2([300,200], 110, 50) #(spawncordinate), speed, health
    cam1 = Camera(1024,834, (2400,2400))    #width, height, mapsize
    rifle = Weapon(15, 0.7, 400) #damage, shootdelay ,bulletspeed, 
    rifle_timer = 0
    fullscreen = False
    Player_lives = 3
    ui_switch = 0
    bullets = []


    # sound:
    pygame.mixer.music.load('sounds/game_track.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)


    # sprites:
    background = pygame.image.load('sprites/icy_background.png').convert()

    heart1 = pygame.image.load('sprites/hearts/l0_hearts1.png').convert_alpha()
    heart1 = pygame.transform.smoothscale(heart1, (45,45))

    heart2 = pygame.image.load('sprites/hearts/l0_hearts1.png').convert_alpha()
    heart2 = pygame.transform.smoothscale(heart2, (45,45))

    heart3 = pygame.image.load('sprites/hearts/l0_hearts1.png').convert_alpha()
    heart3 = pygame.transform.smoothscale(heart3, (45,45))

    crosshair = pygame.image.load('sprites/crosshairs_black.png'). convert_alpha()
    crosshair = pygame.transform.smoothscale(crosshair, (45,45))

    bullet_spr = pygame.image.load('sprites/kogel2.png').convert_alpha()
    bullet_spr = pygame.transform.smoothscale(bullet_spr, (20,20))

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
        # delta time
        dt = clock.tick(60) / 1000  # seconden per frame
        world_time += dt
        rifle_timer += dt
        world_time2 += dt  # fps onafhankelijk
        ui_switch += 1

        # rifle delay check
        rifle_delay = rifle_timer >= rifle.get_rpm()

        # camera update
        cam1.update(player1, player2)

        # animation initialisatie
        movingfront = movingback = False
        movingfront2 = movingback2 = False

        # scherm tekenen
        screen.fill((0, 0, 0))
        screen_pos = cam1.apply(0, 0)
        if cam1.zoom != 1.0:
            new_width = int(background.get_width() * cam1.zoom)
            new_height = int(background.get_height() * cam1.zoom)
            scaled_screen = pygame.transform.scale(background, (new_width, new_height))
            screen.blit(scaled_screen, screen_pos)
        else:
            screen.blit(background, screen_pos)

        # ---- PLAYER MOVEMENT FPS-ONAFHANKELIJK ----
        # Player1 input
        keys = pygame.key.get_pressed()
        dx1 = dy1 = 0
        if keys[pygame.K_q]:
            dx1 -= 1
        if keys[pygame.K_d]:
            dx1 += 1
        if keys[pygame.K_z]:
            dy1 -= 1
        if keys[pygame.K_s]:
            dy1 += 1

        # normaliseer diagonale snelheid
        if dx1 != 0 or dy1 != 0:
            length = (dx1 ** 2 + dy1 ** 2) ** 0.5
            dx1 /= length
            dy1 /= length
            player1.set_cords([
                player1.get_cords()[0] + dx1 * player1.get_speed() * dt,
                player1.get_cords()[1] + dy1 * player1.get_speed() * dt
            ])
            movingfront = dy1 > 0
            movingback = dy1 < 0
            face_me1 = dy1 >= 0

        # Player2 input
        dx2 = dy2 = 0
        if keys[pygame.K_LEFT]:
            dx2 -= 1
        if keys[pygame.K_RIGHT]:
            dx2 += 1
        if keys[pygame.K_UP]:
            dy2 -= 1
        if keys[pygame.K_DOWN]:
            dy2 += 1

        if dx2 != 0 or dy2 != 0:
            length = (dx2 ** 2 + dy2 ** 2) ** 0.5
            dx2 /= length
            dy2 /= length
            player2.set_cords([
                player2.get_cords()[0] + dx2 * player2.get_speed() * dt,
                player2.get_cords()[1] + dy2 * player2.get_speed() * dt
            ])
            movingfront2 = dy2 > 0
            movingback2 = dy2 < 0
            face_me2 = dy2 >= 0

        # draw players
        def draw_player(player, front_sprites, back_sprites, moving_front, moving_back, face_front, current_frame_fr, current_frame_ba):
            pos = player.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])
            if moving_front:
                sprite = front_sprites[int(current_frame_fr)]
            elif moving_back:
                sprite = back_sprites[int(current_frame_ba)]
            else:
                sprite = front_sprites[0] if face_front else back_sprites[0]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                sprite = pygame.transform.scale(sprite, (new_width, new_height))
            screen.blit(sprite, screen_pos)

        draw_player(player1, player1fronts, player1backs, movingfront, movingback, face_me1, current_frame_fr, current_frame_ba)
        draw_player(player2, player2fronts, player2backs, movingfront2, movingback2, face_me2, current_frame_fr2, current_frame_ba2)

        # shooting
        if keys[pygame.K_TAB] and rifle_delay:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_world_x, mouse_world_y = cam1.screen_to_world(mouse_x, mouse_y)
            bullet = Bullet((player1.get_cords()[0]+(20*cam1.zoom), player1.get_cords()[1]+(20*cam1.zoom)),
                (mouse_world_x, mouse_world_y), rifle, world_time)
            
            bullets.append(bullet)
            rifle.reset_timer()
            rifle_timer = 0

        # animation handlers
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

        # bullet updating
        for bullet in bullets[:]:
            bullet.update(dt)
            if not bullet.existing:
                bullets.remove(bullet)
            bullet_x, bullet_y = bullet.get_cords()
            screen_pos = cam1.apply(bullet_x, bullet_y)
            screen.blit(bullet_spr, screen_pos)

        # player enforce bounds
        def enforce_bounds(player):
            x, y = player.get_cords()
            if x < 50: x = 50
            if x > cam1.map_width - 125: x = cam1.map_width - 125
            if y < 45: y = 45
            if y > cam1.map_height - 160: y = cam1.map_height - 160
            player.set_cords([x, y])

        enforce_bounds(player1)
        enforce_bounds(player2)

        # UI handling
        screen.blit(heart1, (cam1.width//2, cam1.height - 771))
        screen.blit(heart2, (cam1.width//2 + 35, cam1.height - 770))
        screen.blit(heart3, (cam1.width//2 - 35, cam1.height - 770))

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((1024, 834), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1024, 834))

        pygame.display.flip()



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
