import pyxel
from enemy.bombardier.BombardierParent import BombardierParent


class SuperBombardier(BombardierParent):

    def __init__(self, x=0, y=0):
        BombardierParent.__init__(self, x, y, 3, 0.5)

    def update(self, boomerang):
        self.y += self.bombardier_speed

        self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 10)
