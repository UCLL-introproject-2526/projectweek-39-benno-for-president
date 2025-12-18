# victory_screen.py
import pygame
import sys


class Button:
    def __init__(self, pos, image, hover_image, on_click, click_sound=None, click_delay_ms=120):
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


class CreditsScroller:
    """
    Star Wars-ish credits scroller (upward + slight perspective).
    - start(): resets scroll
    - update(dt)
    - draw(surface)
    """

    def __init__(
        self,
        width,
        height,
        font_path="Nothing Smoothie.ttf",
        font_size=44,
        color=(245, 230, 90),
        speed_px_per_sec=90,
        start_y=None,
        vanish_y_ratio=0.18,
        max_scale=1.0,
        min_scale=0.35,
    ):
        self.W = width
        self.H = height
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color
        self.speed = speed_px_per_sec
        self.vanish_y = int(self.H * vanish_y_ratio)
        self.max_scale = max_scale
        self.min_scale = min_scale

        self.lines = []
        self.base_surfs = []
        self.total_height = 0

        self.start_y = start_y if start_y is not None else self.H + 60
        self.offset_y = self.start_y

    def set_text(self, lines):
        self.lines = lines[:]
        self.base_surfs = [self.font.render(line, True, self.color) for line in self.lines]

        spacing = 18
        self.total_height = 0
        for s in self.base_surfs:
            self.total_height += s.get_height() + spacing
        self.total_height += 80

    def start(self):
        self.offset_y = self.start_y

    def update(self, dt):
        self.offset_y -= self.speed * dt

    def draw(self, surf):
        # Dark-ish gradient overlay behind credits (optional)
        # Keep it simple: just draw with alpha rect
        shade = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        shade.fill((0, 0, 0, 200))
        surf.blit(shade, (0, 0))

        center_x = self.W // 2
        y = self.offset_y
        spacing = 18

        for base in self.base_surfs:
            # Perspective: as y approaches vanish_y, scale down
            # Map y from [vanish_y .. H] -> scale [min_scale .. max_scale]
            # Clamp for stability
            t = (y - self.vanish_y) / max(1, (self.H - self.vanish_y))
            if t < 0:
                t = 0
            if t > 1:
                t = 1
            scale = self.min_scale + (self.max_scale - self.min_scale) * t

            # If line is far above vanish, skip draw
            if y < self.vanish_y - 200:
                y += base.get_height() + spacing
                continue

            # Scale and blit
            w = int(base.get_width() * scale)
            h = int(base.get_height() * scale)
            if w > 0 and h > 0:
                s = pygame.transform.smoothscale(base, (w, h))
                rect = s.get_rect(center=(center_x, int(y)))
                surf.blit(s, rect)

            y += base.get_height() + spacing

    def finished(self):
        # finished when last line scrolled past vanish area + extra
        return self.offset_y + self.total_height < self.vanish_y - 80


