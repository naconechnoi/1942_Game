import pyxel

from screen.Screen import Screen


class MenuScreen(Screen):
    """This class describes a Menu screen of a game"""
    def update(self, boomerang):
        """This method updates screens by pressing on the SPACE button.
                Menu screen changes to Game screen"""
        if pyxel.btn(pyxel.KEY_SPACE):
            boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)
            print(boomerang.screen)

    def draw(self):
        """This method draws a Menu screen"""
        pyxel.cls(12)
        pyxel.text(50, 70, "1942", pyxel.frame_count % 12)
        pyxel.rectb(38, 63, 40, 20, pyxel.frame_count % 12)
        pyxel.text(30, 135, "- PRESS SPACE -", pyxel.frame_count % 3)

    def get_instance(self, next_screen):
        """This method sets next screen and return the current one (menu screen)"""
        menu_screen = MenuScreen()
        menu_screen.next_screen = next_screen
        return menu_screen


