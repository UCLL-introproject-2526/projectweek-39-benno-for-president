import pygame
from math import sqrt
import random

pygame.init()


Player_lives = 3

class Weapon:
    def __init__(self, dmg, rpm, spread):
        self.set_dmg(dmg)
        self.__rpm = rpm
        self.__spread = spread

    def get_dmg(self):
        return self.__dmg
    
    def set_dmg(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("weapon dmg cannot be negative")
            self.__dmg = value
        else:
            raise ValueError("weapon dmg must be int")
            
    def get_rpm(self):
        return self.__rpm
    
    def set_rpm(self, value):
        if value < 0:
            raise ValueError("weapon rpm cannot be negative")
        self.__rpm = value


    def get_spread(self):
        return self.__spread
    
    def set_spread(self, value):
        if value < 0:
            raise ValueError("weapon spread cannot be negative")
        self.__spread = value


class Player1:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True

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
        
    def move(self, key):
        if key == "q":
            self.set_cords([self.get_cords()[0] - self.__speed,self.get_cords()[1]])
        if key == "d":
            self.set_cords([self.get_cords()[0] + self.__speed,self.get_cords()[1]])
        if key == "z":
            self.set_cords([self.get_cords()[0], self.get_cords()[1] - self.__speed])
        if key == "s":            
            self.set_cords([self.get_cords()[0], self.get_cords()[1] + self.__speed])
        



class Player2:
    def __init__(self, cords, speed, health):
        self.set_cords(cords)
        self.set_speed(speed)
        self.set_health(health)
        self.__alive = True

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



player1 = Player1([400,200], 5, 50)


def main():
    

    screen_size = (1024,834)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    background = pygame.image.load('sprites/icy_background.png').convert()

    pygame.mixer.music.load('sounds/lobby_music.ogg')
    pygame.mixer.music.play(-1, fade_ms=3000)

    benno_img = pygame.image.load('sprites/bigbenno_sprite.png').convert_alpha()
    benno_img = pygame.transform.smoothscale(benno_img, (100, 100))
    player1_sprite = pygame.image.load('sprites/player1/kerstmanachterkant1.png')

    
    run = True

    while run:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        screen.blit(player1_sprite, player1.get_cords())
        

        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            player1.move("d")
        if key[pygame.K_q]:
            player1.move("q")
        if key[pygame.K_s]:
            player1.move("s")
        if key[pygame.K_z]:
            player1.move("z")


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        clock.tick(60)
        pygame.display.flip()
    
    pygame.quit()


main()



    # def render_frame(surface, xpos, ypos):
    #     benno_rect = benno_img.get_rect(center = [xpos, ypos])
    #     surface.blit(benno_img, benno_rect)

    # xpos = 400
    # ypos = 200


    #  render_frame(screen, xpos, ypos)