import math
from enemy.simple_enemy.EnemyParent import EnemyParent


class RedEnemy(EnemyParent):
    """This is a Red Enemy class"""
    def __init__(self, middle, said='left',  x=0, y=0):
        EnemyParent.__init__(self, x, y, 5, 5, 6, 1.5)
        self.t = 0.1
        self.counter_y = middle
        self.said = said

    def update(self, boomerang):
        """This method updates the way this enemy moves
        by its position on a screen"""
        if self.counter_y <= 30:

            self.y += self.enemy_speed

        if 30 < self.counter_y < 310:
            # to make a circle
            res_x = 2.5 * math.sin(self.t)
            res_y = 2.5 * math.cos(self.t)
            self.t += 0.1
            if self.said == 'left':
                self.x += res_x
                self.y += res_y
            if self.said == 'right':
                self.x -= res_x
                self.y += res_y

        if self.counter_y >= 310:
            self.y -= self.enemy_speed
            self.x -= self.enemy_speed

        self.counter_y += self.enemy_speed

