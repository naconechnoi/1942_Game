
import time
from bullet.Bullet import PlayerBullet
from bullet.Bullet import EnemyBullet


class Gun:
    """Генерирует пули"""

    def shoot(self):
        raise Exception

    def generate_bullet(self):
        """Возвращает пульки"""
        raise Exception


class ScheduledGun(Gun):

    def __init__(self, time_gap: float):
        self.previous_shoot = time.time()
        self.time_gap = time_gap

    def shoot(self):
        """Если может стрелять, то возвращает пульку"""
        curr_time = time.time()
        if self.can_shoot(curr_time):
            self.previous_shoot = curr_time
            return self.generate_bullet()

        return None

    def can_shoot(self, curr_time):
        return curr_time - self.previous_shoot >= self.time_gap


class PlayerGun(ScheduledGun):

    def generate_bullet(self):
        return [PlayerBullet(), PlayerBullet()]


class EnemyGun(ScheduledGun):
    
    def generate_bullet(self):
        return [EnemyBullet()]
