import arcade
from arcade.sprite_list import SpriteList
from player import Player

class MainController(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.player = Player(10, 100, 100)
        
        self.bullet_list = None

    def setup(self):
        self.bullet_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.bullet_list.draw()

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
