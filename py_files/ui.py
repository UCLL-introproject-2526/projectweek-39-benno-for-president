
import sys
import subprocess
import pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Menu")


MENU_WIDTH, MENU_HEIGHT = 1024, 834
screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
clock = pygame.time.Clock()

# Geluiden 
click_sound = pygame.mixer.Sound("sounds/sound_effects/click_sound.mp3")
click_sound.set_volume(0.8)

pygame.mixer.music.load("sounds/music/menu_music.ogg")
pygame.mixer.music.play(-1)

# Afbeeldingen
BG = pygame.image.load('sprites/gui/background_start_screen.png').convert()
play_img = pygame.image.load("sprites/gui/play_button.png").convert_alpha()
play_hover_img = pygame.image.load("sprites/gui/play_button_hover.png").convert_alpha()
quit_img = pygame.image.load("sprites/gui/closegame_button.png").convert_alpha()
quit_hover_img = pygame.image.load("sprites/gui/closegame_button_hover.png").convert_alpha()

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
        surf.blit(self.hover_image if self.hover else self.image, self.rect)


def launch_app():
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
center_x = MENU_WIDTH // 2
play_btn = Button((center_x - play_img.get_width() // 2, 400), play_img, play_hover_img, launch_app)
quit_btn = Button((center_x - quit_img.get_width() // 2, 500), quit_img, quit_hover_img, quit_game)
buttons_main = [play_btn, quit_btn]


menu_surface = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))

is_fullscreen = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))

        
        if is_fullscreen:
            screen_width, screen_height = screen.get_size()
            scale = min(screen_width / MENU_WIDTH, screen_height / MENU_HEIGHT)
            x_offset = (screen_width - MENU_WIDTH*scale) // 2
            y_offset = (screen_height - MENU_HEIGHT*scale) // 2

            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                event.pos = ((event.pos[0]-x_offset)/scale, (event.pos[1]-y_offset)/scale)

        for b in buttons_main:
            b.handle_event(event)

    menu_surface.blit(BG, (0, 0))
    for b in buttons_main:
        b.draw(menu_surface)

    if is_fullscreen:
        screen_width, screen_height = screen.get_size()
        scale = min(screen_width / MENU_WIDTH, screen_height / MENU_HEIGHT)
        scaled_surface = pygame.transform.scale(menu_surface, (int(MENU_WIDTH*scale), int(MENU_HEIGHT*scale)))
        x_offset = (screen_width - scaled_surface.get_width()) // 2
        y_offset = (screen_height - scaled_surface.get_height()) // 2
        screen.fill((0, 0, 0))  
        screen.blit(scaled_surface, (x_offset, y_offset))
    else:
        screen.blit(menu_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)