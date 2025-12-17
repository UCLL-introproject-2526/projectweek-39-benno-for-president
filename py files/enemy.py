import pygame

class Enemy:
    def __init__(self, cords, speed, health, dmg):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.set_dmg(dmg)
        self.__alive = True
    
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
        if sqrt((self.__x - player1.get_cords[0])**2 + (self.__y - player1.get_cords[1])**2) < sqrt((self.__x - player2.get_cords[0])**2 + (self.__y - player2.get_cords[1])**2):
            return player1
        else:
            return player2

    def move(self, player):
        if self.__x < player.get_cords[0]:
            self.__x =+ self.get_speed()
        else:
            self.__x =- self.get_speed()

        if self.__y < player.get_cords[1]:
            self.__y =+ self.get_speed()
        else:
            self.__y =- self.get_speed()


    def hit(self, other):
        diff = max(0, self.__health - other.get_dmg())
        self.set_health(diff)
        if self.__health <= 0:
            self.__alive = False
            