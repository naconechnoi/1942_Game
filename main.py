from App import App
from Player import Player
from RegularEnemy import RegularEnemy
from Bombardier import Bombardier
from SuperBombardier import SuperBombardier

app = App()
obj = Player(60, 120, 5, 5)
app.add_object(obj)
app.add_object(RegularEnemy())
app.add_object(Bombardier(30, -5, obj))
app.add_object(SuperBombardier(90, 160))


app.run()
