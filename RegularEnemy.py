import pyxel
import Bullet


RegularEnemyWidth = 6
RegularEnemyHeight = 6
RegularEnemySpeed = 1
RegularEnemies = []
color = 1

class RegularEnemy:

    def __init__(self, x, y, middl):
        self.x = x
        self.y = y
        self.w = RegularEnemyWidth
        self.h = RegularEnemyHeight
        self.color = color
        self.is_alive = True
        self.counter_y = middl

    def update(self, boomerang):

        if self.counter_y <= 80:
            if self.y > pyxel.height - 1:
                self.is_alive = False

            self.y += RegularEnemySpeed

            if self.y % 10 == 0:
                boomerang.add_object(self.shoot())

        if self.counter_y > 80:
            if self.y > pyxel.height - 1:
                self.is_alive = False

            self.y -= RegularEnemySpeed
            self.color = 0
        self.counter_y += RegularEnemySpeed


    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)


    def shoot(self):
        x_pos = self.x + (self.h + self.w) / 6
        y_pos = self.y - (self.h + self.w) / 72

        return Bullet.Bullet(x_pos, y_pos, 4, "down")
