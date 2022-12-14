from enemy.simple_enemy.EnemyParent import EnemyParent


class RegularEnemy(EnemyParent):
    """This is a Regular Enemy class"""
    def __init__(self, middle, x=0, y=0):
        EnemyParent.__init__(self, x, y, 6, 6, 1, 1)
        self.counter_y = middle

    def update(self, boomerang):
        """This method updates the way this enemy moves
            by its position on a screen"""
        if self.counter_y <= 80:
            self.y += self.enemy_speed

            if self.y % 10 == 0:
                self.shoot(boomerang)

        if self.counter_y > 80:
            self.y -= self.enemy_speed
            self.color = 0
        self.counter_y += self.enemy_speed

