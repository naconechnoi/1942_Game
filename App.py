
import pyxel


class App:

    def __init__(self):
        WIDTH = 520
        HEIGHT = 760
        pyxel.init(WIDTH, HEIGHT)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(12)