import pygame

class Camera:
    def __init__(self, width, height, map_size):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0, 0, width, height)
        self.map_width = map_size[0]
        self.map_height = map_size[1]
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1
        self.safe_zone = 100



    def dist(self, a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    def update(self, player1, player2): 


        # Haal de coördinaten van beide spelers
        p1 = player1.get_cords()
        p2 = player2.get_cords()

        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])

        min_x -= self.safe_zone
        max_x += self.safe_zone
        min_y -= self.safe_zone
        max_y += self.safe_zone

        required_w = max_x - min_x
        required_h = max_y - min_y
        zoom_x = self.width / required_w
        zoom_y = self.height / required_h
        self.zoom = max(0.7, min(1.3, min(zoom_x, zoom_y)))

        view_w = self.width / self.zoom
        view_h = self.height / self.zoom

        # Center tussen spelers of tegen mapranden
        center_x = (p1[0] + p2[0]) / 2
        center_y = (p1[1] + p2[1]) / 2

        self.offset.x = center_x - view_w / 2
        self.offset.y = center_y - view_h / 2

        # Clamp tegen mapranden
        self.offset.x = max(0, min(self.offset.x, self.map_width - view_w))
        self.offset.y = max(0, min(self.offset.y, self.map_height - view_h))


        # dx = max(0, p2[0] - (self.offset.x + view_w - safe_x), safe_x - (p1[0] - self.offset.x))
        # dy = max(0, p2[1] - (self.offset.y + view_h - safe_y), safe_y - (p1[1] - self.offset.y))
        # if dx > 0 or dy > 0:
        #     self.zoom = min(self.zoom, min(view_w / (view_w + dx), view_h / (view_h + dy)))


    def apply(self, x, y):          #mapcordinaten naar pccordinaten
        #return (int((x - self.offset.x) * self.zoom), int((y- self.offset.y) * self.zoom))
    
        return (int((x - self.offset.x) * 10), int((y- self.offset.y) * 10))
    
    def screen_to_world(self, sx, sy):
        return (
            sx / self.zoom + self.offset.x,
            sy / self.zoom + self.offset.y
            )
    #screen_pos = cam.world_to_screen(*placed_object.pos)
    #screen.blit(sprite, screen_pos)
