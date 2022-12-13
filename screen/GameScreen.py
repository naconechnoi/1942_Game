import random
import time

import pyxel

from Player import Player
from ScreenBoomerang import ScreenBoomerang
from enemy.bombardier.Bombardier import Bombardier
from enemy.bombardier.SuperBombardier import SuperBombardier
from enemy.simple_enemy.RedEnemy import RedEnemy
from enemy.simple_enemy.RegularEnemy import RegularEnemy


from screen.Screen import Screen


class GameScreen(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.height = 120
        self.width = 160
        self.objects = []
        self.curr_posY = 120
        self.player = None
        self.enemies = []
        self.player_bullets = []
        self.enemy_bullets = []
        self.curr_posY = 120
        self.score = 0
        self.health = 3
        self.is_player_dead = False
        self.__set_up()

    def __set_up(self):
        obj = Player(60, 120, 5, 5)
        self.player = obj

        RegularCount, RedCount = 0, 0
        y = 0

        for i in range(1, 21):

            if i % 2 == 0:
                while RegularCount <= 3:
                    x = random.randrange(10, 120, 5)
                    y -= 20
                    self.add_object(RegularEnemy(y, x, y))
                    RegularCount += 1
                RegularCount = 0
                start = time.time()

            if i % 9 == 0:
                while RedCount < 5:
                    x = random.randrange(20, 50, 10)
                    y -= 20
                    self.add_object(RedEnemy(y, 20, y))
                    RedCount += 1
                RedCount = 0

        self.add_object(Bombardier(obj, 30, -5))
        self.add_object(SuperBombardier(90, 170))

    def update(self, boomerang):

        if self.is_game_over():
            self.is_player_dead = False
            #self.next_screen.set_score(self.score)
            tmp_screen = self.next_screen.get_instance(self.next_screen.next_screen)
            tmp_screen.set_score(self.score)
            boomerang.screen = tmp_screen
            #self.game_update()
        else:
            if self.player is not None:
                boomerang = ScreenBoomerang()
                self.player.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

                # the logic of adding player and enemy bullets on the screen

                if not boomerang.is_player_bullets_add_empty():
                    for element in boomerang.get_player_bullets_add():
                        self.add_player_bullet(element)

                if not boomerang.is_player_bullet_delete_empty():
                    for element in boomerang.get_player_bullets_delete():
                        self.remove_player_bullet(element)

                if not boomerang.is_player_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_player_bullet(element)

                if not boomerang.is_player_bullet_delete_empty():
                    for element in boomerang.get_player_bullets_delete():
                        self.remove_player_bullet(element)

                if not boomerang.is_enemy_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_enemy_bullet(element)

                if not boomerang.is_enemy_bullet_delete_empty():
                    for element in boomerang.get_enemy_bullets_delete():
                        self.remove_enemy_bullet(element)

            # the logic of hitting enemy

            for bullet in self.player_bullets:
                for enemy in self.objects:
                    if (
                            enemy.x + enemy.width > bullet.x
                            and bullet.x + bullet.width > enemy.x
                            and enemy.y + enemy.height > bullet.y
                            and bullet.y + bullet.height > enemy.y
                    ):
                        self.remove_object(enemy)
                        self.score += 10

            # the logic of hitting player

            for enemy_bullet in self.enemy_bullets:
                player = self.player
                if (
                        player.x + player.radius > enemy_bullet.x
                        and enemy_bullet.x + enemy_bullet.width > player.x - player.radius
                        and player.y + player.radius > enemy_bullet.y
                        and enemy_bullet.y + enemy_bullet.width > player.y - player.radius
                ):
                    self.remove_enemy_bullet(enemy_bullet)
                    self.health -= 1
                if self.health <= 0:
                    self.is_player_dead = True
                    print("game over, score: " + str(self.score))

            for obj in self.objects:
                boomerang = ScreenBoomerang()
                obj.update(boomerang)

                if not boomerang.is_enemy_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_enemy_bullet(element)

                if not boomerang.is_enemy_bullet_delete_empty():
                    for element in boomerang.get_enemy_bullets_delete():
                        self.remove_enemy_bullet(element)

            for bullet in self.player_bullets:
                boomerang = ScreenBoomerang()
                bullet.update(boomerang)

                if not boomerang.is_player_bullets_add_empty():
                    for element in boomerang.get_player_bullets_add():
                        self.add_player_bullet(element)

                if not boomerang.is_player_bullet_delete_empty():
                    for element in boomerang.get_player_bullets_delete():
                        self.remove_player_bullet(element)

            for bullet in self.enemy_bullets:
                boomerang = ScreenBoomerang()
                bullet.update(boomerang)

                if not boomerang.is_enemy_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_enemy_bullet(element)

                if not boomerang.is_enemy_bullet_delete_empty():
                    for element in boomerang.get_enemy_bullets_delete():
                        self.remove_enemy_bullet(element)

            for enemy in self.enemies:
                boomerang = ScreenBoomerang()
                enemy.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

    def draw(self):
        pyxel.cls(12)
        for obj in self.objects:
            obj.draw()
        for obj in self.enemies:
            obj.draw()
        for obj in self.player_bullets:
            obj.draw()
        for obj in self.enemy_bullets:
            obj.draw()
        self.player.draw()
        pyxel.text(39, 4, f"SCORE {self.score:5}", 7)
        pyxel.text(1, 153, f"HEALTH {self.health:5}", 7)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_object(self, obj):
        self.objects.append(obj)

    # the logic of adding

    def add_enemy(self, obj):
        self.enemies.append(obj)

    def remove_enemy(self, obj):
        self.enemies.remove(obj)

    def add_player_bullet(self, obj):
        self.player_bullets.append(obj)

    def remove_player_bullet(self, obj):
        self.player_bullets.remove(obj)

    def add_enemy_bullet(self, obj):
        self.enemy_bullets.append(obj)

    def remove_enemy_bullet(self, obj):
        self.enemy_bullets.remove(obj)

    def run(self):
        pyxel.run(self.update, self.draw)

    # the logic of ending game
    def is_game_over(self):
        return pyxel.btnp(pyxel.KEY_EQUALS) or self.is_player_dead

    # you can add the logic of refreshing a game screen to this method
    def game_update(self):
        self.score = 0
        self.health = 3
        self.delete_enemies()
        #self.create_enemies()

    def delete_enemies(self):
        self.objects = []
        self.enemy_bullets = []
        self.player_bullets = []

    def get_instance(self, next_screen):
        game_screen = GameScreen()
        game_screen.next_screen = next_screen
        return game_screen