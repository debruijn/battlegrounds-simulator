import random


class Minion:

    def __init__(self, player, attack=1, health=1, name=None, stars=1, mana=1):
        self.attack = attack
        self.health = health
        self.player = player
        self.stars = stars
        self.mana = mana
        self.buff_attack = 0  # Todo: implement attack and health buffs into combat
        self.buff_health = 0
        if name is None:
            self.name = random.random()
        else:
            self.name = name
        #print(f'Minion {self.name} with stats {self.attack},{self.health} created.')

    def find_target(self):
        return self.player.get_opponent().get_defender()  # Todo: overwrite in case attacker is Zapp

    def take_damage(self, damage):  # Todo: implement poisonous, divine shield
        self.health -= damage
        if self.health <= 0:
            self.player.set_dead(self)
            # Todo: add deathrattles
        #    print(f'Minion {self.name} has died!')

    def do_attack(self, minion):
        self.take_damage(minion.attack)
        minion.take_damage(self.attack)
        #print(f'Minion {self.name} has {self.health} health remaining. '
        #      f'Opponent {minion.name} has {minion.health} health remaining.')

    def combat(self):  # Todo: implement windfury, swipe
        target = self.find_target()
        self.do_attack(target)


if __name__ == '__main__':
    m1 = Minion(4, 3)
    m2 = Minion(1, 5)
    m1.do_attack(m2)
