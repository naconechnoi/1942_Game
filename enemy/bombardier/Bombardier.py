import pyxel
from enemy.bombardier.BombardierParent import BombardierParent


class Bombardier(BombardierParent):
    
    def __init__(self, obj, x=0, y=0):
        BombardierParent.__init__(self, x, y, 2, 1.8)
        self.obj = obj
        self.position_y = 0
        self.Flag = False
        
    def update(self, boomerang):
        if self.obj.current_posY < 100:
            self.Flag = True

        if self.Flag == True:
            if self.position_y <= 70:

                self.y += self.bombardier_speed

                #print(self.obj.current_posY)
                #print(self.position_y)
                #print(self.y)
                """if self.y > pyxel.height - 1:
                    self.is_alive = False"""
            else:
                if 70 < self.position_y <= 130:
                    self.x += 1*(self.bombardier_speed)
                elif 130 < self.position_y <= 160:
                    self.y -= self.bombardier_speed
                elif 160 < self.position_y <= 190:
                    self.x -= self.bombardier_speed
                else:
                    self.y -= self.bombardier_speed
                    self.x += self.bombardier_speed / 2
                """if self.y > pyxel.height - 1:
                    self.is_alive = False"""
            self.position_y += self.bombardier_speed
            self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 9)