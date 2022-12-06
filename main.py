from App import App
from Player import Player
from RegularEnemy import RegularEnemy
from Bombardier import Bombardier

app = App()
app.add_object(Player(60, 120, 5, 5))
app.add_object(RegularEnemy())
app.add_object(Bombardier(30, 2))


app.run()