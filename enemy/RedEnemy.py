import pyxel
import math
from gun.Gun import EnemyGun

RedEnemyWidth = 5
RedEnemyHeight = 5
RedEnemySpeed = 1.5
RedEnemies = []
RedEnemyColor = 6

class RedEnemy:
    # Группа следует за строем, совершает 2-3 круга, бонус за уничтожение всех
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = RedEnemyHeight
        self.w = RedEnemyWidth
        self.color = RedEnemyColor
        self.is_alive = True
        self.counter_y = 0
        self.t = 0.1
        self.gun = EnemyGun

    def update(self, boomerang):

        if self.counter_y <= 80:
            """if self.y > pyxel.height - 1:
                self.is_alive = False"""

        if self.counter_y > 20 and self.counter_y < 130:
            res_x = 2*math.sin(self.t)
            res_y = 2*math.cos(self.t)
            self.t += 0.1
            self.x += res_x
            self.y += res_y
        else:
            self.y += RedEnemySpeed
            self.counter_y += RedEnemySpeed

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

