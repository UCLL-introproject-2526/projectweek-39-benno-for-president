

class Weapon:
    def __init__(self, dmg, rpm, bullet_speed):
        self.set_dmg(dmg)
        self.set_rpm(rpm)
        self.set_bullet_speed(bullet_speed)


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

    def get_bullet_speed(self):
        return self.__bullet_speed
    
    def set_bullet_speed(self, value):
        if value < 0:
            raise ValueError("weapon bullet speed cannot be negative")
        self.__bullet_speed = value


class Bullet:
    def __init__(self, x, y, name, Weap, target, time1):
        self.__x = x
        self.__y = y
        self.__name = name
        self.set_target(target)
        self.__speed = Weap.get_bullet_speed()
        self.time1 = time1

    def get_cords(self):
        return [self.__x, self.__y]
    
    def get_name(self):
        return self.__name
    
    def get_target(self):
        return self.__target
    
    def set_target(self, value):
        self.__target = value
    
    def get_speed(self):
        return self.__speed