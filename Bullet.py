import pyxel


class Bullet:

    def __init__(self, x: float, y: float, speed: float, rotation: str):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.speed = speed
        self.height = 2
        self.width = 1

    def update(self, boomerang):
        if self.rotation == "up":
            if self.y - self.height > 0:
                self.y -= self.speed
            else:
                boomerang.remove_object(self)
        elif self.rotation == "down":
            if self.y - self.height > 0:
                self.y += self.speed
            else:
                boomerang.remove_object(self)

    def draw(self):
        pyxel.rect(self.x, self.y, self.height, self.width, 2)
