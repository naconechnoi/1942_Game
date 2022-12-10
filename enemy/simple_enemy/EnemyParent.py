import pyxel
from gun.Gun import EnemyGun


class EnemyParent:

    def __init__(self, x: float, y: float, height: float, width: float, color: int, enemy_speed: float):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.enemy_speed = enemy_speed
        #self.is_alive = True
        self.counter_y = 0
        self.gun = EnemyGun(1)

    def update(self, boomerang):
        raise Exception

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

    def shoot(self, boomerang):
        x_pos = self.x + (self.height + self.width) / 6
        y_pos = self.y - (self.height + self.width) / 72

        bullets = self.gun.shoot()
        if bullets is not None:
            bullets[0].x = x_pos
            bullets[0].y = y_pos

            boomerang.add_object(bullets[0])