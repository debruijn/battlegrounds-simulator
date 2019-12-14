from scripts.minion import Minion
from scripts.deathrattle import SummonDeathrattle, SummonRandomDeathrattle, DivineShieldDeathrattle, \
    DamageDeathrattle, SummonDeathrattleRatPack, BuffDeathrattle, SummonDeathrattleReplicatingMenace, \
    SummonDeathrattleOpponent, BuffDeathrattleTribe


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
                          Voidwalker, WrathWeaver, ShifterZerus, Toxfin]  # TODO: make this dynamic
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


class CrowdFavorite(Minion):

    def __init__(self, player=None, attack=4, health=4, name="Crowd Favorite"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)


class Crystalweaver(Minion):

    def __init__(self, player=None, attack=5, health=4, name="Crystalweaver"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)


class FloatingWatcher(Minion):

    def __init__(self, player=None, attack=4, health=4, name="Floating Watcher"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=5)
        self.tribe = "Demon"


class Houndmaster(Minion):

    def __init__(self, player=None, attack=4, health=3, name="Houndmaster"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)


class PilotedShredder(Minion):

    def __init__(self, player=None, attack=4, health=3, name="Piloted Shredder"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)
        twoCostMinions = [Annoyotron, MicroMachine, MurlocTidehunter, RockpoolHunter, VulgarHomunculus,
                          KindlyGrandmother, ShieldedMinibot]  # TODO: make this dynamic, or a ref table
        SummonRandomDeathrattle(self, twoCostMinions)
        self.tribe = "Mech"


class Psychotron(Minion):

    def __init__(self, player=None, attack=3, health=4, name="Psych-o-tron"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=5)
        self.tribe = "Mech"
        self.taunt = True
        self.divine_shield = True


class ReplicatingMenace(Minion):

    def __init__(self, player=None, attack=3, health=1, name="Replicating Menace"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)
        SummonDeathrattleReplicatingMenace(self)
        self.tribe = "Mech"


