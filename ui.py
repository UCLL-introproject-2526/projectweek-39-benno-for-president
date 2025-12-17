import sys
import subprocess
import pygame

pygame.init()
pygame.display.set_caption("Menu")

WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FONT_BIG = pygame.font.SysFont(None, 72)
FONT_MED = pygame.font.SysFont(None, 42)
FONT_SMALL = pygame.font.SysFont(None, 28)

# Kleuren
BG = (18, 18, 22)
PANEL = (28, 28, 36)
WHITE = (235, 235, 235)
MUTED = (170, 170, 180)
ACCENT = (110, 180, 255)
BTN = (45, 45, 60)
BTN_HOVER = (70, 70, 95)
BTN_TEXT = (245, 245, 245)

def draw_text(surf, text, font, color, center):
    img = font.render(text, True, color)
    rect = img.get_rect(center=center)
    surf.blit(img, rect)

class Button:
    def __init__(self, rect, label, on_click):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.on_click = on_click
        self.hover = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.on_click()

    def draw(self, surf):
        color = BTN_HOVER if self.hover else BTN
        pygame.draw.rect(surf, color, self.rect, border_radius=14)
        pygame.draw.rect(surf, (90, 90, 120), self.rect, width=2, border_radius=14)
        draw_text(surf, self.label, FONT_MED, BTN_TEXT, self.rect.center)

def launch_app():
    # Start app.py met dezelfde Python interpreter als waarmee menu.py draait
    try:
        subprocess.Popen([sys.executable, "app.py"])
        pygame.quit()
        sys.exit(0)
    except Exception as e:
        print("Kon app.py niet starten:", e)

def quit_game():
    pygame.quit()
    sys.exit(0)

# Simpele options "state"
show_options = False
volume = 50

def toggle_options():
    global show_options
    show_options = not show_options

def vol_down():
    global volume
    volume = max(0, volume - 10)

def vol_up():
    global volume
    volume = min(100, volume + 10)

# Buttons
btn_w, btn_h = 300, 70
center_x = WIDTH // 2
start_y = 220
gap = 18

play_btn = Button((center_x - btn_w//2, start_y + 0*(btn_h+gap), btn_w, btn_h), "PLAY", launch_app)
options_btn = Button((center_x - btn_w//2, start_y + 1*(btn_h+gap), btn_w, btn_h), "OPTIONS", toggle_options)
quit_btn = Button((center_x - btn_w//2, start_y + 2*(btn_h+gap), btn_w, btn_h), "QUIT", quit_game)

opt_minus = Button((center_x - 170, start_y + 3*(btn_h+gap) + 10, 80, 55), "-", vol_down)
opt_plus  = Button((center_x + 90,  start_y + 3*(btn_h+gap) + 10, 80, 55), "+", vol_up)

buttons_main = [play_btn, options_btn, quit_btn]
buttons_opt = [opt_minus, opt_plus]

def draw_background():
    screen.fill(BG)

    # Panel
    panel_rect = pygame.Rect(0, 0, 520, 460)
    panel_rect.center = (WIDTH//2, HEIGHT//2 + 15)
    pygame.draw.rect(screen, PANEL, panel_rect, border_radius=22)
    pygame.draw.rect(screen, (60, 60, 85), panel_rect, width=2, border_radius=22)

    # Header
    draw_text(screen, "MY GAME", FONT_BIG, WHITE, (WIDTH//2, 120))
    draw_text(screen, "Select an option", FONT_SMALL, MUTED, (WIDTH//2, 160))

def draw_options():
    # Options box
    box = pygame.Rect(0, 0, 520, 120)
    box.center = (WIDTH//2, 485)
    pygame.draw.rect(screen, (35, 35, 48), box, border_radius=18)
    pygame.draw.rect(screen, (70, 70, 95), box, width=2, border_radius=18)

    draw_text(screen, "VOLUME", FONT_SMALL, MUTED, (WIDTH//2, box.top + 28))
    draw_text(screen, f"{volume}%", FONT_MED, ACCENT, (WIDTH//2, box.top + 72))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if show_options:
                show_options = False
            else:
                quit_game()

        for b in buttons_main:
            b.handle_event(event)
        if show_options:
            for b in buttons_opt:
                b.handle_event(event)

    draw_background()

    for b in buttons_main:
        b.draw(screen)

    if show_options:
        draw_options()
        for b in buttons_opt:
            b.draw(screen)

    pygame.display.flip()
    clock.tick(60)
