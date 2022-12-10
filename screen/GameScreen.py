import pyxel

from ScreenBoomerang import ScreenBoomerang
from screen.Screen import Screen


class GameScreen(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.height = 120
        self.width = 160
        pyxel.init(self.height, self.width)
        self.objects = []
        self.curr_posY = 120

    def update(self, boomerang):

        if self.is_game_over():
            boomerang.screen = self.next_screen
        else:
            for obj in self.objects:
                boomerang = ScreenBoomerang()
                obj.update(boomerang)

                if not boomerang.is_add_list_empty():
                    for element in boomerang.get_add_list():
                        self.add_object(element)

                if not boomerang.is_delete_list_empty():
                    for element in boomerang.get_delete_list():
                        self.remove_object(element)

    def draw(self):
        pyxel.cls(12)
        for obj in self.objects:
            obj.draw()

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_object(self, obj):
        self.objects.append(obj)

    def is_game_over(self):
        if pyxel.btnp(pyxel.KEY_EQUALS):
            return True
        return False
