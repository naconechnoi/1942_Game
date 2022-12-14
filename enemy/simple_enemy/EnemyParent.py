import pyxel
from gun.Gun import EnemyGun


class EnemyParent:
    """This is a parent class for Simple Enemies"""
    def __init__(self, x: float, y: float, height: float, width: float, color: int, enemy_speed: float):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.enemy_speed = enemy_speed
        self.counter_y = 0
        # defined time gap between bullets
        self.gun = EnemyGun(1)

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
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def enemy_speed(self):
        return self.__enemy_speed

    @enemy_speed.setter
    def enemy_speed(self, enemy_speed):
        self.__enemy_speed = enemy_speed

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def update(self, boomerang):
        raise Exception

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)

    def shoot(self, boomerang):
        """This method describes how all of the enemies shoot"""
        x_pos = self.x + (self.height + self.width) / 6
        y_pos = self.y - (self.height + self.width) / 72

        # generates bullets
        bullets = self.gun.shoot()

        if bullets is not None:

            bullets[0].x = x_pos
            bullets[0].y = y_pos

            # adding bullets in the special list
            boomerang.add_enemy_bullet(bullets[0])
