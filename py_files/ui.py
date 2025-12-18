import sys
import subprocess
import pygame


pygame.init()
pygame.display.set_caption("Menu")
pygame.mixer.init()

WIDTH, HEIGHT = 1024, 834
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



#sound

click_sound = pygame.mixer.Sound(
    "sounds/sound_effects/click_sound.mp3"
)
click_sound.set_volume(0.8)

pygame.mixer.music.load("sounds/music/menu_music.ogg")
pygame.mixer.music.play()


BG = pygame.image.load('sprites/gui/background_start_screen.png').convert()


play_img = pygame.image.load(
    "sprites/gui/play_button.png"
).convert_alpha()

play_hover_img = pygame.image.load(
    "sprites/gui/play_button_hover.png"
).convert_alpha()

quit_img = pygame.image.load(
    "sprites/gui/closegame_button.png"
).convert_alpha()

quit_hover_img = pygame.image.load(
    "sprites/gui/closegame_button_hover.png"
).convert_alpha()

play_hover_img = pygame.transform.scale(play_hover_img, play_img.get_size())


quit_hover_img = pygame.transform.scale(quit_hover_img, quit_img.get_size())




class Button:
    def __init__(self, pos, image, hover_image, on_click):
        self.image = image
        self.hover_image = hover_image
        self.on_click = on_click
        self.rect = self.image.get_rect(topleft=pos)
        self.hover = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                click_sound.play()
                pygame.time.delay(450)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.on_click()
                



    def draw(self, surf):
        if self.hover:
            surf.blit(self.hover_image, self.rect)
        else:
            surf.blit(self.image, self.rect)

def toggle_fullscreen():
    global is_fullscreen, screen, WIDTH, HEIGHT, center_x

    is_fullscreen = not is_fullscreen
    if is_fullscreen:
        screen = pygame.display.set_mode((1024, 834), pygame.FULLSCREEN)  
        WIDTH, HEIGHT = screen.get_size()
    else:
        screen = pygame.display.set_mode((1024, 834))
        WIDTH, HEIGHT = 1024, 834

    center_x = WIDTH // 2

    # Buttons opnieuw positioneren
    play_btn.rect.topleft = (center_x - play_img.get_width() // 2, 400)
    quit_btn.rect.topleft = (center_x - quit_img.get_width() // 2, 500)        

def launch_app():
    # Start app.py met dezelfde Python interpreter als waarmee menu.py draait
    try:
        subprocess.Popen([sys.executable, "py_files/app.py"])
        pygame.quit()
        sys.exit(0)
    except Exception as e:
        print("Kon app.py niet starten:", e)

def quit_game():
    pygame.quit()
    sys.exit(0)




# Buttons

center_x = WIDTH // 2
start_y = 220
gap = 18

play_btn = Button(
    pos=(center_x - play_img.get_width() // 2, 400),
    image=play_img,
    hover_image=play_hover_img,
    on_click=launch_app
)

quit_btn = Button(
    pos=(center_x - quit_img.get_width() // 2, 500),
    image=quit_img,
    hover_image=quit_hover_img,
    on_click=quit_game
)



buttons_main = [play_btn, quit_btn]





is_fullscreen = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                toggle_fullscreen()

        for b in buttons_main:
            b.handle_event(event)

            
        
    bg_scaled = pygame.transform.scale(BG, (WIDTH, HEIGHT))
    screen.blit(bg_scaled, (0, 0))

    for b in buttons_main:
        b.draw(screen)

    

    pygame.display.flip()
    clock.tick(60)
    current_time = pygame.time.get_ticks()