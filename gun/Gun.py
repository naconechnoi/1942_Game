
import time
from bullet.Bullet import PlayerBullet
from bullet.Bullet import EnemyBullet


class Gun:
    """"This abstract class generates bullets"""

    def shoot(self):
        raise Exception

    def generate_bullet(self):
        raise Exception


class ScheduledGun(Gun):
    """This class describes a time gap between bullets
     that were shoot and whether bullets can be shoot"""
    def __init__(self, time_gap: float):
        self.previous_shoot = time.time()
        self.time_gap = time_gap

    def shoot(self):
        """This method tell that if gun can shoot,
        it generates a bullet"""
        curr_time = time.time()
        if self.can_shoot(curr_time):
            self.previous_shoot = curr_time
            return self.generate_bullet()

        return None

    def can_shoot(self, curr_time):
        """This method checks whether time gap was observed"""
        return curr_time - self.previous_shoot >= self.time_gap


class PlayerGun(ScheduledGun):
    """This is a class for a Players bullets"""
    def generate_bullet(self):
        return [PlayerBullet(), PlayerBullet()]


class EnemyGun(ScheduledGun):
    """This is a class for Enemies bullets"""
    def generate_bullet(self):
        return [EnemyBullet()]
