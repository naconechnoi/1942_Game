import pyxel


class Bullet:

    def __init__(self, x: float, y: float, speed: float):
        self.x = x
        self.y = y

        self.speed = speed

        self.height = 2
        self.width = 1

    def move(self):
        if self.y - self.height > 0:
            self.y -= self.speed
        else:
            return None, True

        return None, False

    def draw(self):
        pyxel.rect(self.x, self.y, self.height, self.width, 2)

    def update(self):
        return self.move()
