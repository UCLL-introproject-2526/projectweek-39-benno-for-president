import pygame
import pygame_gui


pygame.init()

screen_size = (1024,823)
pygame.display.set_caption('Main Menu')
window_surface = pygame.display.set_mode(screen_size)

background_picture = pygame.image.load('sprites/gui/background_start_screen.png')


manager = pygame_gui.UIManager(screen_size)

button_image = pygame.image.load('sprites/gui/play_button.png').convert_alpha




hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)

hello_button.set_image(button_image)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background_picture, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()