import random
import time
from App import App
from Player import Player
from enemy.simple_enemy.RedEnemy import RedEnemy
from enemy.simple_enemy.RegularEnemy import RegularEnemy
from enemy.bombardier.Bombardier import Bombardier
from enemy.bombardier.SuperBombardier import SuperBombardier
from Boomerang import Boomerang


RegularCount = 0
RedCount = 0
y = 0

app = App()
obj = Player(60, 120, 5, 5)
app.add_player(obj)


while RegularCount <= 5:
    x = random.randrange(10, 120, 5)
    y -= 20
    NewEnemy = RegularEnemy(y, x, y)
    app.add_object(NewEnemy)
    RegularCount += 1


while RegularCount > 5 and RedCount < 5:
    y -= 20
    NewRed = RedEnemy(y, 20, y)
    app.add_object(RedEnemy(y, 20, y))
    RedCount += 1



app.add_object(SuperBombardier(20, 0))


app.run()
