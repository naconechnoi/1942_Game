import random
from App import App
from Player import Player
from enemy.simple_enemy.RedEnemy import RedEnemy
from enemy.simple_enemy.RegularEnemy import RegularEnemy
from enemy.bombardier.Bombardier import Bombardier
from enemy.bombardier.SuperBombardier import SuperBombardier
from screen.GameScreen import GameScreen
from screen.MenuScreen import MenuScreen
from screen.GameOverScreen import GameOverScreen

Enemies = []
EnemyCount = 0
y = 0

menu_screen = MenuScreen()
game_screen = GameScreen()
game_over_screen = GameOverScreen()

# set up menu screen
menu_screen.next_screen = game_screen

# set up game screen
game_screen.next_screen = game_over_screen
obj = Player(60, 120, 5, 5)
game_screen.add_object(obj)

game_screen.add_object(RegularEnemy(20, 100))

game_screen.add_object(Bombardier(obj, 30, -5))
game_screen.add_object(SuperBombardier(90, 160))
game_screen.add_object(RedEnemy(10, 5))

# set up game over screen
game_over_screen.next_screen = menu_screen

# set up app screen
app = App(menu_screen)
app.run()

"""while EnemyCount <= 5: # всего должно быть 20 врагов (5 * 4 ? Каждые 100/50
    # очков будут вылетать)
    x = random.randrange(10, 120, 5)
    y -= 20
    NewEnemy = RegularEnemy(x, y, y)
    app.add_object(RegularEnemy(x, y, y))
    EnemyCount += 1"""

