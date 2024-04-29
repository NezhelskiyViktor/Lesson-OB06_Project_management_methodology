class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 20

    def attack(self, oher):
        oher.health -= self.power

    def is_alive(self):
        return self.health > 0
