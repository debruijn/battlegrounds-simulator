import random
import numpy as np
from scripts.minion import Minion


class Deathrattle:

    def __init__(self, minion=None):
        self.minion = minion
        self.minion.add_deathrattle(self)

    def trigger(self):
        pass


class DamageDeathrattle(Deathrattle):

    def __init__(self, minion=None, damage=1):
        self.damage = damage
        super().__init__(minion)

    def trigger(self):
        target = self.minion.player.get_opponent().get_defender(ignore_taunt=True)
        target.take_damage(self.damage)


class SummonDeathrattle(Deathrattle):

    def __init__(self, minion=None, minion_type=Minion, summon_count=1):
        self.minion_type = minion_type
        self.summon_count = summon_count
        super().__init__(minion)

    def trigger(self):
        player = self.minion.player
        [self.minion_type(player) for __i in range(self.summon_count)]


class SummonDeathrattleOpponent(SummonDeathrattle):

    def trigger(self):
        opponent = self.minion.player.opponent
        [self.minion_type(opponent) for __i in range(self.summon_count)]


class SummonDeathrattleReplicatingMenace(SummonDeathrattle):

    def __init__(self, minion=None):
        from scripts.minion_catalogue import Microbot
        super().__init__(minion, minion_type=Microbot, summon_count=3)


class SummonDeathrattleRatPack(Deathrattle):

    def __init__(self, minion=None, minion_type=Minion):
        self.minion_type = minion_type
        super().__init__(minion)

    def trigger(self):
        player = self.minion.player
        [self.minion_type(player) for __i in range(self.minion.attack)]


class SummonRandomDeathrattle(Deathrattle):

    def __init__(self, minion=None, minion_types=None, summon_count=1):
        self.minion_types = minion_types
        self.summon_count = summon_count
        super().__init__(minion)

    def trigger(self):
        player = self.minion.player
        [random.choice(self.minion_types)(player) for __i in range(self.summon_count)]


class DivineShieldDeathrattle(Deathrattle):

    def trigger(self):
        player = self.minion.player
        if len(player.minions) > 0:
            random.choice(player.minions).divine_shield = True


class BuffDeathrattle(Deathrattle):

    def __init__(self, minion=None, buff_attack=1, buff_health=1, buff_count=1, distinct=True):
        self.buff_attack = buff_attack
        self.buff_health = buff_health
        self.distinct = distinct
        if buff_count == "all":
            self.buff_count = 7
        else:
            self.buff_count = buff_count

        super().__init__(minion)

    def apply_buff(self, minion):
        minion.attack += self.buff_attack
        minion.health += self.buff_health

    def get_feasible_minions(self, player):
        return player.minions

    def trigger(self):
        player = self.minion.player
        minions = self.get_feasible_minions(player)
        if self.distinct:
            buff_index = random.sample(range(len(minions)), k=np.min([len(minions), self.buff_count]))
        else:
            buff_index = random.choices(range(len(minions)), k=self.buff_count)
        [self.apply_buff(minions[i]) for i in buff_index]


class BuffDeathrattleTribe(BuffDeathrattle):

    def __init__(self, minion=None, buff_attack=1, buff_health=1, buff_count=1, tribe="Beast", distinct=True):
        self.tribe = tribe
        super().__init__(minion, buff_attack, buff_health, buff_count, distinct)

    def get_feasible_minions(self, player):
        minions = [m for m in player.minions if m.tribe == self.tribe]
        return minions


if __name__ == '__main__':
    from scripts.minion import Minion
    from scripts.player import Player

    player1 = Player()
    player2 = Player()
    minion1 = Minion(player1, attack=4, health=3)
    deathrattle = DamageDeathrattle(minion1, damage=2)
    defender = Minion(player2, attack=1, health=5)
    player1.set_opponent(player2)

    print(defender.health)
    minion1.trigger_deathrattles()
    print(defender.health)

    print(len(player2.minions))
    SummonDeathrattle(defender, Minion, 1)
    print(len(player2.minions))
    defender.deathrattle[0].trigger()
    print(f"Number deathrattles: {len(defender.deathrattle)}")
    print(len(player2.minions))
    defender.trigger_deathrattles()
    print(len(player2.minions))
    minion1.do_attack(defender)
    print(len(player2.minions))
    print(player2.minions)
