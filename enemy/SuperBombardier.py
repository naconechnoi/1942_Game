import pyxel
from enemy.BombardierParent import Enemy


class SuperBombardier(Enemy):

    def __init__(self, x=0, y=0):
        Enemy.__init__(self, x, y, 3, 0.5)

    def update(self, boomerang):
        self.y -= self.bombardier_speed

        self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 10)
