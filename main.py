from App import App
from Player import Player
from RegularEnemy import RegularEnemy

app = App()
app.add_object(Player(60, 120, 5, 5))
app.add_object(RegularEnemy())

app.run()