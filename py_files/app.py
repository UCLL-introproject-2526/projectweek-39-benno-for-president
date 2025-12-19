import pygame
from math import sqrt
from math import tan
import random
from player import Player1,Player2
from weapons import Weapon, Bullet
from enemy import Enemy
from camera import Camera
from random import randint, choice

def get_player_hitbox(player, cam, base_size=35, offset=(0, 0)):
    

    size = int(base_size * cam.zoom)
    rect = pygame.Rect(0, 0, size, size)
    rect.center = (
        int(player.get_cords()[0] + offset[0]),
        int(player.get_cords()[1] + offset[1])
    )
    return rect


def spawn_location(p1, p2, small_border, big_border):
        x_min = min(p1[0], p2[0])
        x_max = max(p1[0], p2[0])
        y_min = min(p1[1], p2[1])
        y_max = max(p1[1], p2[1])

        inner = pygame.Rect(
            x_min - small_border,
            y_min - small_border,
            (x_max - x_min) + 2 * small_border,
            (y_max - y_min) + 2 * small_border
        )

        outer = pygame.Rect(
            x_min - big_border,
            y_min - big_border,
            (x_max - x_min) + 2 * big_border,
            (y_max - y_min) + 2 * big_border
        )

        zones = ["top", "bottom", "left", "right"]
        side = choice(zones)

        if side == "top":
            x = randint(outer.left, outer.right)
            y = randint(outer.top, inner.top)

        elif side == "bottom":
            x = randint(outer.left, outer.right)
            y = randint(inner.bottom, outer.bottom)

        elif side == "left":
            x = randint(outer.left, inner.left)
            y = randint(inner.top, inner.bottom)

        else:  # right
            x = randint(inner.right, outer.right)
            y = randint(inner.top, inner.bottom)

        return (int(x), int(y))

