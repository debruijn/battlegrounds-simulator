from scripts.minion import Minion
from scripts.deathrattle import SummonDeathrattle, SummonRandomDeathrattle, DivineShieldDeathrattle, DamageDeathrattle, \
    SummonDeathrattleRatPack, BuffDeathrattle


class Annoyotron(Minion):

    def __init__(self, player=None, attack=1, health=2, name="Annoy-o-tron"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=2)
        self.taunt = True
        self.divine_shield = True
        self.tribe = "Mech"


class InfestedWolf(Minion):

    def __init__(self, player=None, attack=3, health=3, name="Infested Wolf"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)
        self.tribe = "Beast"
        SummonDeathrattle(self, Spider, 2)


class Spider(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Spider"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Beast"
        self.random_summon = False


class Mecharoo(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Mecharoo"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Mech"
        SummonDeathrattle(self, JoEBot, 1)


class JoEBot(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Jo-E Bot"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Mech"
        self.random_summon = False


class Alleycat(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Alleycat"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Beast"


class Tabbycat(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Tabbycat"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Beast"
        self.random_summon = False


class MicroMachine(Minion):

    def __init__(self, player=None, attack=1, health=2, name="Micro Machine"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.tribe = "Mech"


class MurlocTidecaller(Minion):

    def __init__(self, player=None, attack=1, health=2, name="Murloc Tidecaller"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Murloc"


class MurlocTidehunter(Minion):

    def __init__(self, player=None, attack=2, health=1, name="Murloc Tidehunter"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.tribe = "Murloc"


class MurlocScout(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Murloc Scout"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Murloc"
        self.random_summon = False


class RighteousProtector(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Righteous Protector"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.divine_shield = True
        self.taunt = True


class RockpoolHunter(Minion):

    def __init__(self, player=None, attack=2, health=3, name="Rockpool Hunter"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.tribe = "Murloc"


class SelflessHero(Minion):

    def __init__(self, player=None, attack=2, health=1, name="Selfless Hero"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        DivineShieldDeathrattle(self)


class Voidwalker(Minion):

    def __init__(self, player=None, attack=1, health=3, name="Voidwalker"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.taunt = True
        self.tribe = "Demon"


class VulgarHomunculus(Minion):

    def __init__(self, player=None, attack=2, health=4, name="Vulgar Homunculus"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.taunt = True
        self.tribe = "Demon"


class WrathWeaver(Minion):

    def __init__(self, player=None, attack=1, health=1, name="WrathWeaver"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)


class MountedRaptor(Minion):

    def __init__(self, player=None, attack=3, health=2, name="Mounted Raptor"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        OneCostMinions = [Alleycat, Mecharoo, MurlocTidecaller, RighteousProtector, SelflessHero,
                          Voidwalker, WrathWeaver]  # TODO: make this dynamic
        SummonRandomDeathrattle(self, OneCostMinions)
        self.tribe = "Beast"


class ColdlightSeer(Minion):

    def __init__(self, player=None, attack=2, health=3, name="Coldlight Seer"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        self.tribe = "Murloc"


class HarvestGolem(Minion):

    def __init__(self, player=None, attack=2, health=3, name="Harvest Golem"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        SummonDeathrattle(self, DamagedGolem)
        self.tribe = "Mech"


class DamagedGolem(Minion):

    def __init__(self, player=None, attack=2, health=1, name="Damaged Golem"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Mech"
        self.random_summon = False


class KaboomBot(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Kaboom Bot"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        DamageDeathrattle(self, 4)
        self.tribe = "Mech"


class KindlyGrandmother(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Kindly Grandmother"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=2)
        SummonDeathrattle(self, BigBadWolf)
        self.tribe = "Beast"


class BigBadWolf(Minion):

    def __init__(self, player=None, attack=3, health=2, name="Big Bad Wolf"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.tribe = "Beast"
        self.random_summon = False


class MetaltoothLeaper(Minion):

    def __init__(self, player=None, attack=3, health=3, name="Metaltooth Leaper"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        self.tribe = "Mech"


class NathrezimOverseer(Minion):

    def __init__(self, player=None, attack=2, health=4, name="Nathrezim Overseer"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        self.tribe = "Demon"


class NightmareAmalgam(Minion):

    def __init__(self, player=None, attack=3, health=4, name="Nightmare Amalgam"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        self.tribe = "All"


class PogoHopper(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Pogo-Hopper"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=1)
        self.tribe = "Mech"


class RatPack(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Rat Pack"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        SummonDeathrattleRatPack(self, Rat)
        self.tribe = "Beast"


class Rat(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Rat"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Beast"
        self.random_summon = False


class ShieldedMinibot(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Shielded Minibot"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=2)
        self.divine_shield = True


class SpawnOfNZoth(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Spawn of N'Zoth"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        BuffDeathrattle(self, buff_count="all")


class Zoobot(Minion):

    def __init__(self, player=None, attack=3, health=3, name="Zoobot"):
        super().__init__(player, name=name, attack=attack, health=health, stars=2, mana=3)
        self.tribe = "Mech"

# TODO: Dire Wolf Alpha, Murloc Warleader, Old Murk-Eye, Scavenging Hyena, all minions >=3 stars


if __name__ == "__main__":
    from scripts.player import Player
    player = Player(minion=MountedRaptor())
    player.minions[0].trigger_deathrattles()
