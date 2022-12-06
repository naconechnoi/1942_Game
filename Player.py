import pyxel
import Bullet


class Player:

    def __init__(self, x: float, y: float, radius: float, color: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.current_posY = 120

    def move(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x + self.radius < 120:
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x - self.radius > 0:
            self.x -= 1
        if pyxel.btn(pyxel.KEY_UP) and self.y - self.radius > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y + self.radius < 160:
            self.y += 1
        #if pyxel.btn(pyxel.KEY_SPACE):
        self.current_posY = self.y
       # print(self.current_posY)
        return self.shoot(), False

        #return None, False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

    def update(self):
        return self.move()

    def shoot(self):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius/4

        return Bullet.Bullet(x_pos, y_pos, 4, "up")
