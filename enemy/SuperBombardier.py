import pyxel
from gun.Gun import EnemyGun

class SuperBombardier:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.bombardier_speed = 0.5
        self.radius = 3
        self.is_alive = True
        self.gun = EnemyGun(2)

    def update(self, boomerang):

        self.y -= self.bombardier_speed

        self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 10)


    def shoot(self, boomerang):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4

        bullets = self.gun.shoot()
        if bullets != None:
            bullets[0].x = x_pos
            bullets[0].y = y_pos

            boomerang.add_object(bullets[0])


        #return Bullet.Bullet(x_pos, y_pos, 4, "down")
