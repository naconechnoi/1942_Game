import pyxel
from gun.Gun import PlayerGun


class Player:

    def __init__(self, x: float, y: float, radius: float, color: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.gun = PlayerGun(0.5)
        self.current_posY = 120

    def update(self, boomerang):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x + self.radius < 120:
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x - self.radius > 0:
            self.x -= 1
        if pyxel.btn(pyxel.KEY_UP) and self.y - self.radius > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y + self.radius < 160:
            self.y += 1
        self.current_posY = self.y

        self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

    def shoot(self, boomerang):

        x_pos1 = self.x - self.radius
        x_pos2 = self.x + self.radius
        y_pos = self.y + self.radius/4
        bullets = self.gun.shoot()

        if bullets is not None:
            bullets[0].x = x_pos1
            bullets[1].x = x_pos2

            for bullet in bullets:
                bullet.y = y_pos
                boomerang.add_player_bullet(bullet)
