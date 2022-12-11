import pyxel
from ScreenBoomerang import ScreenBoomerang, AppBoomerang
from screen.MenuScreen import Screen


class App:

    def __init__(self, start_screen: Screen):
        self.curr_screen = start_screen

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
