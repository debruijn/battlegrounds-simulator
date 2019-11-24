import unittest
from scripts.minion import Minion
from scripts.player import Player


class TestMinions(unittest.TestCase):

    def test_attack(self):
        m1 = Minion(attack=4, health=3)
        m2 = Minion(attack=1, health=5)

        m1.do_attack(m2)
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 1)

    def test_repeated_attack(self):
        m1 = Minion(attack=4, health=3)
        m2 = Minion(attack=1, health=9)

        m1.do_attack(m2)
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 5)

        m2.do_attack(m1)
        self.assertEqual(m1.health, 1)
        self.assertEqual(m2.health, 1)

    def test_death(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1, attack=4, health=3)
        m2 = Minion(player2, attack=1, health=5)

        m1.do_attack(m2)
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 1)

        self.assertFalse(m1.dead)
        self.assertFalse(m2.dead)

        m2.do_attack(m1)
        self.assertEqual(m1.health, 1)
        self.assertEqual(m2.health, -3)

        self.assertFalse(m1.dead)
        self.assertTrue(m2.dead)

    def test_swipe_middle(self):
        player1 = Player()
        player2 = Player()

        defender1 = Minion(player2, attack=1, health=2)
        defender2 = Minion(player2, attack=0, health=3)
        defender3 = Minion(player2, attack=0, health=4)

        defenders = [defender1, defender2, defender3]
        attacker = Minion(player1, attack=1, health=2)

        attacker.do_attack(defenders)
        self.assertEqual(defender1.health, 1)
        self.assertEqual(defender2.health, 2)
        self.assertEqual(defender3.health, 3)
        self.assertEqual(attacker.health, 1)

    def test_swipe_side(self):
        player1 = Player()
        player2 = Player()

        defender1 = Minion(player2, attack=1, health=2)
        defender2 = Minion(player2, attack=0, health=3)

        defenders = [defender1, defender2]
        attacker = Minion(player1, attack=1, health=2)

        attacker.do_attack(defenders)
        self.assertEqual(defender1.health, 1)
        self.assertEqual(defender2.health, 2)
        self.assertEqual(attacker.health, 1)

    def test_divine_shield(self):
        m1 = Minion(attack=4, health=3)
        m2 = Minion(attack=1, health=5)

        m1.divine_shield = True
        m1.do_attack(m2)
        self.assertEqual(m1.health, 3)
        self.assertEqual(m2.health, 1)
        self.assertFalse(m1.divine_shield)

        m2.divine_shield = True
        m1.do_attack(m2)
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 1)
        self.assertFalse(m2.divine_shield)

    def test_poisonous(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1, attack=4, health=3)
        m2 = Minion(player2, attack=1, health=5)

        m1.poisonous = True
        m1.do_attack(m2)
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 0)
        self.assertTrue(m2.dead)

        m3 = Minion(player2, attack=1, health=1)
        m1.do_attack(m3)
        self.assertEqual(m1.health, 1)
        self.assertEqual(m3.health, -3)
        self.assertTrue(m3.dead)

    def test_get_target(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1)
        m2 = Minion(player2)
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        self.assertEqual(m1.find_target(), m2)

    def test_get_single_target_with_swipe(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1)
        m2 = Minion(player2)
        player1.set_opponent(player2)
        player2.set_opponent(player1)
        m1.swipe = True

        self.assertEqual(m1.find_target(), m2)

    # def test_get_target_swipe(self):  TODO: add this back when taunt works
    #     player1 = Player()
    #     player2 = Player()
    #     player1.set_opponent(player2)
    #     player2.set_opponent(player1)
    #
    #     defender1 = Minion(player2, attack=1, health=2)
    #     defender2 = Minion(player2, attack=0, health=3)
    #     defender2.taunt = True
    #     defender3 = Minion(player2, attack=0, health=4)
    #
    #     defenders = [defender2, defender1, defender3]
    #     attacker = Minion(player1, attack=1, health=2)
    #     attacker.swipe = True
    #
    #     self.assertListEqual(attacker.find_target(), defenders)

    # def test_get_target_side_swipe_due_to_taunt(self):  TODO: add this back when taunt works
    #     player1 = Player()
    #     player2 = Player()
    #     player1.set_opponent(player2)
    #     player2.set_opponent(player1)
    #
    #     defender1 = Minion(player2, attack=1, health=2)
    #     defender1.taunt = True
    #     defender2 = Minion(player2, attack=0, health=3)
    #     defender3 = Minion(player2, attack=0, health=4)
    #
    #     defenders = [defender1, defender2]
    #     attacker = Minion(player1, attack=1, health=2)
    #     attacker.swipe = True
    #
    #     self.assertListEqual(attacker.find_target(), defenders)

    def test_windfury(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1, attack=2, health=3)
        m2 = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        m1.windfury = True
        m1.do_combat()
        self.assertEqual(m1.health, 1)
        self.assertEqual(m2.health, 1)

    def test_windfury_divineshield_attacker(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1, attack=2, health=3)
        m2 = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        m1.windfury = True
        m1.divine_shield = True
        m1.do_combat()
        self.assertEqual(m1.health, 2)
        self.assertEqual(m2.health, 1)

    def test_windfury_divineshield_defender(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1, attack=2, health=3)
        m2 = Minion(player2, attack=1, health=5)
        player1.set_opponent(player2)
        player2.set_opponent(player1)

        m1.windfury = True
        m2.divine_shield = True
        m1.do_combat()
        self.assertEqual(m1.health, 1)
        self.assertEqual(m2.health, 3)


if __name__ == '__main__':
    unittest.main()
