
import pyxel


class Player:

    def __init__(self, x: int, y: int):
        pyxel.init(120, 160)
        self.x = x
        self.y = y
        pyxel.run(self.update, self.draw)

    def move(self):
        if self.x + 10 < 120 and pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        elif pyxel.btn(pyxel.KEY_LEFT) and self.x - 10 > 0:
            self.x -= 1
        elif pyxel.btn(pyxel.KEY_UP) and self.y - 10 > 0:
            self.y -= 1
        elif pyxel.btn(pyxel.KEY_DOWN) and self.y + 10 < 160:
            self.y += 1


    def draw(self):
        pyxel.cls(12)
        pyxel.circ(50, 80, 10, 6)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            self.move()
