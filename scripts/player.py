import random
from scripts.minion import Minion


class Player:

    def __init__(self):
        self.minions = []
        self.dead_minions = []
        self.opponent = 0

    def set_opponent(self, opponent):
        self.opponent = opponent

    def get_opponent(self):
        return self.opponent

    def add_minion(self, minion):
        self.minions.append(minion)

    def set_dead(self, minion):
        self.minions.pop(self.minions.index(minion))
        self.dead_minions.append(minion)

    def check_alive(self):
        return len(self.minions) > 0

    def get_defender(self):
        return random.choice(self.minions)

    def get_attacker(self):
        return random.choice(self.minions)

    def do_attack(self):
        minion = self.get_attacker()
        minion.combat()


if __name__ == "__main__":
    player1 = Player()
    player1.add_minion(Minion(player1, 2, 3))
    player1.add_minion(Minion(player1, 3, 5))

    player2 = Player()
    player2.add_minion(Minion(player2, 1, 12))

    player1.set_opponent(player2)
    player2.set_opponent(player1)

    for i in range(5):
        player1.do_attack()
        player2.do_attack()
