# endscreen.py
import pygame
import sys
import subprocess
import os

fullscreen = False



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
        pygame.quit()
        os.execl(sys.executable, sys.executable, *sys.argv)




    def quit_game(self):
        pygame.quit()
        sys.exit()

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
