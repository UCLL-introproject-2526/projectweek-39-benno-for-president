import pygame
from math import sqrt
from player import Player1, Player2
from random import randint, choice

class Enemy:
    def __init__(self, cords, speed, health, dmg):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.set_dmg(dmg)
        self.image = pygame.image.load('sprites/enemies/enemy_front1.png')
        self.__alive = True
        self.rect = self.image.get_rect(topleft=self.get_cords())
        self.mask = pygame.mask.from_surface(self.image)

    def get_cords(self):
        return [self.__x, self.__y]

    def set_cords(self, list_inp):
        if not isinstance(list_inp, list):
            if not  len(list_inp) == 2:
                raise ValueError("enemy cords cannot be empty and has to be list")
            
        self.__x = list_inp[0]
        self.__y = list_inp[1]

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, value):
        if value < 0:
            raise ValueError("enemy speed cannot be negative")
        self.__speed = value

    def get_health(self):
        return self.__health
    
    def set_health(self, value):
        if value < 0:
            raise ValueError("enemy health cannot be negative")
        self.__health = value

    def get_dmg(self):
        return self.__dmg
    
    def set_dmg(self, value):
        if value < 0:
            raise ValueError("enemy dmg cannot be negative")
        self.__dmg = value

    def get_alive(self):
        return self.__alive

    def get_closest(self, player1, player2):
        if sqrt((self.__x - player1.get_cords()[0])**2 + (self.__y - player1.get_cords()[1])**2) < sqrt((self.__x - player2.get_cords()[0])**2 + (self.__y - player2.get_cords()[1])**2):
            return player1
        else:
            return player2

    def move(self, player, dt): # player vinden met get closest en dt megeven
        
        # Bepaal richting
        dx = player.get_cords()[0] - self.__x
        dy = player.get_cords()[1] - self.__y

        distance = sqrt(dx**2 + dy**2)

        if distance != 0:
            self.__x += (dx / distance) * self.__speed * dt
            self.__y += (dy / distance) * self.__speed * dt


    def hit(self, other):
        diff = max(0, self.__health - other.get_dmg())
        self.set_health(diff)
        if self.__health <= 0:
            self.__alive = False



def spawn_location(self, p1, p2, small_border, big_border):
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

    return int(x), int(y)




    # def spawn_location(self, p1, p2, small_border, big_border): #p1 & p2 moet playerX.get_cords() zijn en min border = min afstand van player dat ze spawnen & big border is max
    #     x_min = min(p1[0], p2[0])
    #     x_max = max(p1[0], p2[0])
    #     y_min = min(p1[1], p2[1])
    #     y_max = max(p1[1], p2[1])

    #     inner = pygame.Rect(
    #         x_min - small_border,
    #         y_min - small_border,
    #         (x_max - x_min) + 2 * small_border,
    #         (y_max - y_min) + 2 * small_border)

    #     outer = pygame.Rect(
    #         x_min - big_border,
    #         y_min - big_border,
    #         (x_max - x_min) + 2 * big_border,
    #         (y_max - y_min) + 2 * big_border)

    #     side = choice(["top", "bottom", "left", "right"])

    #     if side == "top":
    #         x = randint(outer.left, outer.right)
    #         y = outer.top
    #     elif side == "bottom":
    #         x = randint(outer.left, outer.right)
    #         y = outer.bottom
    #     elif side == "left":
    #         x = outer.left
    #         y = randint(outer.top, outer.bottom)
    #     else:
    #         x = outer.right
    #         y = randint(outer.top, outer.bottom)

    #     return x, y

