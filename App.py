import pyxel


class App:

    def __init__(self):
        self.height = 120
        self.width = 160
        pyxel.init(self.height, self.width)
        self.objects = []

    def draw_title(self):
        pyxel.cls(12)
        pyxel.text(50, 70, "1942", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS ENTER -", pyxel.frame_count % 3)

    def draw(self):
        self.draw_title()
        pyxel.cls(12)
        for obj in self.objects:
            obj.draw()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            for obj in self.objects:
                res, to_del = obj.update()

                if res is not None:
                    self.objects.append(res)

                if to_del is not None and to_del:
                    self.objects.remove(obj)

    def add_object(self, obj):
        self.objects.append(obj)

    def run(self):
        pyxel.run(self.update, self.draw)
