import pyxel
from gun.Gun import EnemyGun
from enemy.BombardierParent import Enemy


class Bombardier(Enemy):
    
    def __init__(self, obj, x=0, y=0):
        Enemy.__init__(self,x, y, 2, 1.8)
        self.obj = obj
        self.position_y = 0
        
    def update(self, boomerang):
        if self.obj.current_posY < 100:
            if self.position_y <= 70:

                self.y += self.bombardier_speed

                print(pyxel.height)
                print(self.y)
                """if self.y > pyxel.height - 1:
                    self.is_alive = False"""
            elif self.position_y:
                if 70 < self.position_y <= 100:
                    self.x += self.bombardier_speed
                elif 100 < self.position_y <= 130:
                    self.y -= self.bombardier_speed
                elif 130 < self.position_y <= 160:
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