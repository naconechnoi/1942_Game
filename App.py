import pyxel
from Boomerang import Boomerang


class App:

    def __init__(self):
        self.height = 120
        self.width = 160
        pyxel.init(self.height, self.width)
        self.objects = []
        self.enemies = []
        self.players = []
        self.player_bullets = []
        self.enemy_bullets = []
        self.curr_posY = 120
        self.score = 0
        self.health = 3

    def draw_title(self):
        pyxel.cls(12)
        pyxel.text(50, 70, "1942", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS ENTER -", pyxel.frame_count % 3)

    def draw(self):
        self.draw_title()
        pyxel.cls(12)
        for obj in self.objects:
            obj.draw()
        for obj in self.enemies:
            obj.draw()
        for obj in self.players:
            obj.draw()
        for obj in self.player_bullets:
            obj.draw()
        for obj in self.enemy_bullets:
            obj.draw()
        pyxel.text(39, 4, f"SCORE {self.score:5}", 7)
        pyxel.text(1, 153, f"HEALTH {self.health:5}", 7)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            for player_bullet in self.players:
                boomerang = Boomerang()
                player_bullet.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

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

            for player_bullet in self.player_bullets:
                for enemy in self.objects:
                    if (
                        enemy.x + enemy.width > player_bullet.x
                        and player_bullet.x + player_bullet.width > enemy.x
                        and enemy.y + enemy.height > player_bullet.y
                        and player_bullet.y + player_bullet.height > enemy.y
                    ):
                        self.remove_object(enemy)
                        self.score += 10

            for enemy_bullet in self.enemy_bullets:
                for enemy in self.players:
                    if (
                        enemy.x + enemy.width > enemy_bullet.x
                        and enemy_bullet.x + enemy_bullet.width > enemy.x
                        and enemy.y + enemy.height > enemy_bullet.y
                        and enemy_bullet.y + enemy.height > enemy.y
                    ):
                        self.remove_enemy_bullet(enemy_bullet)
                        self.health -= 1
                    if self.health == 0:
                        pyxel.quit()
                        print('game over')

            for player_bullet in self.objects:
                boomerang = Boomerang()
                player_bullet.update(boomerang)

                if not boomerang.is_enemy_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_enemy_bullet(element)

                if not boomerang.is_enemy_bullet_delete_empty():
                    for element in boomerang.get_enemy_bullets_delete():
                        self.remove_enemy_bullet(element)

            for player_bullet in self.player_bullets:
                boomerang = Boomerang()
                player_bullet.update(boomerang)

                if not boomerang.is_player_bullets_add_empty():
                    for element in boomerang.get_player_bullets_add():
                        self.add_player_bullet(element)

                if not boomerang.is_player_bullet_delete_empty():
                    for element in boomerang.get_player_bullets_delete():
                        self.remove_player_bullet(element)

            for player_bullet in self.enemy_bullets:
                boomerang = Boomerang()
                player_bullet.update(boomerang)

                if not boomerang.is_enemy_bullets_add_empty():
                    for element in boomerang.get_enemy_bullets_add():
                        self.add_enemy_bullet(element)

                if not boomerang.is_enemy_bullet_delete_empty():
                    for element in boomerang.get_enemy_bullets_delete():
                        self.remove_enemy_bullet(element)

            for player_bullet in self.enemies:
                boomerang = Boomerang()
                player_bullet.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_object(self, obj):
        self.objects.append(obj)

    def add_enemy(self, obj):
        self.enemies.append(obj)

    def remove_enemy(self, obj):
        self.enemy.remove(obj)

    def add_player(self, obj):
        self.players.append(obj)

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
