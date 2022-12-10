from enemy.simple_enemy.EnemyParent import EnemyParent


class RegularEnemy(EnemyParent):

    def __init__(self, middle: float, x=0, y=0):
        EnemyParent.__init__(self, x, y, 6, 6, 1, 1)

    def update(self, boomerang):

        if self.counter_y <= 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

            self.y += self.enemy_speed

            if self.y % 10 == 0:
                self.shoot(boomerang)

        if self.counter_y > 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

            self.y -= self.enemy_speed
            self.color = 0
        self.counter_y += self.enemy_speed

