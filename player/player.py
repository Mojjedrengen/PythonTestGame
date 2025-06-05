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

    def draw(self):
        #arcade.draw_lrbt_rectangle_filled(self.x, self.x+self.size, self.y, self.y+self.size, arcade.csscolor.BROWN)
        arcade.draw_lbwh_rectangle_filled(self.x, self.y, self.size, self.size, arcade.csscolor.RED)

    def move(self):
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

    def shoot(self, bullet_list):
        if self.changeX == 0 and self.changeY == 0:
            return
        bullet = Bullet(self.x, self.y, self.changeY, self.changeX)
        bullet_list.append(bullet)
