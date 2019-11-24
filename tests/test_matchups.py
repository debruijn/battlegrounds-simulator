import unittest
from scripts.minion import Minion
from scripts.player import Player
from scripts.round import Round
from scripts.minion_catalogue import InfestedWolf, Annoyotron


class TestMatchups(unittest.TestCase):

    def test_one_annoyotrons_vs_infested_wolf(self):
        player1 = Player(minion=InfestedWolf())
        player2 = Player(minions=[Annoyotron() for __i in range(1)])
        round = Round([player1, player2])
        self.assertEqual(round.run(), 0)

    def test_two_annoyotrons_vs_infested_wolf(self):
        player1 = Player(minion=InfestedWolf())
        player2 = Player(minions=[Annoyotron() for __i in range(2)])
        round = Round([player1, player2])
        self.assertEqual(round.run(), 2)

    def test_three_annoyotrons_vs_infested_wolf(self):
        player1 = Player(minion=InfestedWolf())
        player2 = Player(minions=[Annoyotron() for __i in range(3)])
        round = Round([player1, player2])
        self.assertEqual(round.run(), 1)


if __name__ == '__main__':
    unittest.main()
