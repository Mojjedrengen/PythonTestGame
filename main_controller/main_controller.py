import arcade
from arcade.sprite_list import SpriteList
from player import Player

class MainController(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)
 
        self.player_list = None
        self.bullet_list = None
        self.player = None
        self.player_collider = None

    def setup(self):
        texture = arcade.make_soft_square_texture(50, arcade.csscolor.RED, 255, 90)
        self.player_collider = arcade.Sprite()
        self.player_collider.scale = 0.4
        self.bullet_list = arcade.SpriteList()
        self.player = Player(10, 100, 100, self.player_collider)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_collider)
        print("Test Branch")

    def on_draw(self):
        self.clear()
        self.bullet_list.draw()
        self.player_list.draw()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.on_update(self.bullet_list, delta_time)
        self.bullet_list.update()
    
    def on_key_press(self, key, modifiers):
        if   key == arcade.key.A:
            self.player.moveX(-1)
        elif key == arcade.key.D:
            self.player.moveX(1)
        elif key == arcade.key.W:
            self.player.moveY(1)
        elif key == arcade.key.S:
            self.player.moveY(-1)
        elif key == arcade.key.LEFT:
            self.player.shootX(-1)
        elif key == arcade.key.RIGHT:
            self.player.shootX(1)
        elif key == arcade.key.UP:
            self.player.shootY(1)
        elif key == arcade.key.DOWN:
            self.player.shootY(-1)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.player.moveX(0)
        if key == arcade.key.W or key == arcade.key.S:
            self.player.moveY(0)
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.shootX(0)
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.shootY(0)
