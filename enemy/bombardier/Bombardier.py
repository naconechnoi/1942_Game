import pyxel
from enemy.bombardier.BombardierParent import BombardierParent


class Bombardier(BombardierParent):
    """This is a Bombardier class"""
    def __init__(self, obj, middle, y=0, x=0):
        BombardierParent.__init__(self, x, y, 2, 1.8)
        self.obj = obj
        self.position_y = middle
        self.Flag = False
        
    def update(self, boomerang):
        """This method updates the way bombardier moves on a screen
        according to the placement of a Player"""
        if self.obj.current_posY < 100:
            self.Flag = True

        if self.Flag is True:
            if self.position_y <= 70:
                self.y += self.bombardier_speed
            else:
                # we ask him to make a square by his moves
                if 70 < self.position_y <= 130:
                    self.x += self.bombardier_speed
                elif 130 < self.position_y <= 160:
                    self.y -= self.bombardier_speed
                elif 160 < self.position_y <= 190:
                    self.x -= self.bombardier_speed
                else:
                    self.y -= self.bombardier_speed
                    self.x += self.bombardier_speed / 2

            self.position_y += self.bombardier_speed
            # generates bullets
            self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 9)