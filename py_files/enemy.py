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




    def spawn_location(self, p1, p2, small_border, big_border): #p1 & p2 moet playerX.get_cords() zijn en min border = min afstand van player dat ze spawnen & big border is max
        if p1[0] < p2[0]:
            if p1[1] > p2[1]:
                square_players = [p1, [p1[0], p2[1]], p2, [p2[0], p1[1]]] #links onder, links boven, rechts boven, rechts onder
            else:
                square_players = [[p1[0], p2[1]],p1,[p2[0], p1[1]],  p2]
        else:
            if p1[1] > p2[1]:
                square_players = [p2 [p2[0], p1[1]], p1, [p1[0], p2[1]]] #links onder, links boven, rechts boven, rechts onder
            else:
                square_players = [[p2[0], p1[1]],p2,[p1[0], p2[1]],  p1]



        square_min_grinch = square_players.copy()
        
        square_min_grinch[0][0] -= small_border
        square_min_grinch[0][1] += small_border
        square_min_grinch[1][0] -= small_border
        square_min_grinch[1][1] -= small_border
        square_min_grinch[2][0] += small_border
        square_min_grinch[2][1] -= small_border
        square_min_grinch[3][0] += small_border
        square_min_grinch[3][1] += small_border

        square_big_grinch = square_min_grinch.copy()

        square_big_grinch[0][0] -= big_border
        square_big_grinch[0][1] += big_border
        square_big_grinch[1][0] -= big_border
        square_big_grinch[1][1] -= big_border
        square_big_grinch[2][0] += big_border
        square_big_grinch[2][1] -= big_border
        square_big_grinch[3][0] += big_border
        square_big_grinch[3][1] += big_border

        mob_x1 = randint(int(square_min_grinch[0][0]), int(square_big_grinch[0][0]))
        mob_x2 = randint(int(square_min_grinch[3][0]), int(square_big_grinch[3][0]))
        
        mob_x = choice([mob_x1, mob_x2])

        mob_y1 = randint(int(square_min_grinch[0][1]), int(square_big_grinch[0][1]))
        mob_y2 = randint(int(square_min_grinch[3][1]), int(square_big_grinch[3][1]))
        
        mob_y = choice([mob_y1, mob_y2])

        return (int(mob_x), int(mob_y))