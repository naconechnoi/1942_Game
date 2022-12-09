import pyxel
from gun.Gun import EnemyGun


RegularEnemyWidth = 6
RegularEnemyHeight = 6
RegularEnemySpeed = 1
RegularEnemies = []
color = 1

class RegularEnemy:

    def __init__(self, x, y, middle):
        self.x = x
        self.y = y
        self.w = RegularEnemyWidth
        self.h = RegularEnemyHeight
        self.color = color
        self.is_alive = True
        self.counter_y = middle
        self.gun = EnemyGun(4)

    def update(self, boomerang):

        if self.counter_y <= 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

            self.y += RegularEnemySpeed

            if self.y % 10 == 0:
                self.shoot(boomerang)

        if self.counter_y > 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

            self.y -= RegularEnemySpeed
            self.color = 0
        self.counter_y += RegularEnemySpeed

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)

    def shoot(self, boomerang):
        x_pos = self.x + (self.h + self.w) / 6
        y_pos = self.y - (self.h + self.w) / 72

        bullets = self.gun.shoot()
        if bullets != None:
            bullets[0].x = x_pos
            bullets[0].y = y_pos

            boomerang.add_object(bullets[0])

        #return Bullet.Bullet(x_pos, y_pos, 4, "down")
