import pyxel
from Boomerang import Boomerang

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
                boomerang = Boomerang()
                print(obj)
                obj.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_object(self, obj):
        self.objects.append(obj)

    def run(self):
        pyxel.run(self.update, self.draw)