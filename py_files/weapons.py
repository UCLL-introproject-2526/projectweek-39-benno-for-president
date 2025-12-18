import pygame

class Weapon:
    def __init__(self, dmg, rpm, bullet_speed):
        self.set_dmg(dmg)
        self.set_rpm(rpm)
        self.set_bullet_speed(bullet_speed)
        self.timer = 0

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

    def can_shoot(self):
        return self.timer >= 60 / self.get_rpm
    
    def reset_timer(self):
        self.timer = 0

    def update(self, dt):
        self.timer += dt


class Bullet:
    def __init__(self, start_pos, target_pos, weap, spawn_time):
        self.pos = pygame.Vector2(start_pos)
        self.__name = f"bullet_{spawn_time}"
        
        direction = pygame.Vector2(target_pos) - self.pos   #berekent vector
        if direction.length() > 0:                          # berekent norm van vecctor
            direction = direction.normalize() 
        
        self.__speed = weap.get_bullet_speed()          # past snelheid aan per wapen
        self.vel = direction * self.__speed
        self.spawn_time = spawn_time
        self.existing = True

        self.image = pygame.image.load("sprites.kogel2.png").conver_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def get_cords(self):
        return [self.pos.x, self.pos.y]
    
    def get_name(self):
        return self.__name
    
    def get_speed(self):
        return self.__speed
    
    def update(self, dt):
        self.pos += self.vel * dt
        self.rect.center = self.pos
        
        x, y = self.pos.x, self.pos.y       #kogel verdwijnen na map
        if x < 0 or x > 2400 or y < 0 or y > 2400: 
            self.existing = False

