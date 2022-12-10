
class Screen:

    def __init__(self):
        self.next_screen = None

    @property
    def next_screen(self):
        return self.__next_screen

    @next_screen.setter
    def next_screen(self, next_screen):
        self.__next_screen = next_screen

    def update(self, boomerang):
        raise Exception

    def draw(self):
        raise Exception
