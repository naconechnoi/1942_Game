import pyxel
from enemy.bombardier.BombardierParent import BombardierParent


class SuperBombardier(BombardierParent):
    """This is a Super Bombardier class"""
    def __init__(self, x=0, y=0):
        BombardierParent.__init__(self, x, y, 3, 0.5)

    def update(self, boomerang):
        """This method defines its movements on a screen"""
        self.y += self.bombardier_speed

        # generates bullets
        self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 10)
