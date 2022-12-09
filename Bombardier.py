import pyxel
import math
import Bullet


class Bombardier:

    def __init__(self, x: int, y: int, obj):
        self.x = x
        self.y = y
        self.bombardier_speed = 1.8
        self.radius = 2
        self.is_alive = True
        self.position_y = 0
        self.obj = obj
        self.t = 0.1

    def update(self, boomerang):
        if self.obj.current_posY < 100:
            if self.position_y <= 70:

                self.y += self.bombardier_speed

                if self.y > pyxel.height - 1:
                    self.is_alive = False
            else:
                res_x = 2 * math.sin(self.t)
                res_y = 2 * math.cos(self.t)
                self.t += 0.1
                self.x += res_x
                self.y += res_y

                if self.y > pyxel.height - 1:
                    self.is_alive = False

            self.position_y += self.bombardier_speed

            boomerang.add_object(self.shoot())

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 9)

    def shoot(self):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4

        return Bullet.Bullet(x_pos, y_pos, 4, "down")
