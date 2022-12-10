import pyxel

from screen.Screen import Screen


class MenuScreen(Screen):

    def update(self, boomerang):
        if pyxel.btn(pyxel.KEY_SPACE):

            boomerang.screen = self.next_screen
            print(boomerang.screen)

    def draw(self):
        pyxel.cls(12)
        pyxel.text(50, 70, "1942", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS SPACE -", pyxel.frame_count % 3)