def main():
    # pygame setup
    pygame.init()

    pygame.display.set_caption("Benno vs Santa")
    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.scrap.init()
    pygame.font.init()
    

    # loop setup
    world_time = 0
    world_time2 = 0
    player1 = Player1([200,200], 100, 50) #speed was 3
    player2 = Player2([300,200], 125, 50) #(spawncordinate), speed, health
    cam1 = Camera(1024,834, (2400,2400))    #width, height, mapsize
    rifle = Weapon(15, 0.7, 400) #damage, shootdelay ,bulletspeed, 
    rifle_timer = 0
    fullscreen = False
    Player_lives = 3
    enemy_count = 0
    ui_switch = 0
    bullets = []
    spawned = False
    current_wave_finished = True
    wave_start = False
    hit_timer = 0
    current_wave = 1


    # sound:
    pygame.mixer.music.load('sounds/music/game_track.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)
    pygame.mixer.music.set_volume(0.7)

    shoot_sound = pygame.mixer.Sound("sounds/sound_effects/shoot_sound.mp3")
    shoot_sound.set_volume(0.5)

    wave_sound = pygame.mixer.Sound("sounds/sound_effects/new_wave.mp3")
    wave_sound.set_volume(0.1)



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

    E1 = pygame.image.load('sprites/enemies/enemy_front1.png').convert_alpha()
    E1 = pygame.transform.smoothscale(E1, (60,60))

    E2 = pygame.image.load('sprites/enemies/enemy_front2.png').convert_alpha()
    E2 = pygame.transform.smoothscale(E2, (60,60))

    E3 = pygame.image.load('sprites/enemies/enemy_front3.png').convert_alpha()
    E3 = pygame.transform.smoothscale(E3, (60,60))

    E4 = pygame.image.load('sprites/enemies/enemy_back1.png').convert_alpha()
    E4 = pygame.transform.smoothscale(E4, (60,60))

    E5 = pygame.image.load('sprites/enemies/enemy_back2.png').convert_alpha()
    E5 = pygame.transform.smoothscale(E5, (60,60))

    E6 = pygame.image.load('sprites/enemies/enemy_back3.png').convert_alpha()
    E6 = pygame.transform.smoothscale(E6, (60,60))

    enemy_fronts = [E1,
                    E2,
                    E3]
    
    enemy_backs = [E4,
                   E5,
                   E6]
    
    Benno_Boss_Controler = pygame.image.load('sprites/enemies/bigbenno_final_boss.png').convert_alpha()
    Benno_Boss_Controler = pygame.transform.smoothscale(Benno_Boss_Controler, (150,150))

    # ------------
    player1_sprite_back = pygame.image.load('sprites/player1/dikkeelfsprite5.png').convert_alpha()
    player1_sprite_back = pygame.transform.smoothscale(player1_sprite_back, (75,75))

    player1_sprite_front = pygame.image.load('sprites/player1/dikkeelfsprite2.png').convert_alpha()
    player1_sprite_front = pygame.transform.smoothscale(player1_sprite_front, (75,75))

    player2_sprite_back = pygame.image.load('sprites/player2/kerstmanachterkant1.png').convert_alpha()
    player2_sprite_back = pygame.transform.smoothscale(player2_sprite_back, (75,75))

    player2_sprite_front = pygame.image.load('sprites/player2/kerstmanfront1.png').convert_alpha()
    player2_sprite_front = pygame.transform.smoothscale(player2_sprite_front, (75,75))
    

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
    current_frame_fr_enemy = 0
    current_frame_ba_enemy = 0
    animation_speed = 0.2
    enemy_animation_speed = 0.4
    face_me1 = False
    face_me2 = False
    face_me_enemy = False
    hit_timer1 = 0
    hit_timer2 = 0
    wave_timer = 0

    enemies = []

    # writing function
    def write(text, text_col, x, y):
        img = pygame.font.Font("Nothing Smoothie.ttf", 50).render(text, True, text_col)
        screen.blit(img, (x,y))


    # benno_img = pygame.image.load('sprites/bigbenno_sprite.png').convert_alpha()
    # benno_img = pygame.transform.smoothscale(benno_img, (100, 100))
    
    # game loop
    run = True
    while run:
        # variables
        dt = clock.tick(60) / 1000  # seconden per frame
        world_time += dt
        rifle_timer += dt
        world_time2 += dt  # fps onafhankelijk
        ui_switch += 1
        if rifle_timer >= rifle.get_rpm(): 
            rifle_delay = True 
        else: 
            rifle_delay = False
        wave_timer += 1 * dt
        hit_timer1 += 1 * dt
        hit_timer2 += 1 * dt


        # camera update
        cam1.update(player1, player2)


        # animation initialisatie
        movingfront_enemy = False
        movingback_enemy = False
        movingfront = movingback = False
        movingfront2 = movingback2 = False

        def draw_enemy(enemy, front_sprites, back_sprites, moving_front, moving_back, face_front, current_frame_fr, current_frame_ba):
            pos = enemy.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])

            if moving_front:
                sprite = front_sprites[int(current_frame_fr)]
            elif moving_back:
                sprite = back_sprites[int(current_frame_ba)]
            else:
                if face_front:
                    sprite = front_sprites[0]
                else:
                    sprite = back_sprites[0]

            if cam1.zoom != 1.0:
                new_width = int(60 * cam1.zoom)
                new_height = int(60 * cam1.zoom)
                sprite = pygame.transform.scale(sprite, (new_width, new_height))

            screen.blit(sprite, screen_pos)


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
        

        # cursor verbergen
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)


        # enemy looping
        # wave checking
        if enemy_count == 0 and wave_timer >= 15 and current_wave_finished:

            if current_wave == 1:
                if wave_start == False:
                    Title_timer = 0
                    wave_start = True
                    spawned = False
                    
                wave_sound.play()
                
                if Title_timer <= 3:
                    write(f"wave {current_wave} starting", (0,0,0), cam1.width // 2 - 100, cam1.height // 2 - 300)
                    Title_timer += 1 * dt
                else:
                    enemy_count = (current_wave + 2 )** 2
                    current_wave_finished = False
                    


                    if enemy_count == 0 and not current_wave_finished:
                        current_wave += 1
                        wave_timer = 0
                        wave_start = False
                        current_wave_finished = True


            elif current_wave == 2:
                if wave_start == False:
                    Title_timer = 0
                    wave_start = True
                    spawned = False
                    
                wave_sound.play()
                
                if Title_timer <= 3:
                    write(f"wave {current_wave} starting", (0,0,0), cam1.width // 2 - 100, cam1.height // 2 - 300)
                    Title_timer += 1 * dt
                else:
                    enemy_count = 0
                    # enemy_count = (current_wave + 2 )** 2
                    current_wave_finished = False
                    


                    if enemy_count == 0 and not current_wave_finished:
                        current_wave += 1
                        wave_timer = 0
                        wave_start = False
                        current_wave_finished = True


            elif current_wave > 2:
                if wave_start == False:
                    Title_timer = 0
                    wave_start = True
                    spawned = False
                    
                wave_sound.play()
                
                if Title_timer <= 3:
                    write(f"wave {current_wave} starting", (0,0,0), cam1.width // 2 - 100, cam1.height // 2 - 300)
                    Title_timer += 1 * dt
                else:
                    enemy_count = 0
                    # enemy_count = (current_wave + 2 )** 2
                    current_wave_finished = False
                    


                    if enemy_count == 0 and not current_wave_finished:
                        current_wave += 1
                        wave_timer = 0
                        wave_start = False
                        current_wave_finished = True


        


        # player movement
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
        
        # movement kanker 1
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

            # sideways animations:
            if keys[pygame.K_d] and not keys[pygame.K_z]:
                movingfront = True
            elif keys[pygame.K_q] and not keys[pygame.K_z]:
                movingfront = True
            
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

        # movment kanker 2
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

            # sideways
            if keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
                movingfront2 = True
            elif keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
                movingfront2 = True

        # draw players
        def draw_player(player, front_sprites, back_sprites, moving_front, moving_back, face_front, current_frame_fr, current_frame_ba):
            pos = player.get_cords()
            screen_pos = cam1.apply(pos[0], pos[1])

            if moving_front:
                sprite = front_sprites[int(current_frame_fr)]
            elif moving_back:
                sprite = back_sprites[int(current_frame_ba)]
            else:
                if face_front:
                    sprite = front_sprites[0]
                else:
                    sprite = back_sprites[0]

            if cam1.zoom != 1.0:
                new_width = int(sprite.get_width() * cam1.zoom)
                new_height = int(sprite.get_height() * cam1.zoom)
                sprite = pygame.transform.scale(sprite, (new_width, new_height))
            screen.blit(sprite, screen_pos)

        if player1.alive():
            draw_player(player1, player1fronts, player1backs, movingfront, movingback, face_me1, current_frame_fr, current_frame_ba)
        if player2.alive():
            draw_player(player2, player2fronts, player2backs, movingfront2, movingback2, face_me2, current_frame_fr2, current_frame_ba2)


        # player enforce bounds
        def enforce_bounds(player, other):
            x, y = player.get_cords()
            if x < 50: x = 50
            if x > cam1.map_width - 125: x = cam1.map_width - 125
            if y < 45: y = 45
            if y > cam1.map_height - 160: y = cam1.map_height - 160

            # player seperation
            if x > other.get_cords()[0] + 950: x = other.get_cords()[0] + 950
            if x < other.get_cords()[0] - 950: x = other.get_cords()[0] - 950
            if y > other.get_cords()[1] + 950: y = other.get_cords()[1] + 950
            if y < other.get_cords()[1] - 950: y = other.get_cords()[1] - 950

            player.set_cords([x, y])

        enforce_bounds(player1, player2)
        enforce_bounds(player2, player1)


        # shooting
        if keys[pygame.K_TAB] and rifle_delay:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_world_x, mouse_world_y = cam1.screen_to_world(mouse_x, mouse_y)
            bullet = Bullet((player1.get_cords()[0]+(20*cam1.zoom), player1.get_cords()[1]+(20*cam1.zoom)),
                (mouse_world_x, mouse_world_y), rifle, world_time)
            
            bullets.append(bullet)
            shoot_sound.play()  
            rifle.reset_timer()
            rifle_timer = 0


        #player hitboxes
        p1_hitbox = get_player_hitbox(player1, cam1, base_size=35, offset=(37, 45))   
        

        p2_hitbox = get_player_hitbox(player2, cam1, base_size=35, offset=(37, 45))

        for enemy in enemies[:]:
            target = enemy.get_closest(player1, player2)
            enemy.move(target, dt)

            # enemy hitbox
            e_size = int(25 * cam1.zoom)
            enemy_rect = pygame.Rect(0, 0, e_size, e_size)
            enemy_rect.center = (
                int(enemy.get_cords()[0] + 15),
                int(enemy.get_cords()[1] + 30)
            )

            # collision met player 1
            if enemy_rect.colliderect(p1_hitbox) and hit_timer1 > 1:
                player1.hit(enemy.get_dmg())  # of whatever je functie heet
                print(player1.get_health())
                hit_timer1 = 0

            # collision met player 2
            if enemy_rect.colliderect(p2_hitbox) and hit_timer2 > 1:
                player2.hit(int(enemy.get_dmg()))
                print(player2.get_health())
                hit_timer2 = 0

            draw_enemy(
                enemy,
                enemy_fronts,
                enemy_backs,
                movingfront_enemy,
                movingback_enemy,
                face_me_enemy,
                current_frame_fr_enemy,
                current_frame_ba_enemy
            )


        # bullet updating
        # bullet updating loop
        for bullet in bullets[:]:
            bullet.update(dt)
            
            # 1. Maak een TIJDELIJKE kogel-hitbox die meeschaalt
            # Stel de originele kogel is 10 pixels breed
            b_size = max(2, int(6 * cam1.zoom)) 
            scaled_bullet_rect = pygame.Rect(0, 0, b_size, b_size)
            scaled_bullet_rect.center = (int(bullet.pos.x), int(bullet.pos.y))

            base_enemy_size = 25
            e_size = int(base_enemy_size * cam1.zoom) 

            for enemy in enemies[:]:
                # 3. Maak een TIJDELIJKE vijand-hitbox
                collision_rect = pygame.Rect(0, 0, e_size, e_size)
                collision_rect.center = (int(enemy.get_cords()[0]+ 15), int(enemy.get_cords()[1]+ 30))

                # 4. Check collision tussen de twee GESCHAALDE rects
                if scaled_bullet_rect.colliderect(collision_rect):
                    enemy.hit(bullet.damage)
                    bullet.existing = False
                    if not enemy.get_alive():
                        enemies.remove(enemy)
                        enemy_count -= 1
                        print(enemy_count)
                    break 

            if not bullet.existing:
                if bullet in bullets: bullets.remove(bullet)
                continue

            # Tekenen
            bullet_screen_pos = cam1.apply(bullet.pos.x, bullet.pos.y)
            screen.blit(bullet_spr, bullet_screen_pos)

        # for bullet in bullets[:]: 
        #     bullet.update(dt) # Hier wordt self.pos bijgewerkt
        #     scaled_size = int(60 * cam1.zoom)
        #     # Check of de kogel nog in de lijst zit en bestaat
        #     if not bullet.existing:
        #         if bullet in bullets: bullets.remove(bullet)
        #         continue

        #     # Gebruik de functie die je al hebt gemaakt om de error te voorkomen
        #     # Dit haalt de [x, y] lijst op uit je kogel klasse
        #     cords = bullet.get_cords() 
        #     current_bullet_x = cords[0]
        #     current_bullet_y = cords[1]

        #     # Collision check
        #     for enemy in enemies:
        #         scaled_rect = pygame.Rect(0, 0, scaled_size, scaled_size)
                
        #         if bullet.rect.colliderect(enemy.rect):
        #             enemy.hit(bullet.damage)
        #             bullet.existing = False
        #             if not enemy.get_alive():
        #                 enemies.remove(enemy)
        #                 enemy_count -= 1
        #             break

        #     if not bullet.existing:
        #         if bullet in bullets: bullets.remove(bullet)
        #         continue

        #     # TEKENEN
        #     # We gebruiken hier de lokale variabelen die we net gevuld hebben
        #     bullet_screen_pos = cam1.apply(current_bullet_x, current_bullet_y)
        #     screen.blit(bullet_spr, bullet_screen_pos)

  


        # enemy spawn loop
        if enemy_count != 0 and wave_start and spawned == False and current_wave <= 2: 
            for i in range(0, enemy_count):
                enemy = Enemy((spawn_location(player1.get_cords(), player2.get_cords(), 700, 1100)), 40, 20, 20)
                #enemy.set_cords(enemy.spawn_location(player1.get_cords(), player2.get_cords(), 700, 1100))
                print(enemy.get_cords())
                enemies.append(enemy)
            spawned = True

        if enemy_count != 0 and wave_start and spawned == False and current_wave > 2: 
            for i in range(0, enemy_count):
                enemy = Enemy((spawn_location(player1.get_cords(), player2.get_cords(), 700, 1100)), 40, 20, 10)
                #enemy.set_cords(enemy.spawn_location(player1.get_cords(), player2.get_cords(), 700, 1100))
                print(enemy.get_cords())
                enemies.append(enemy)
            spawned = True

        for enemy in enemies:
            target = enemy.get_closest(player1, player2)
            enemy.move(target, dt)
            draw_enemy(enemy, enemy_fronts, enemy_backs, movingfront_enemy, movingback_enemy, face_me_enemy, current_frame_fr_enemy, current_frame_ba_enemy)
        


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

        
        # UI handling
        screen.blit(heart1, (cam1.width//2 + 75, cam1.height - 771))
        screen.blit(heart2, (cam1.width//2 + 50, cam1.height - 770))
        screen.blit(heart3, (cam1.width//2  + 25, cam1.height - 770))

        
        #dood

        if not player1.alive() and not player2.alive():
            pygame.mouse.set_visible(True)
            class Button:
                def __init__(self, pos, image, hover_image, on_click, click_sound=None, click_delay_ms=300):
                    self.image = image
                    self.hover_image = hover_image
                    self.on_click = on_click
                    self.click_sound = click_sound
                    self.click_delay_ms = click_delay_ms

                    self.rect = self.image.get_rect(topleft=pos)
                    self.hover = False

                def handle_event(self, event):
                    if event.type == pygame.MOUSEMOTION:
                        self.hover = self.rect.collidepoint(event.pos)

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.rect.collidepoint(event.pos):
                            if self.click_sound:
                                self.click_sound.play()
                            if self.click_delay_ms:
                                pygame.time.delay(self.click_delay_ms)

                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if self.rect.collidepoint(event.pos):
                            self.on_click()

                def draw(self, surf):
                    surf.blit(self.hover_image if self.hover else self.image, self.rect)


            class EndScreen:
                """
                Gebruik:
                    endscreen = EndScreen(screen, width, height)
                    ...
                    if player.dead:
                        endscreen.show()
                    ...
                    for event in pygame.event.get():
                        endscreen.handle_event(event)
                    ...
                    # teken altijd eerst je gameplay:
                    draw_gameplay()
                    # en dan pas:
                    endscreen.draw()
                """

                def __init__(
                    self,
                    screen: pygame.Surface,
                    width: int,
                    height: int,
                    overlay_alpha: int = 170,
                    title_text: str = "GAME OVER",
                    subtitle_text: str = "je bent verloren loser",
                    restart_script: str = "app.py",
                    # Assets:
                    click_sound_path: str = "sounds/sound_effects/click_sound.mp3",
                    menu_img_path: str = "sprites/gui/try_again_button.png",
                    menu_hover_path: str = "sprites/gui/image.png",
                    quit_img_path: str = "sprites/gui/closegame_button.png",
                    quit_hover_path: str = "sprites/gui/closegame_button_hover.png",
                    # Layout:
                    title_y: int = 260,
                    subtitle_y: int = 330,
                    menu_btn_y: int = 420,
                    quit_btn_y: int = 520,
                ):
                    self.screen = screen
                    self.WIDTH = width
                    self.HEIGHT = height

                    self.active = False
                    self.restart_script = restart_script


                    self.title_text = title_text
                    self.subtitle_text = subtitle_text

                    # Overlay (half transparant)
                    self.overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
                    self.overlay.fill((0, 0, 0, max(0, min(255, overlay_alpha))))

                    # Fonts
                    FONT_PATH = "Nothing Smoothie.ttf"

                    self.font_big = pygame.font.Font(FONT_PATH, 110)
                    self.font_small = pygame.font.Font(FONT_PATH, 44)


                    # Sound
                    self.click_sound = None
                    try:
                        self.click_sound = pygame.mixer.Sound(click_sound_path)
                        self.click_sound.set_volume(0.8)
                    except Exception:
                        # Geen crash als sound ontbreekt
                        self.click_sound = None

                    # Images
                    self.menu_img = pygame.image.load(menu_img_path).convert_alpha()
                    self.menu_hover = pygame.image.load(menu_hover_path).convert_alpha()
                    self.quit_img = pygame.image.load(quit_img_path).convert_alpha()
                    self.quit_hover = pygame.image.load(quit_hover_path).convert_alpha()

                    #print("try again:", self.menu_img.get_size())
                    #print("quit:", self.quit_img.get_size())

                            
                    MENU_SIZE = (406, 66)  
                    QUIT_SIZE = (406, 66)   
                    # scale base images
                    self.menu_img = pygame.transform.smoothscale(self.menu_img, MENU_SIZE)
                    self.menu_hover = pygame.transform.smoothscale(self.menu_hover, MENU_SIZE)

                    self.quit_img = pygame.transform.smoothscale(self.quit_img, QUIT_SIZE)
                    self.quit_hover = pygame.transform.smoothscale(self.quit_hover, QUIT_SIZE)

                    center_x = self.WIDTH // 2
                    self.title_pos = (center_x, title_y)
                    self.subtitle_pos = (center_x, subtitle_y)

                    self.menu_btn = Button(
                        (center_x - self.menu_img.get_width() // 2, menu_btn_y),
                        self.menu_img,
                        self.menu_hover,
                        self.restart_game,
                        click_sound=self.click_sound,
                    )

                    self.quit_btn = Button(
                        (center_x - self.quit_img.get_width() // 2, quit_btn_y),
                        self.quit_img,
                        self.quit_hover,
                        self.quit_game,
                        click_sound=self.click_sound,
                    )

                    self.buttons = [self.menu_btn, self.quit_btn]

                # ---- Public controls ----
                def show(self):
                    self.active = True

                def hide(self):
                    self.active = False

                # ---- Actions ----
                def restart_game(self):
                    main()




                def quit_game(self):
                    pygame.quit()
                    run = False
                    pygame.quit()

                # ---- Loop hooks ----
                def handle_event(self, event):
                    if not self.active:
                        return
                    for b in self.buttons:
                        b.handle_event(event)

                def draw(self):
                    if not self.active:
                        return

                    # Donker over gameplay heen
                    self.screen.blit(self.overlay, (0, 0))

                    title = self.font_big.render(self.title_text, True, (255, 255, 255))
                    subtitle = self.font_small.render(self.subtitle_text, True, (220, 220, 220))

                    self.screen.blit(title, title.get_rect(center=self.title_pos))
                    self.screen.blit(subtitle, subtitle.get_rect(center=self.subtitle_pos))

                    for b in self.buttons:
                        b.draw(self.screen)


            #open in this file
            if __name__ == "__main__":
                pygame.init()
                pygame.mixer.init()

                WIDTH, HEIGHT = 1024, 834
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("EndScreen Demo")
                clock = pygame.time.Clock()

                # temp bg
                bg = pygame.Surface((WIDTH, HEIGHT))
                bg.fill((30, 60, 90))

                endscreen = EndScreen(screen, WIDTH, HEIGHT)
                endscreen.show() 
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        endscreen.handle_event(event)

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            fullscreen = not fullscreen

                            if fullscreen:
                                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                            else:
                                screen = pygame.display.set_mode((WIDTH, HEIGHT))

                            
                            endscreen.screen = screen

                    
                    screen.blit(bg, (0, 0))

                    endscreen.draw()

                    pygame.display.flip()
                    clock.tick(60)


                pygame.quit()


        
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1024, 834))

                    pygame.mouse.set_visible(False)

        
        # draw crosshair
        mouse_x, mouse_y = pygame.mouse.get_pos()

        crosshair_rect = crosshair.get_rect(center=(mouse_x, mouse_y))
        screen.blit(crosshair, crosshair_rect)


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