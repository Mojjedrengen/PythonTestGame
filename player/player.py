import arcade
import math

class Player:
    def __init__(self, speed, x: float, y : float, collider : arcade.Sprite):
        self.size = 3.5
        self.speed = speed
        self.center_x = x
        self.center_y = y
        self.changeX = 0
        self.changeY = 0
        self.dirX = 0
        self.dirY = 0
        self.attack_speed : float = 10 # Frequence
        self.delta_shoot_time = 0
        self.collider = collider
        self.collider.scale = self.size
        self.health_points = 3

    def draw(self):
        x = self.center_x - self.size / 2
        y = self.center_y - self.size / 2
        arcade.draw_lrbt_rectangle_filled(x, x+self.size, y, y+self.size, arcade.csscolor.BROWN)
        self.collider.draw_hit_box(arcade.csscolor.RED, 2)
        #arcade.draw_lbwh_rectangle_filled(self.center_x, self.center_y, self.size, self.size, arcade.csscolor.RED)

    def on_update(self, bullet_list, delta_time):
        self.lastDeltaTime = delta_time
        self.__move(delta_time)
        as_time = 1 / self.attack_speed
        self.delta_shoot_time += delta_time
        if self.delta_shoot_time > as_time and not (self.dirX == 0 and self.dirY == 0):
            self.__shoot(bullet_list)
            self.delta_shoot_time = 0

    def __move(self, delta_time):
        length = math.sqrt(math.pow(self.changeX, 2) + math.pow(self.changeY, 2))
        if length == 0:
            return
        moveX = self.changeX / length
        moveY = self.changeY / length
        self.center_x = self.center_x + moveX * self.speed * delta_time
        self.center_y = self.center_y + moveY * self.speed * delta_time
        self.collider.center_x = self.center_x
        self.collider.center_y = self.center_y


    def moveX(self, changeX : int ):
        if (changeX > 1 or changeX < -1):
            return
        self.changeX = changeX

    def moveY(self, changeY : int): 
        if (changeY > 1 or changeY < -1):
            return
        self.changeY = changeY

    def boundsX(self, changeX : int):
        if (changeX > 1 or changeX < -1):
            return
        tempCX = self.changeX
        self.changeX = changeX
        self.__move(self.lastDeltaTime)
        self.changeX = tempCX
    
    def boundsY(self, changeY : int):
        if (changeY > 1 or changeY < -1):
            return
        tempCY = self.changeY
        self.changeY = changeY
        self.__move(self.lastDeltaTime)
        self.changeY = tempCY

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
        texture = arcade.make_soft_square_texture(15, arcade.csscolor.BLACK, 255, 90)
        length = math.sqrt(math.pow(self.dirX, 2) + math.pow(self.dirY, 2))
        moveX = self.dirX / length
        moveY = self.dirY / length
        angle = math.acos(self.dirY / length) * 180 / math.pi
        bullet = arcade.Sprite(texture)
        bullet.angle = angle
        bullet.change_x = moveX * 10
        bullet.change_y = moveY * 10
        bullet.center_x = self.center_x
        bullet.center_y = self.center_y
        bullet_list.append(bullet)

    def is_hit(self) -> bool:
        self.health_points -= 1
        if self.health_points <= 0:
            return True
        else:
            return False
