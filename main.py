import random
from App import App
from Player import Player
from RegularEnemy import RegularEnemy
from Bombardier import Bombardier
from SuperBombardier import SuperBombardier
from RedEnemy import RedEnemy

Enemies = []
EnemyCount = 0
y = 0

app = App()
obj = Player(60, 120, 5, 5)
app.add_object(obj)
 
# добавить нижний цикл в функцию которая будет их размножать

while EnemyCount <= 5: # всего должно быть 20 врагов (5 * 4 ? Каждые 100/50
    # очков будут вылетать)
    x = random.randrange(10, 120, 5)
    y -= 20
    NewEnemy = RegularEnemy(x, y, y)
    app.add_object(RegularEnemy(x, y, y))
    EnemyCount += 1

app.add_object(Bombardier(30, -5, obj))
app.add_object(SuperBombardier(90, 160))
app.add_object(RedEnemy(10, 5))

app.run()
