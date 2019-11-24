import unittest
from scripts.minion import Minion
from scripts.player import Player
from scripts.round import Round


class TestRounds(unittest.TestCase):

    def test_set_players_as_opponents(self):
        player1 = Player(minion=Minion())
        player2 = Player(minion=Minion())
        Round([player1, player2])
        self.assertEqual(player1.opponent, player2)
        self.assertEqual(player2.opponent, player1)

    def test_select_first_player_based_on_minion_count(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        player2 = Player(minions=[Minion() for __i in range(2)])
        round = Round([player1, player2])
        round.select_first_player()
        self.assertEqual(round.current_player, 0)

    def test_select_first_player_based_on_minion_count_alternative(self):
        player1 = Player(minions=[Minion() for __i in range(2)])
        player2 = Player(minions=[Minion() for __i in range(3)])
        round = Round([player1, player2])
        round.select_first_player()
        self.assertEqual(round.current_player, 1)

    def test_select_first_player_equal_minion_count(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        player2 = Player(minions=[Minion() for __i in range(3)])
        round = Round([player1, player2])
        round.select_first_player()
        self.assertIn(round.current_player, [0, 1])

    def test_result_one_player_dead(self):
        player1 = Player(minion=Minion())
        player2 = Player(minion=Minion())
        round = Round([player1, player2])
        player1.set_dead(player1.minions[0])
        self.assertEqual(round.find_result(), 1)

    def test_result_one_player_dead_alternative(self):
        player1 = Player(minion=Minion())
        player2 = Player(minion=Minion())
        round = Round([player1, player2])
        player2.set_dead(player2.minions[0])
        self.assertEqual(round.find_result(), 0)

    def test_result_both_players_dead(self):
        player1 = Player(minion=Minion())
        player2 = Player(minion=Minion())
        round = Round([player1, player2])
        player1.set_dead(player1.minions[0])
        player2.set_dead(player2.minions[0])
        self.assertEqual(round.find_result(), 2)

    def test_run_gives_winner(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        player2 = Player(minions=[Minion() for __i in range(2)])
        round = Round([player1, player2])

        self.assertEqual(round.run(), 0)

    def test_run_gives_winner_alternative(self):
        player1 = Player(minions=[Minion() for __i in range(2)])
        player2 = Player(minions=[Minion() for __i in range(3)])
        round = Round([player1, player2])

        self.assertEqual(round.run(), 1)

    def test_run_gives_draw(self):
        player1 = Player(minions=[Minion() for __i in range(3)])
        player2 = Player(minions=[Minion() for __i in range(3)])
        round = Round([player1, player2])

        self.assertEqual(round.run(), 2)


if __name__ == '__main__':
    unittest.main()
