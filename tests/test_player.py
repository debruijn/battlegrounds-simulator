import unittest
from scripts.minion import Minion
from scripts.player import Player


class TestPlayers(unittest.TestCase):

    def test_add_first_minion_automatic(self):
        player1 = Player()
        m1 = Minion(player1)
        self.assertEqual(player1.minions[0], m1)

    def test_add_first_minion_manual(self):
        player1 = Player()
        m1 = Minion()
        player1.add_minion(m1)
        self.assertEqual(player1.minions[0], m1)

    def test_add_minion_in_constructor(self):
        player1 = Player(minion=Minion())
        self.assertEqual(len(player1.minions), 1)

    def test_add_multiple_minions_in_constructor(self):
        player1 = Player(minions=[Minion() for __i in range(4)])
        self.assertEqual(len(player1.minions), 4)

    def test_add_more_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(4)]
        self.assertListEqual(player1.minions, minions)

    def test_add_too_many_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(8)]
        self.assertEqual(len(player1.minions), 7)
        self.assertListEqual(player1.minions, minions[0:7])

    def test_add_too_many_minions_in_constructor(self):
        player1 = Player(minions=[Minion() for __i in range(8)])
        self.assertEqual(len(player1.minions), 7)

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
        player1 = Player()
        m1 = Minion(player1)
        self.assertEqual(player1.get_defender(), m1)

    def test_taunt_minions(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(7)]
        minions[1].taunt = True
        minions[3].taunt = True
        minions[6].taunt = True
        taunt_minions = player1.get_taunt_minions()
        self.assertEqual(len(taunt_minions), 3)
        self.assertListEqual(taunt_minions, [minions[1], minions[3], minions[6]])

    def test_get_defender_with_taunt(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(7)]
        minions[1].taunt = True
        self.assertEqual(player1.get_defender(), minions[1])

    def test_get_defender_with_multiple_taunt(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(7)]
        minions[1].taunt = True
        minions[3].taunt = True
        minions[6].taunt = True
        self.assertTrue(player1.get_defender().taunt)

    def test_get_defender_swipe(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        minions[1].taunt = True
        self.assertListEqual(player1.get_defender(swipe=True), [minions[1], minions[0], minions[2]])

    def test_get_defender_swipe_side(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        minions[0].taunt = True
        self.assertListEqual(player1.get_defender(swipe=True), minions[0:2])

    def test_get_defender_swipe_side_alternative(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        minions[2].taunt = True
        self.assertListEqual(player1.get_defender(swipe=True), [minions[2], minions[1]])

    def test_get_defender_swipe_single_minion(self):
        player1 = Player()
        m1 = Minion(player1)
        self.assertEqual(player1.get_defender(swipe=True), m1)

    def test_get_attacker_one_minion(self):
        player1 = Player()
        m1 = Minion(player1)
        self.assertEqual(player1.get_attacker(), m1)

    def test_get_attacker_multiple_minions_first_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        self.assertEqual(player1.get_attacker(), minions[0])

    def test_get_attacker_multiple_minions_later_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        player1.update_attacker()
        player1.update_attacker()
        self.assertEqual(player1.get_attacker(), minions[2])

    def test_update_attacker(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        self.assertEqual(player1.next_attacker, 0)
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 1)
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 2)

    def test_update_attacker_loop_around(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        player1.update_attacker()
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 2)
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 0)
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 1)

    def test_dead_minion_as_next_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 1)
        player1.set_dead(player1.minions[1])
        self.assertEqual(player1.next_attacker, 1)
        self.assertEqual(player1.get_attacker(), minions[2])

    def test_dead_minion_after_next_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        self.assertEqual(player1.next_attacker, 0)
        player1.set_dead(player1.minions[1])
        self.assertEqual(player1.next_attacker, 0)
        self.assertEqual(player1.get_attacker(), minions[0])

    def test_dead_minion_before_next_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        player1.update_attacker()
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 2)
        player1.set_dead(player1.minions[1])
        self.assertEqual(player1.next_attacker, 1)
        self.assertEqual(player1.get_attacker(), minions[2])

    def test_dead_rightmost_minion_as_next_attacker(self):
        player1 = Player()
        minions = [Minion(player1) for __i in range(3)]
        player1.update_attacker()
        player1.update_attacker()
        self.assertEqual(player1.next_attacker, 2)
        player1.set_dead(player1.minions[2])
        self.assertEqual(player1.next_attacker, 0)
        self.assertEqual(player1.get_attacker(), minions[0])


if __name__ == '__main__':
    unittest.main()
