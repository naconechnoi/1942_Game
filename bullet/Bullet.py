import pyxel


class Bullet:
    """This is a class that describes a bullet"""
    def __init__(self, x: float, y: float, width: float, height: float, speed: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.height = height
        self.width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        self.__speed = speed

    def update(self, boomerang):
        raise Exception

    def draw(self):
        pyxel.rect(self.x, self.y, self.height, self.width, 2)


class PlayerBullet(Bullet):
    """This is a class that describes Players bullet"""
    def __init__(self, x=0, y=0):
        Bullet.__init__(self, x, y, 3, 3, 3)

    def update(self, boomerang):
        if self.y - self.height > 0:
            self.y -= self.speed
        else:
            boomerang.remove_player_bullet(self)


class EnemyBullet(Bullet):
    """This is a class that describes Enemies bullet"""
    def __init__(self, x=0, y=0):
        Bullet.__init__(self, x, y, 2, 2, 2)

    def update(self, boomerang):
        """This method updates position of a bullet
        and adds it to a remove list when it gets out of a screen"""
        if self.y - self.height > 0:
            self.y += self.speed
        else:
            boomerang.remove_enemy_bullet(self)
