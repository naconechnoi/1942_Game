import pyxel

from screen.Screen import Screen


class GameOverScreen(Screen):

    def update(self, boomerang):
        if pyxel.btn(pyxel.KEY_SPACE):
            boomerang.screen = self.next_screen

    def draw(self):
        pyxel.cls(12)
        pyxel.text(50, 70, "-GAME OVER-", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS ENTER -", pyxel.frame_count % 3)