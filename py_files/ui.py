import sys
import subprocess
import pygame

pygame.init()
pygame.display.set_caption("Menu")

WIDTH, HEIGHT = 1024, 834
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FONT_BIG = pygame.font.SysFont(None, 72)
FONT_MED = pygame.font.SysFont(None, 42)
FONT_SMALL = pygame.font.SysFont(None, 28)

# Kleuren
BG = pygame.image.load('sprites/gui/background_start_screen.png').convert()
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
        subprocess.Popen([sys.executable, "py_files/app.py"])
        pygame.quit()
        sys.exit(0)
    except Exception as e:
        print("Kon app.py niet starten:", e)

def quit_game():
    pygame.quit()
    sys.exit(0)




# Buttons
btn_w, btn_h = 300, 70
center_x = WIDTH // 2
start_y = 220
gap = 18

play_btn = Button((center_x - btn_w//2, start_y + 0*(btn_h+gap), btn_w, btn_h), "PLAY", launch_app)

quit_btn = Button((center_x - btn_w//2, start_y + 2*(btn_h+gap), btn_w, btn_h), "QUIT", quit_game)



buttons_main = [play_btn, quit_btn]






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        


        for b in buttons_main:
            b.handle_event(event)

            
        

    screen.blit(BG, (0, 0))

    for b in buttons_main:
        b.draw(screen)

    

    pygame.display.flip()
    clock.tick(60)