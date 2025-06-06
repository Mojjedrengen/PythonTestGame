import arcade
import math
from .bullet import Bullet

class Player:
    def __init__(self, speed, x, y):
        self.speed = speed
        self.x = x
        self.y = y
        self.size = 50
        self.changeX = 0
        self.changeY = 0
        self.dirX = 0
        self.dirY = 0
        self.attack_speed : float = 10 # Frequence
        self.delta_shoot_time = 0

    def draw(self):
        #arcade.draw_lrbt_rectangle_filled(self.x, self.x+self.size, self.y, self.y+self.size, arcade.csscolor.BROWN)
        arcade.draw_lbwh_rectangle_filled(self.x, self.y, self.size, self.size, arcade.csscolor.RED)

    def on_update(self, bullet_list, delta_time):
        self.__move()
        as_time = 1 / self.attack_speed
        self.delta_shoot_time += delta_time
        if self.delta_shoot_time > as_time and not (self.dirX == 0 and self.dirY == 0):
            self.__shoot(bullet_list)
            self.delta_shoot_time = 0

    def __move(self):
        length = math.sqrt(math.pow(self.changeX, 2) + math.pow(self.changeY, 2))
        if length == 0:
            return
        moveX = self.changeX / length
        moveY = self.changeY / length
        self.x = self.x + moveX * self.speed
        self.y = self.y + moveY * self.speed 


    def moveX(self, changeX : int ):
        if (changeX > 1 or changeX < -1):
            return
        self.changeX = changeX

    def moveY(self, changeY : int): 
        if (changeY > 1 or changeY < -1):
            return
        self.changeY = changeY

    def shootY(self, dirY : int): 
        if (dirY > 1 or dirY < -1):
            return
        self.dirY = dirY

    def shootX(self, dirX : int): 
        if (dirX > 1 or dirX < -1):
            return
        self.dirX = dirX

    def __shoot(self, bullet_list):
        """if self.changeX == 0 and self.changeY == 0:
            return
        bullet = Bullet(self.x, self.y, self.changeY, self.changeX)
        bullet_list.append(bullet)
        """
        if self.dirX == 0 and self.dirY == 0:
            return
        img = arcade.draw_ellipse_filled(self.x, self.y, 10, 25, arcade.csscolor.BLACK)
        length = math.sqrt(math.pow(self.dirX, 2) + math.pow(self.dirY, 2))
        moveX = self.dirX / length
        moveY = self.dirY / length
        angle = math.cos(self.dirY / length)
        bullet = arcade.Sprite(img)
        bullet.angle = angle
        bullet.change_x = moveX * 50
        bullet.change_y = moveY * 50
        bullet.center_x = self.x
        bullet.center_y = self.y
        bullet_list.append(bullet)