class VictoryScreen:
    def __init__(
        self,
        screen: pygame.Surface,
        width: int,
        height: int,
        overlay_alpha: int = 140,
        title_text: str = "VICTORY ROYALE",
        subtitle_text: str = "je hebt kerstmis gered",
        # Assets
        click_sound_path: str = "sounds/sound_effects/click_sound.mp3",
        # Font
        font_path: str = "Nothing Smoothie.ttf",
    ):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height

        self.active = False
        self.mode = "victory"  

        self.title_text = title_text
        self.subtitle_text = subtitle_text

        # overlay
        self.overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, max(0, min(255, overlay_alpha))))

        # fonts
        self.font_big = pygame.font.Font(font_path, 110)
        self.font_small = pygame.font.Font(font_path, 44)

        # sound click
        self.click_sound = None
        try:
            self.click_sound = pygame.mixer.Sound(click_sound_path)
            self.click_sound.set_volume(0.8)
        except Exception:
            self.click_sound = None

        # buttons
        self.btn_img = pygame.image.load('sprites/gui/credits_button.png').convert_alpha()
        self.btn_hover = pygame.image.load('sprites/gui/credits_hover.png').convert_alpha()

        self.quit_img = pygame.image.load("sprites/gui/closegame_button.png").convert_alpha()
        self.quit_hover = pygame.image.load("sprites/gui/closegame_button_hover.png").convert_alpha()
        
        BTN_SIZE = (406, 66)
        self.btn_img = pygame.transform.smoothscale(self.btn_img, BTN_SIZE)
        self.btn_hover = pygame.transform.smoothscale(self.btn_hover, BTN_SIZE)

        self.quit_img = pygame.transform.smoothscale(self.quit_img, BTN_SIZE)
        self.quit_hover = pygame.transform.smoothscale(self.quit_hover, BTN_SIZE)

        cx = self.WIDTH // 2
        self.title_pos = (cx, 230)
        self.subtitle_pos = (cx, 305)

        # Buttons
        self.credits_btn = Button(
            (cx - self.btn_img.get_width() // 2, 430),
            self.btn_img,
            self.btn_hover,
            self.open_credits,
            click_sound=self.click_sound,
            click_delay_ms=120,

        )
        self.quit_btn = Button(
            (cx - self.btn_img.get_width() // 2, 520),
            self.btn_img,
            self.btn_hover,
            self.quit_game,
            click_sound=self.click_sound,
            click_delay_ms=120,
        )
        self.quit_btn = Button(
        (cx - self.quit_img.get_width() // 2, 520),
        self.quit_img, self.quit_hover, self.quit_game,
        click_sound=self.click_sound, click_delay_ms=120
         )

        self.buttons = [self.credits_btn, self.quit_btn]

       

        # Button labels (drawn on top of the placeholder buttons)
        self.btn_font = pygame.font.Font(font_path, 40)

        self.scroller = CreditsScroller(
            self.WIDTH,
            self.HEIGHT,
            font_path=font_path,
            font_size=44,
            color=(245, 230, 90),
            speed_px_per_sec=30,
        )
        credit_text="""
BENNO VS SANTA


Benno Debals, geode IT’er, diep in het systeem,
Computer systems, kernels, bits, hij kent het probleem.
PowerPoint staat klaar, slides strak genummerd,
Maar de aula is leeg… zelfs de echo is verstomd 🫥

Hij praat over threads en over scheduling,
Maar de stoelen kijken terug, pure stilte, geen kring.
“Dit komt op het examen”, zegt hij keer op keer,
Maar niemand die luistert, niemand die ’t noteert.

Hij klikt naar slide 42,
Maar zelfs Moodle kijkt hem moe.
Hij weet alles, da’s geen vraag,
Maar waar is zijn publiek vandaag?

🎶 Bennooo Debals, geode IT’er man,
Goed in computer systems, beter dan je kan.
Niemand komt naar zijn les, niemand kent zijn slides,
Maar in zijn hoofd draait Linux — altijd, realtime. 🎶

Altijd realtime

Cache coherency, mutex locks, race condition fight,
Hij dropt die termen alsof het niets is, elke site.
Studenten zeggen: “We kijken de opname wel”,
Maar die opname blijft ongezien, net als zijn verhaal.

Hij debugt het leven zoals een C-programma,
Maar attendance blijft null, da’s het echte drama.
Zijn slides zijn correct, maar niemand die het weet,
PDF na PDF, ongeopend, te laat, te breed.

🎶 Bennooo Debals, geode IT’er man,
Goed in computer systems, beter dan je kan.
Niemand komt naar zijn les, niemand kent zijn slides,
Maar in zijn hoofd draait Linux — altijd, realtime. 🎶

Altijd realtime

Misschien geen publiek, geen volle zaal,
Maar Benno blijft compileren, keer op keer, loyaal.
Hij doet het voor de kennis, niet voor de faam,
Een echte engineer, zelfs zonder naam.

🎶 Benno Debals…
Geode IT’er, still standing strong.
Slides onbekend, les bijna leeg,
Maar zijn kennis? Die leeft nog lang. 🎶

CREDITS

Programming
- Benno Productions (RyanF, RyanDW, Sander, Ruben)

Art & Sprites
- Team Benno

Music & Sound
- Benno Music

Special Thanks
- Iedereen die getest heeft

Made with pygame

THE END
""".strip("\n")
    
        self.scroller.set_text(credit_text.splitlines())

    # public controls
    def show(self):
        self.active = True
        self.mode = "victory"

    def hide(self):
        self.active = False
        self.stop_credits_music()

    # actions
    def open_credits(self):
        self.mode = "credits"
        self.scroller.start()
        self.play_credits_music()

    def close_credits(self):
        self.mode = "victory"
        self.stop_credits_music()

    def quit_game(self):
        pygame.quit()
        sys.exit()

    
    def play_credits_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("sounds/benno_song.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def stop_credits_music(self):
        # If you want to resume gameplay music later, do that in app.py after hide().
        try:
            pygame.mixer.music.stop()
        except Exception:
            pass

    # loop hooks
    def handle_event(self, event):
        if not self.active:
            return

        if self.mode == "victory":
            for b in self.buttons:
                b.handle_event(event)

        elif self.mode == "credits":
            # ESC or click anywhere returns
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.close_credits()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.close_credits()

    def update(self, dt):
        if not self.active:
            return
        if self.mode == "credits":
            self.scroller.update(dt)
            if self.scroller.finished():
                self.close_credits()

    def draw_button_label(self, btn, text):
        label = self.btn_font.render(text, True, (15, 15, 15))
        rect = label.get_rect(center=btn.rect.center)
        self.screen.blit(label, rect)

    def draw(self):
        if not self.active:
            return

        if self.mode == "victory":
            self.screen.blit(self.overlay, (0, 0))

            title = self.font_big.render(self.title_text, True, (255, 255, 255))
            subtitle = self.font_small.render(self.subtitle_text, True, (220, 220, 220))

            self.screen.blit(title, title.get_rect(center=self.title_pos))
            self.screen.blit(subtitle, subtitle.get_rect(center=self.subtitle_pos))

            for b in self.buttons:
                b.draw(self.screen)

        elif self.mode == "credits":
            self.scroller.draw(self.screen)


# Optional demo run
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    W, H = 1024, 834
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("VictoryScreen Demo")
    clock = pygame.time.Clock()

    # fake gameplay bg
    bg = pygame.Surface((W, H))
    bg.fill((25, 60, 40))

    vs = VictoryScreen(screen, W, H)
    vs.show()

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            vs.handle_event(event)

        # draw "gameplay"
        screen.blit(bg, (0, 0))

        vs.update(dt)
        vs.draw()

        pygame.display.flip()

    pygame.quit()

