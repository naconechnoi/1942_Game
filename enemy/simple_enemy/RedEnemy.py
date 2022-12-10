import math
from enemy.simple_enemy.EnemyParent import EnemyParent


class RedEnemy(EnemyParent):

    def __init__(self, x=0, y=0):
        EnemyParent.__init__(self, x, y, 5, 5, 6, 1.5)
        self.t = 0.1

    def update(self, boomerang):
        if self.counter_y <= 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

        if 20 < self.counter_y < 130:
            res_x = 2 * math.sin(self.t)
            res_y = 2 * math.cos(self.t)
            self.t += 0.1
            self.x += res_x
            self.y += res_y
        else:
            self.y += self.enemy_speed
            self.counter_y += self.enemy_speed