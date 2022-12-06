import pyxel
import Bullet


enemy_width = 6
enemy_height = 6
enemy_speed = 1
enemies = []


class RegularEnemy:

    def __init__(self, x: int = 50, y: int = 2, color: int = 1):
        self.x = x
        self.y = y
        self.w = enemy_width
        self.h = enemy_height
        self.color = color
        self.timer_offset = pyxel.rndi(0, 59)
        self.is_alive = True
        enemies.append(self)
        self.counter_y = 0

    def move(self):

        if self.counter_y <= 80:
            if (pyxel.frame_count + self.timer_offset) % 60 < 40:
                self.x += enemy_speed

            else:
                self.x -= enemy_speed

            if self.y > pyxel.height - 1:
                self.is_alive = False

            self.y += enemy_speed

            if self.y % 10 == 0:
                return self.shoot(), False

        if self.counter_y > 80:
            if (pyxel.frame_count + self.timer_offset) % 60 < 40:
                self.x += enemy_speed

            else:
                self.x -= enemy_speed

            if self.y > pyxel.height - 1:
                self.is_alive = False

            self.y -= enemy_speed

        self.counter_y += enemy_speed

        return None, False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)

    def update(self):
        return self.move()

    def shoot(self):
        x_pos = self.x + (self.h + self.w) / 6
        y_pos = self.y - (self.h + self.w) / 72

        return Bullet.BulletEnemy(x_pos, y_pos)