import random
from scripts.minion import Minion

# Todo: add hero power effects at beginning of round for specific types of Players (Ragnaros, Lich King, etc)
# Todo: add check for player-broad effects (Baron Rivendare, Malganis)


class Player:

    def __init__(self, health=40, tavern_level=1, minion=None, minions=None):
        self.minions = []
        self.dead_minions = []
        self.opponent = 0
        self.health = health
        self.tavern_level = tavern_level
        self.next_attacker = 0
        self.max_minions = 7
        if minions is not None:
            [self.add_minion(minion) for minion in minions]
            [minion.set_player(self) for minion in minions]
        elif minion is not None:
            self.add_minion(minion)
            minion.set_player(self)

    def set_opponent(self, opponent):
        self.opponent = opponent

    def get_opponent(self):
        return self.opponent

    def add_minion(self, minion):
        if len(self.minions) < self.max_minions:
            self.minions.append(minion)

    def set_dead(self, minion):
        dead_index = self.minions.index(minion)
        self.minions.pop(dead_index)
        if dead_index < self.next_attacker:
            self.next_attacker -= 1
        if dead_index >= len(self.minions):
            self.next_attacker = 0
        self.dead_minions.append(minion)
        # Todo: also add dead minion to dead minions in the round
        # Todo: trigger on-death effects

    def check_alive(self):
        return len(self.minions) > 0

    def get_defender(self, swipe=False):
        if swipe and (len(self.minions) > 1):
            defender_index = random.randint(0, len(self.minions))
            if defender_index == 0:
                defender = [self.minions[defender_index], self.minions[defender_index + 1]]
            elif defender_index == len(self.minions) - 1:
                defender = [self.minions[defender_index], self.minions[defender_index - 1]]
            else:
                defender = [self.minions[defender_index], self.minions[defender_index - 1],
                            self.minions[defender_index + 1]]

        else:
            defender = random.choice(self.minions)

        return defender  # Todo: add check for taunt minions; if so, select from them

    def get_lowest_attack_defender(self):
        return random.choice(self.minions)  # Todo: return (1 of the) minions with lowest attack

    def update_attacker(self):
        self.next_attacker += 1
        if self.next_attacker >= len(self.minions):
            self.next_attacker = 0

    def get_attacker(self):
        attacker = self.minions[self.next_attacker]
        return attacker

    def do_attack(self):
        minion = self.get_attacker()
        minion.do_combat()
        self.update_attacker()


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
