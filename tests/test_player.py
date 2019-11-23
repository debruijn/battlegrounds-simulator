import unittest
from scripts.minion import Minion
from scripts.player import Player


class MyTestCase(unittest.TestCase):

    def test_add_first_minion_automatic(self):
        player1 = Player()
        m1 = Minion(player1)
        self.assertEqual(player1.minions[0], m1)

    def test_add_first_minion_manual(self):
        player1 = Player()
        m1 = Minion()
        player1.add_minion(m1)
        self.assertEqual(player1.minions[0], m1)

    def test_add_more_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(4)]
        self.assertListEqual(player1.minions, minions)

    def test_add_too_many_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(8)]
        self.assertEqual(len(player1.minions), 7)
        self.assertListEqual(player1.minions, minions[0:7])

    def test_dead_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(4)]
        player1.set_dead(minions[0])
        player1.set_dead(minions[1])
        self.assertListEqual(player1.minions, minions[2:4])
        self.assertListEqual(player1.dead_minions, minions[0:2])

    def test_dead_player(self):
        player1 = Player()
        m1 = Minion(player1)
        player1.set_dead(m1)
        self.assertEqual(player1.dead_minions[0], m1)
        self.assertFalse(player1.check_alive())

    def test_error_set_other_players_minion_dead(self):
        player1 = Player()
        player2 = Player()
        m1 = Minion(player1)
        with self.assertRaisesRegex(ValueError, "is not in list"):
            player2.set_dead(m1)

    def test_get_defender(self):
        1 + 1

    def test_get_defender_swipe(self):
        1 + 1

    def test_get_defender_swipe_side(self):
        1 + 1

    def test_get_defender_swipe_single_minion(self):
        1 + 1

    def test_get_attacker(self):
        1 + 1

    def test_next_attacker(self):
        1 + 1

    def test_next_attacker_loop_around(self):
        1 + 1

    def test_dead_minion_next_attacker(self):
        1 + 1

    def test_dead_minion_before_next_attacker(self):
        1 + 1

    def test_dead_minion_after_next_attacker(self):
        1 + 1



if __name__ == '__main__':
    unittest.main()
