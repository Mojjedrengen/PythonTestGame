import arcade
import math


class Bullet:
    def __init__(self, x, y, changeX, changeY):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.speed = 75
        self.length = math.sqrt(math.pow(self.changeX, 2) + math.pow(self.changeY, 2))
        self.angle = math.cos(changeY / self.length)
        self.width = 10
        self.height = 25

    def update(self):
        if self.length == 0:
            return
        moveX = self.changeX / self.length
        moveY = self.changeY / self.length
        self.x = self.x + moveX * self.speed
        self.y = self.y + moveY * self.speed

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height, arcade.csscolor.BLACK, self.angle)
