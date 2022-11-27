
import pyxel


class App:

    def __init__(self):
        pyxel.init(120, 160)
        pyxel.run(self.update, self.draw_title)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw_title(self):
        pyxel.cls(12)
        pyxel.text(50, 70, "1942", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS ENTER -", pyxel.frame_count % 3)


