import random
import pygame
from math import sqrt
from math import 

class enemy:
    def __init__(self, cordinaten):
        self.x = cordinaten[0]
        self.y = cordinaten[1]
        self.speed = #moet nog een waarde krijgen
        self.alive = True


## dit moet naar main:

zombies = []

for i in range(0,5):
    x_pos = random.randint(0, schermbreedte)
    y_pos = random.randint(0, schermhoogte//2) # zodat zombies bv op bovenste helft van scherm komen en niet op player 1 of 2 spawnen


#calculates which player is closer to an enemy and lets the enemy move closer to player
def closest():
    if sqrt((self.__x - player1.get_cords[0])**2 + (self.__y - player1.get_cords[1])**2) < sqrt((self.__x - player2.get_cords[0])**2 + (self.__y - player2.get_cords[1])**2):
        return player1
    else:
        return player2


def move():
    if closest() = player1:
        if self.__x < player1.get_cords[0]:
            self.__x =+ self.get_speed()
        else:
            self.__x =- self.get_speed()

        if self.__y < player1.get_cords[1]:
          self.__y =+ self.get_speed()
        else:
            self.__y =- self.get_speed()

    else:
        if self.__x < player2.get_cords[0]:
            self.__x =+ self.get_speed()
        else:
            self.__x =- self.get_speed()

        if self.__y < player2.get_cords[0]:
            self.__y =+ self.get_speed()
        else:
            self.__y =- self.get_speed()


--------------------------------------------------------------------------
def spawn_around_players(): #spawnable box for the enemy's
    players_box_cords = [] # [x_min, x_max, y_min, y_max]
    if player1.get_cords[0] < player2.get_cords[0]:
        players_box_cords[0] = player1.get_cords[0] - 250
        players_box_cords[1] = player2.get_cords[0] + 250
    else:
        players_box_cords[0] = player2.get_cords[0] - 250
        players_box_cords[1] = player1.get_cords[0] + 250

    if player1.get_cords[1] < player2.get_cords[1]:
        players_box_cords[2] = player1.get_cords[1] - 250
        players_box_cords[3] = player2.get_cords[1] + 250
    else:
        players_box_cords[2] = player2.get_cords[1] - 250
        players_box_cords[3] = player1.get_cords[1] + 250

    enemy_box_cords = players_box_cords.copy()
    enemy_box_cords[0] -= 500
    enemy_box_cords[1] += 500
    enemy_box_cords[2] -= 500
    enemy_box_cords[3] += 500

    for cordinaat in range(0,4):
        if enemy_box_cords[cordinaat] < 0:
            enemy_box_cords[cordinaat] = 0

------------------------------------------------------------------------------------------

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0,0, width, height)
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1

    def dist(self, a, b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    def update(self, player1, player2, mouse_world): #mouse_pos nog niet gemaakt
        mouse_pos = pygame.mouse.get_pos()
        cam_x = (player1.get_cords[0] + player2.get_cords[0] + mouse_pos[0] ) / 3
        cam_y = (player1.get_cords[1] + player2.get_cords[1] + mouse_pos[1] ) / 3

        self.offset.x = cam_x - self.width / 2
        self.offset.y = cam_y - self.height / 2

        max_dist = max(self.dist((cam_x, cam_y),player1.get_cords), self.dist(cam_x, cam_y),player1.get_cords, self.dist(cam_x, cam_y),player1.get_cords)

        target_zoom = 800 / (max_dist + 1)

        self.zoom = max(0.5, min(1.3, target_zoom))
    

#main:
camera = Camera(with, height)
mouse_screen = pygame.mouse.get_pos()

mouse_world = (mouse_screen[0]/ camera.zoom + camera.offset.x, mouse_screen[1]/ camera.zoom + camera.offset.y)
camera.update(player1, player2, mouse_world)

