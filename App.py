import pyxel
from ScreenBoomerang import AppBoomerang

from screen.MenuScreen import MenuScreen



class App:

    def __init__(self, curr_screen, height, width):
        self.height = height
        self.width = width
        pyxel.init(self.height, self.width)
        self.curr_screen = curr_screen

    def update(self):
        boomerang = AppBoomerang()
        self.curr_screen.update(boomerang)
        next_screen = boomerang.screen

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif next_screen is not None:
            self.curr_screen = next_screen

    def draw(self):
        self.curr_screen.draw()

    def run(self):
        pyxel.run(self.update, self.draw)
