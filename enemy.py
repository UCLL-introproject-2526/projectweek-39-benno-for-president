import random
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

