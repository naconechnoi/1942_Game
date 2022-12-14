from gun.Gun import EnemyGun


class BombardierParent:
    """This is a parent class for Bombardiers"""
    def __init__(self, x: float, y: float, radius: float, bombardier_speed: float):
        self.x = x
        self.y = y
        self.bombardier_speed = bombardier_speed
        self.radius = radius
        self.width = 6
        self.height = 6
        # defined time gap between bullets
        self.gun = EnemyGun(1.5)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def bombardier_speed(self):
        return self.__bombardier_speed

    @bombardier_speed.setter
    def bombardier_speed(self, bombardier_speed):
        self.__bombardier_speed = bombardier_speed

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def update(self, boomerang):
        raise Exception

    def draw(self):
        raise Exception

    def shoot(self, boomerang):
        """This method describes how all Bombardiers shoot"""
        x_pos = self.x - self.radius
        y_pos = self.y + self.radius / 4

        # generate bullets
        bullets = self.gun.shoot()

        if bullets is not None:

            bullets[0].x = x_pos
            bullets[0].y = y_pos

            # adding bullets in the special list
            boomerang.add_enemy_bullet(bullets[0])
