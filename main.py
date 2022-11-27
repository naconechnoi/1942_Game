from App import App
from Player import Player

app = App()
app.add_object(Player(60, 120, 5, 5))

app.run()