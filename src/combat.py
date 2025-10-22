class Combat:
    def __init__(self):
        self.enemy_health = 100
        self.player_health = 100

    def attack(self, damage):
        self.enemy_health -= damage
        if self.enemy_health <= 0:
            print("Enemy defeated!")

