import unittest
from scripts.minion import Minion
from scripts.player import Player
from scripts.deathrattle import Deathrattle, SummonDeathrattle, DamageDeathrattle, DivineShieldDeathrattle, \
    BuffDeathrattle


class TestDeathrattles(unittest.TestCase):

    def test_damage_deathrattle_manually_deathrattle(self):
        player1 = Player()
        player2 = Player()
        minion = Minion(player1, attack=4, health=3)
        DamageDeathrattle(minion, damage=2)
        defender = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)

        minion.deathrattle[0].trigger()
        self.assertEqual(defender.health, 3)

    def test_damage_deathrattle_manually_minion(self):
        player1 = Player()
        player2 = Player()
        minion = Minion(player1, attack=4, health=3)
        DamageDeathrattle(minion, damage=2)
        defender = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)

        minion.trigger_deathrattles()
        self.assertEqual(defender.health, 3)

    def test_damage_deathrattle_with_combat(self):
        player1 = Player()
        player2 = Player()
        minion = Minion(player1, attack=4, health=3)
        DamageDeathrattle(minion, damage=2)
        defender = Minion(player2, attack=3, health=7)
        player1.set_opponent(player2)

        minion.do_attack(defender)
        self.assertEqual(defender.health, 1)

    def test_damage_deathrattle_triggers_deathrattle(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        DamageDeathrattle(minion1, damage=2)

        defender = Minion(player2, attack=3, health=6)
        DamageDeathrattle(defender, damage=2)

        minion1.do_attack(defender)
        self.assertEqual(minion2.health, 1)

    def test_damage_deathrattle_for_both_by_combat(self):
        pass  # Todo: implement after implementing a deathrattle phase

    def test_multiple_damage_deathrattles(self):
        player1 = Player()
        player2 = Player()
        minion = Minion(player1, attack=4, health=3)
        DamageDeathrattle(minion, damage=2)
        DamageDeathrattle(minion, damage=3)
        defender = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)

        minion.trigger_deathrattles()
        self.assertEqual(defender.health, 0)

    def test_summon_deathrattle_one_minion(self):
        player1 = Player()
        minion = Minion(player1)
        SummonDeathrattle(minion)

        minion.trigger_deathrattles()
        self.assertEqual(len(player1.minions), 2)

    def test_summon_deathrattle_multiple_minions(self):
        player1 = Player()
        minion = Minion(player1)
        SummonDeathrattle(minion, summon_count=3)

        minion.trigger_deathrattles()
        self.assertEqual(len(player1.minions), 4)

    def test_summon_deathrattle_one_minion_multiple_types(self):
        pass  # TODO: implement after having more minion types

    def test_summon_deathrattle_multiple_minions_multiple_types(self):
        pass  # TODO: implement after having more minion types

    def test_summon_deathrattle_too_many_minions(self):
        player1 = Player()
        minion = Minion(player1)
        SummonDeathrattle(minion, summon_count=8)

        minion.trigger_deathrattles()
        self.assertEqual(len(player1.minions), 7)
        self.assertIn(minion, player1.minions)

    def test_summon_deathrattle_too_many_minions_by_combat(self):
        player1 = Player()
        player2 = Player()
        minion = Minion(player1, attack=4, health=3)
        SummonDeathrattle(minion, summon_count=8)
        defender = Minion(player2, attack=3, health=7)
        player1.set_opponent(player2)

        minion.do_attack(defender)

        self.assertEqual(len(player1.minions), 7)
        self.assertNotIn(minion, player1.minions)

    def test_multiple_summon_deathrattles(self):
        player1 = Player()
        minion = Minion(player1)
        SummonDeathrattle(minion)
        SummonDeathrattle(minion, summon_count=2)

        minion.trigger_deathrattles()
        self.assertEqual(len(player1.minions), 4)

    def test_divineshield_deathrattle(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        DivineShieldDeathrattle(minion1)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertTrue(minion2.divine_shield)

    def test_divineshield_deathrattle_empty_board(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion = Minion(player1, attack=4, health=3)
        DivineShieldDeathrattle(minion)

        defender = Minion(player2, attack=3, health=6)

        minion.do_attack(defender)
        self.assertFalse(defender.divine_shield)

    def test_buff_deathrattle_one_minion(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack, 5)
        self.assertEqual(minion2.health, 4)

    def test_buff_deathrattle_more_minions_distinct(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count=2)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack, 5)
        self.assertEqual(minion2.health, 4)
        self.assertEqual(minion3.attack, 5)
        self.assertEqual(minion3.health, 4)

    def test_buff_deathrattle_more_minions_not_distinct(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count=2, distinct=False)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack + minion3.attack, 4 + 4 + 2)
        self.assertEqual(minion2.health + minion3.health, 3 + 3 + 2)

    def test_buff_deathrattle_more_minions_than_buffs_distinct(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        minion4 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count=2)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack + minion3.attack + minion4.attack, 5+5+4)
        self.assertEqual(minion2.health + minion3.health + minion4.health, 4+4+3)

    def test_buff_deathrattle_more_minions_nondistinct_more_buffs_than_minions(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count=4, distinct=False)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack + minion3.attack, 4 + 4 + 4)
        self.assertEqual(minion2.health + minion3.health, 3 + 3 + 4)

    def test_buff_deathrattle_boardwide(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        minion4 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count="all")

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack + minion3.attack + minion4.attack, 5+5+5)
        self.assertEqual(minion2.health + minion3.health + minion4.health, 4+4+4)

    def test_multiple_buff_deathrattles(self):
        player1 = Player()
        player2 = Player()
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        minion1 = Minion(player1, attack=4, health=3)
        minion2 = Minion(player1, attack=4, health=3)
        minion3 = Minion(player1, attack=4, health=3)
        BuffDeathrattle(minion1, buff_count=1)
        BuffDeathrattle(minion1, buff_count=2)

        defender = Minion(player2, attack=3, health=6)

        minion1.do_attack(defender)
        self.assertEqual(minion2.attack + minion3.attack, 4 + 4 + 3)
        self.assertEqual(minion2.health + minion3.health, 3 + 3 + 3)

    def test_combination_summon_buff_deathrattle(self):
        pass  # TODO: depends on order?


if __name__ == '__main__':
    unittest.main()
