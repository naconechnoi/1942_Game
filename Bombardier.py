import pyxel
import Bullet

class Bombardier:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.bombardier_speed = 1.8
        self.radius = 2
        self.is_alive = True
        self.position_y = 0

    def move(self):

        if self.position_y <= 70:

            self.y += self.bombardier_speed

            if self.y > pyxel.height - 1:
                self.is_alive = False
        else:

            if 70 < self.position_y <= 100:
                self.x += self.bombardier_speed
            elif 100 < self.position_y <= 130:
                self.y -= self.bombardier_speed
            elif 130 < self.position_y <= 160:
                self.x -= self.bombardier_speed
            else:
                self.y -= self.bombardier_speed
                self.x += self.bombardier_speed / 2

            if self.y > pyxel.height - 1:
                self.is_alive = False

        self.position_y += self.bombardier_speed

        return self.shoot(), False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 9)

    def update(self):
        return self.move()

    def shoot(self):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4

        return Bullet.Bullet(x_pos, y_pos, 4, "down")