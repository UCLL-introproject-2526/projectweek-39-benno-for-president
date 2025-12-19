from math import sqrt
import pygame


class Player1:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True
    
    def alive(self):
        return self.__alive

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
        if self.__health <= 0:
            self.__alive = False

    def hit(self, damage):
        health = self.get_health() - int(damage)
        self.set_health = health
        return health
    
    def get_cords(self):
        return [self.__x, self.__y]
    
    def set_cords(self, list_inp):
        if isinstance(list_inp, list):
            if len(list_inp) != 2:
                raise ValueError("player 1 cords cannot be empty")
            self.__x = list_inp[0]
            self.__y = list_inp[1]
        else:
            raise ValueError("player 1 cords have to be list")
    
        

class Player2:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True

    def alive(self):
        return self.__alive

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
        if self.__health <= 0:
            self.__alive = False
    
    def hit(self, damage):
        health = self.get_health() - int(damage)
        self.set_health = health
        return health

    def get_cords(self):
        return [self.__x, self.__y]
    
    def set_cords(self, list_inp):
        if isinstance(list_inp, list):
            if len(list_inp) != 2:
                raise ValueError("player 2 cords cannot be empty")
            self.__x = list_inp[0]
            self.__y = list_inp[1]
        else:
            raise ValueError("player 2 cords have to be list")