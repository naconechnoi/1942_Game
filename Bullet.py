import pyxel

height_bullet = 2
width_bullet = 1
bullet_speed = 2
bullets = []


class Bullet:

    def __init__(self, x: float, y: float, speed: float):
        self.x = x
        self.y = y

        self.speed = speed

        self.height = height_bullet
        self.width = width_bullet

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


class BulletEnemy():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = width_bullet
        self.h = height_bullet
        self.is_alive = True
        bullets.append(self)

    def move(self):
        self.y += bullet_speed
        if self.y + self.h - 1 < 0:
            self.is_alive = False
        return None, False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 5)

    def update(self):
        return self.move()

