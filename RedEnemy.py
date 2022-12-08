import pyxel
import math

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

    def move(self):

            if self.counter_y <= 80:
                if self.y > pyxel.height - 1:
                    self.is_alive = False
            if self.counter_y > 20 and self.counter_y < 130:
                res_x = 2*math.sin(self.t)
                res_y = 2*math.cos(self.t)
                self.t+=0.1
                self.x += res_x
                self.y += res_y
            else:
                self.y += RedEnemySpeed
            self.counter_y += RedEnemySpeed

            return None, False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)

    def update(self):
        return self.move()