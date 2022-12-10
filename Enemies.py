import random

def ForRegularEnemy():
    EnemyCount = 5
    y = 0

    while EnemyCount <= 5:
        x = random.randrange(10, 120, 5)
        y -= 20
        EnemyCount += 1
        return x, y


