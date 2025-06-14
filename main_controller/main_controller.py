from PIL import Image
import arcade
from arcade.sprite_list import SpriteList
from arcade.texture import Texture
from pyglet.graphics import Batch
from player import Player

import random

class MainController(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)
        
        #self.height = height
        #self.width = width

        self.game_over = True
        
        self.player_list = None
        self.bullet_list = None
        self.player = None
        self.player_collider = None
        self.enemy_list = None
        self.game_over_text = None

        self.score = 0
        self.enemy_frequency = 1
        self.enemy_time_counter = 0
        
        self.ui = Batch()
        self.ui_text = arcade.Text("", self.width / 2, self.height / 2 + 15, font_size=24, bold=True, anchor_x="center", batch=self.ui)
        self.score_text = arcade.Text("Score: " + str(self.score), 0, self.height - 50, batch=self.ui)

    def setup(self):
        self.game_over = False
        self.ui_text.text = ""
        self.score_text.font_size = 12
        img = Image.open("data/PlayerYes.png")
        texture = arcade.Texture(img)
        self.player_collider = arcade.Sprite(texture)
        self.player_collider.scale = 1
        self.bullet_list = arcade.SpriteList()
        self.player = Player(200, 100, 100, self.player_collider)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_collider)
        self.enemy_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        self.ui.draw()
        if not self.game_over:
            self.bullet_list.draw()
            self.player.draw()
            self.player_list.draw()
            self.enemy_list.draw()
        else:
            return

    def on_update(self, delta_time):
        if not self.game_over:
            self.player.on_update(self.bullet_list, delta_time)
            self.bullet_list.update()
            self.enemy_list.update()
            t = 1 / self.enemy_frequency
            self.enemy_time_counter += delta_time
            if self.enemy_time_counter >= t:
                self.enemy_time_counter = 0
                texture = arcade.make_soft_square_texture(50, arcade.csscolor.BLACK, 255, 255)
                enemy = arcade.Sprite(texture)
                enemy.change_x = 0 
                enemy.change_y = -5
                enemy.center_y = self.height - 50
                enemy.center_x = random.randint(50, self.width-50)
                self.enemy_list.append(enemy)

            for bullet in self.bullet_list:
                hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                for enemy in hit_list:
                    enemy.remove_from_sprite_lists()
                    self.score += 1
                    print("score: ", self.score)

                if bullet.center_y > self.height or bullet.center_y < 0 or bullet.center_x > self.width or bullet.center_x < 0:
                    bullet.remove_from_sprite_lists()

            for player in self.player_list:
                player.draw_hit_box(arcade.csscolor.BLACK, 2)
                if player.center_y > self.height:
                    self.player.boundsY(-1)
                elif player.center_y < 0:
                    self.player.boundsY(1)
                elif player.center_x > self.width:
                    self.player.boundsX(-1)
                elif player.center_x < 0:
                    self.player.boundsX(1)

            for enemy in self.enemy_list:
                hit_list = arcade.check_for_collision_with_list(enemy, self.player_list)
                if len(hit_list) > 0:
                    enemy.remove_from_sprite_lists()
                    print(self.player.health_points - 1)
                    if self.player.is_hit():
                        print("Game Over")
                        self.on_game_over()
                
                if enemy.center_y > self.height or enemy.center_y < 0 or enemy.center_x > self.width or enemy.center_x < 0:
                    enemy.remove_from_sprite_lists()
            self.score_text.text = "Score: " + str(self.score)

    
    def on_key_press(self, key, modifiers):
        if not self.game_over:
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
        if not self.game_over:
            if key == arcade.key.A or key == arcade.key.D:
                self.player.moveX(0)
            if key == arcade.key.W or key == arcade.key.S:
                self.player.moveY(0)
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player.shootX(0)
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.player.shootY(0)

    def on_game_over(self):
        self.game_over = True

        self.player_list = None
        self.bullet_list = None
        self.player = None
        self.player_collider = None
        self.enemy_list = None
        
        self.score_text.text = "Score: " + str(self.score)
        self.score_text.anchor_x = "center"
        self.score_text.position = (self.width / 2, self.height / 2 - 15)
        print(self.score_text.font_size)
        self.score_text.font_size = 24

        self.ui_text = "Game Over"

        self.score = 0
