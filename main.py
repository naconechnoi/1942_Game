import random
import time
from App import App
from Player import Player
from enemy.simple_enemy.RedEnemy import RedEnemy
from enemy.simple_enemy.RegularEnemy import RegularEnemy
from enemy.bombardier.Bombardier import Bombardier
from enemy.bombardier.SuperBombardier import SuperBombardier
from screen.GameScreen import GameScreen
from screen.MenuScreen import MenuScreen
from screen.GameOverScreen import GameOverScreen

menu_screen = MenuScreen()
game_screen = GameScreen()
game_over_screen = GameOverScreen()

# set up menu screen
menu_screen.next_screen = game_screen

# set up game screen
game_screen.next_screen = game_over_screen
obj = Player(60, 120, 5, 5)
game_screen.player = obj

RegularCount, RedCount = 0, 0
y = 0

for i in range(1, 21):

    if i % 2 == 0:
        while RegularCount <= 3:
            x = random.randrange(10, 120, 5)
            y -= 20
            game_screen.add_object(RegularEnemy(y, x, y))
            RegularCount += 1
        RegularCount = 0
        start = time.time()

    if i % 9 == 0:
        while RedCount < 5:
            x = random.randrange(20, 50, 10)
            y -= 20
            game_screen.add_object(RedEnemy(y, 20, y))
            RedCount += 1
        RedCount = 0



game_screen.add_object(Bombardier(obj, 30, -5))
game_screen.add_object(SuperBombardier(90, 170))

# set up game over screen
game_over_screen.next_screen = menu_screen

# set up app screen
app = App(menu_screen)
app.run()