class Microbot(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Microbot"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Mech"
        self.random_summon = False


class ScrewjankClunker(Minion):

    def __init__(self, player=None, attack=2, health=5, name="Screwjank Clunker"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)
        self.tribe = "Mech"


class ShifterZerus(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Shifter Zerus"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=1)


class TortollanShellraiser(Minion):

    def __init__(self, player=None, attack=2, health=6, name="Tortollan Shellraiser"):
        super().__init__(player, name=name, attack=attack, health=health, stars=3, mana=4)
        BuffDeathrattle(self, buff_count=1)


class AnnoyoModule(Minion):

    def __init__(self, player=None, attack=2, health=4, name="Annoy-o-Module"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=4)
        self.tribe = "Mech"
        self.taunt = True
        self.divine_shield = True


class CaveHydra(Minion):

    def __init__(self, player=None, attack=2, health=4, name="Cave Hydra"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=3)
        self.tribe = "Beast"
        self.swipe = True


class DefenderOfArgus(Minion):

    def __init__(self, player=None, attack=2, health=3, name="Defender of Argus"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=4)


class IronSensei(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Iron Sensei"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=3)
        self.tribe = "Mech"


class MenagerieMagician(Minion):

    def __init__(self, player=None, attack=4, health=4, name="Menagerie Magician"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=5)


class PilotedSkyGolem(Minion):

    def __init__(self, player=None, attack=6, health=4, name="Piloted Sky Golem"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=6)
        fourCostMinions = [PilotedShredder, DefenderOfArgus, AnnoyoModule, TortollanShellraiser, ScrewjankClunker,
                           ReplicatingMenace, Houndmaster, Crystalweaver, CrowdFavorite, InfestedWolf, GentleMegasaur,
                           StrongshellScavenger]
        # TODO: make this dynamic, or a ref table
        SummonRandomDeathrattle(self, fourCostMinions)
        self.tribe = "Mech"


class PrimalfinLookout(Minion):

    def __init__(self, player=None, attack=3, health=2, name="Primalfin Lookout"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=3)
        self.tribe = "Murloc"


class Toxfin(Minion):

    def __init__(self, player=None, attack=1, health=2, name="Toxfin"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=1)
        self.tribe = "Murloc"


class VirmenSensei(Minion):

    def __init__(self, player=None, attack=4, health=5, name="Virmen Sensei"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=5)


class TheBeast(Minion):

    def __init__(self, player=None, attack=9, health=7, name="The Beast"):
        super().__init__(player, name=name, attack=attack, health=health, stars=4, mana=6)
        self.tribe = "Beast"
        SummonDeathrattleOpponent(self, FinkleEinhorn)


class FinkleEinhorn(Minion):

    def __init__(self, player=None, attack=3, health=3, name="Finkle Einhorn"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=3)
        self.random_summon = False


class AnnihilanBattlemaster(Minion):

    def __init__(self, player=None, attack=3, health=1, name="Annihilan Battlemaster"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=8)
        self.tribe = "Demon"


class BrannBronzebeard(Minion):

    def __init__(self, player=None, attack=2, health=4, name="Brann Bronzebeard"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=3)


class GoldrinnTheGreatWolf(Minion):

    def __init__(self, player=None, attack=4, health=4, name="The Beast"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=8)
        self.tribe = "Beast"
        BuffDeathrattleTribe(self, buff_attack=4, buff_health=4, buff_count="all", tribe="Beast", distinct=True)


class KingBagurgle(Minion):

    def __init__(self, player=None, attack=6, health=3, name="King Bagurgle"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=6)  # TODO: check mana
        self.tribe = "Murloc"
        BuffDeathrattleTribe(self, buff_attack=2, buff_health=2, buff_count="all", tribe="Murloc", distinct=True)


class LightfangEnforcer(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Lightfang Enforcer"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=6)


class MechanoEgg(Minion):

    def __init__(self, player=None, attack=0, health=5, name="Mechano-Egg"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=5)
        self.tribe = "Mech"
        SummonDeathrattle(self, Robosaur)


class Robosaur(Minion):

    def __init__(self, player=None, attack=8, health=8, name="Robosaur"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=8)
        self.tribe = "Mech"
        self.random_summon = False


class SatedThreshadon(Minion):

    def __init__(self, player=None, attack=5, health=7, name="Sated Threshadon"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=7)
        self.tribe = "Beast"
        SummonDeathrattle(self, Murloc, 3)


class Murloc(Minion):

    def __init__(self, player=None, attack=1, health=1, name="Murloc"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=1)
        self.tribe = "Murloc"
        self.random_summon = False


class SavannahHighmane(Minion):

    def __init__(self, player=None, attack=6, health=5, name="Savannah Highmane"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=6)
        self.tribe = "Beast"
        SummonDeathrattle(self, Hyena, 2)


class Hyena(Minion):

    def __init__(self, player=None, attack=2, health=2, name="Hyena"):
        super().__init__(player, name=name, attack=attack, health=health, stars=1, mana=2)
        self.tribe = "Beast"
        self.random_summon = False


class StrongshellScavenger(Minion):

    def __init__(self, player=None, attack=2, health=3, name="Strongshell Scavenger"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=4)


class Voidlord(Minion):

    def __init__(self, player=None, attack=3, health=9, name="Voidlord"):
        super().__init__(player, name=name, attack=attack, health=health, stars=5, mana=9)
        self.tribe = "Demon"
        SummonDeathrattle(self, Voidwalker, 3)


class FoeReaper4000(Minion):

    def __init__(self, player=None, attack=6, health=9, name="Foe Reaper 4000"):
        super().__init__(player, name=name, attack=attack, health=health, stars=6, mana=8)
        self.tribe = "Mech"
        self.swipe = True


class GentleMegasaur(Minion):

    def __init__(self, player=None, attack=5, health=4, name="Gentle Megasaur"):
        super().__init__(player, name=name, attack=attack, health=health, stars=6, mana=4)
        self.tribe = "Beast"


class Ghastcoiler(Minion):

    def __init__(self, player=None, attack=7, health=7, name="Ghastcoiler"):
        super().__init__(player, name=name, attack=attack, health=health, stars=6, mana=6)
        self.tribe = "Beast"
        deathrattleMinions = [SneedsOldShredder, Ghastcoiler, Voidlord, SavannahHighmane, SatedThreshadon, MechanoEgg,
                              KingBagurgle, GoldrinnTheGreatWolf, TheBeast, PilotedSkyGolem, TortollanShellraiser,
                              ReplicatingMenace, PilotedShredder, InfestedWolf, SpawnOfNZoth, RatPack, MountedRaptor,
                              KindlyGrandmother, KaboomBot, HarvestGolem, SelflessHero, Mecharoo]
        # TODO: make this dynamic, or a ref table
        # TODO: add Kangors
        SummonRandomDeathrattle(self, deathrattleMinions)


class SneedsOldShredder(Minion):

    def __init__(self, player=None, attack=5, health=7, name="Sneed's Old Shredder"):
        super().__init__(player, name=name, attack=attack, health=health, stars=6, mana=8)
        self.tribe = "Mech"
        legendaries = [SneedsOldShredder, FoeReaper4000, KingBagurgle, GoldrinnTheGreatWolf, BrannBronzebeard,
                       TheBeast, ShifterZerus]
        # TODO: make this dynamic (for which I need to add legendary field), or a ref table
        # TODO: add missing legendaries
        SummonRandomDeathrattle(self, legendaries)


class Maexxna(Minion):

    def __init__(self, player=None, attack=2, health=8, name="Maexxna"):
        super().__init__(player, name=name, attack=attack, health=health, stars=6, mana=6)
        self.tribe = "Beast"
        self.poisonous = True


# TODO:
#  Active stat effects: Dire Wolf Alpha, Murloc Warleader, Old Murk-Eye, Phalanx Commander, Siegebreaker, Mal'Ganis
#  On-death effects: Scavenging Hyena, Soul Juggler, Baron Rivendare (sortof), Ironhide Direhorn, Junkbot
#  On-summon effects: Cobalt Guardian, Khadgar, Pack Leader, Mama Bear
#  On-damage effects: Imp Gang Boss, Bolvar Fireblood (sortof), Security Rover
#  On-attack effects: Festoroot Hulk, The Boogeymonster (also on-death..)
#  Other: Kangor's Apprentice, Zapp Slywick


if __name__ == "__main__":
    from scripts.player import Player
    player_test = Player(minion=MountedRaptor())
    player_test.minions[0].trigger_deathrattles()
