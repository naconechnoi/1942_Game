import pyxel

from screen.Screen import Screen


class GameOverScreen(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.score = 0

    def update(self, boomerang):
        if pyxel.btn(pyxel.KEY_MINUS):
            boomerang.screen = self.next_screen.get_instance(self.next_screen.next_screen)

    def draw(self):
        pyxel.cls(12)
        pyxel.text(40, 70, "-GAME OVER-", pyxel.frame_count % 12)
        pyxel.rectb(25, 63, 70, 20, pyxel.frame_count % 12)
        pyxel.text(26, 135, """- PRESS  " - " TO -\n    START AGAIN""", pyxel.frame_count % 3)
        pyxel.text(39, 4, f"SCORE: {self.score:5}", 7)

    def set_score(self, score):
        self.score = score

    def get_instance(self, next_screen):
        game_over_screen = GameOverScreen()
        game_over_screen.next_screen = next_screen
        return game_over_screen
