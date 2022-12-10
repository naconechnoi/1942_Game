import pyxel

from screen.Screen import Screen


class GameOverScreen(Screen):

    def update(self, boomerang):
        if pyxel.btn(pyxel.KEY_MINUS):
            boomerang.screen = self.next_screen

    def draw(self):
        pyxel.cls(12)
        pyxel.text(40, 70, "-GAME OVER-", pyxel.frame_count % 12)
        pyxel.rectb(25, 63, 70, 20, pyxel.frame_count % 12)
        pyxel.text(26, 135, """- PRESS  " - " TO -\n    START AGAIN""", pyxel.frame_count % 3)
