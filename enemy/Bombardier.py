import pyxel
from gun.Gun import EnemyGun

class Bombardier:

    def __init__(self, x: int, y: int, obj):
        self.x = x
        self.y = y
        self.bombardier_speed = 1.8
        self.radius = 2
        self.is_alive = True
        self.position_y = 0
        self.obj = obj
        self.gun = EnemyGun(8)

    def update(self, boomerang):
        if self.obj.current_posY < 100:
            if self.position_y <= 70:

                self.y += self.bombardier_speed

                if self.y > pyxel.height - 1:
                    self.is_alive = False
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
                if self.y > pyxel.height - 1:
                    self.is_alive = False
            self.position_y += self.bombardier_speed

            self.shoot(boomerang)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, 9)

    def shoot(self, boomerang):

        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4
        bullets = self.gun.shoot()

        if bullets != None:

            bullets[0].x = x_pos
            bullets[0].y = y_pos

            boomerang.add_object(bullets[0])


        # return Bullet.Bullet(x_pos, y_pos, 4, "down")
