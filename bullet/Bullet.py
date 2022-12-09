import pyxel


class Bullet:

    def __init__(self, x: float, y: float, width: float, height: float, speed: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.height = height
        self.width = width


    def update(self, boomerang):
        raise Exception

    def draw(self):
        pyxel.rect(self.x, self.y, self.height, self.width, 2)


class PlayerBullet(Bullet):

    def __init__(self, x=0, y=0):
        Bullet.__init__(self, x, y, 3, 3, 3)

    def update(self, boomerang):
        if self.y - self.height > 0:
            self.y -= self.speed
        else:
            boomerang.remove_object(self)


class EnemyBullet(Bullet):

    def __init__(self, x=0, y=0):
        Bullet.__init__(self, x, y, 2, 2, 2)

    def update(self, boomerang):
        if self.y - self.height > 0:
            self.y += self.speed
        else:
            boomerang.remove_object(self)