import pyxel
import Bullet


class SuperBombardier:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.bombardier_speed = 0.5
        self.radius = 3
        self.is_alive = True

    def move(self):

        self.y -= self.bombardier_speed

        return self.shoot(), False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 10)

    def update(self):
        return self.move()

    def shoot(self):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4

        return Bullet.Bullet(x_pos, y_pos, 4, "down")
