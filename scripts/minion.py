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
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.poisonous = False
        self.swipe = False
        if name is None:
            self.name = random.random()
        else:
            self.name = name

    def find_target(self):
        return self.player.get_opponent().get_defender(self.swipe)  # Todo: overwrite in case attacker is Zapp

    def take_damage(self, damage, poisonous):
        if self.divine_shield:
            self.divine_shield = False  # TODO: add trigger for "on removal of divine shield"
        else:
            self.health -= damage
            if self.health > 0 and poisonous:
                self.health = 0
            if self.health <= 0:
                self.player.set_dead(self)
                # Todo: add deathrattles

    def do_attack(self, minion):
        if isinstance(minion, list):  # List returned in case of swipe attack
            minions = minion
            minion = minions.pop(0)
            for other_minions in minions:  # Swipe damage
                other_minions.take_damage(self.attack, self.poisonous)  # Todo: check order of swipe effects
        self.take_damage(minion.attack, minion.poisonous)
        minion.take_damage(self.attack, self.poisonous)

    def do_combat(self):
        target = self.find_target()
        self.do_attack(target)
        if self.windfury and self.health>0:
            target = self.find_target()
            self.do_attack(target)


if __name__ == '__main__':
    m1 = Minion(4, 3)
    m2 = Minion(1, 5)
    m1.do_attack(m2)
