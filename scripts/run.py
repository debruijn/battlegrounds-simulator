from scripts.player import Player
from scripts.minion import Minion
from scripts.round import Round


class Run:

    def __init__(self, R=1):
        self.R = R
        self.results = [0, 0, 0]

    def setup(self):
        player1 = Player()
        player1.add_minion(Minion(player1, 5, 2, "Minion 1.1"))
        player1.add_minion(Minion(player1, 3, 5, "Minion 1.2"))
        player1.add_minion(Minion(player1, 1, 15, "Minion 1.3"))
        player1.add_minion(Minion(player1, 2, 10, "Minion 1.4"))
        player1.add_minion(Minion(player1, 2, 3, "Minion 1.5"))

        player2 = Player()
        player2.add_minion(Minion(player2, 1, 12, "Minion 2.1"))
        player2.add_minion(Minion(player2, 2, 11, "Minion 2.2"))
        player2.add_minion(Minion(player2, 1, 15, "Minion 2.3"))
        player2.add_minion(Minion(player2, 1, 15, "Minion 2.4"))

        player1.set_opponent(player2)
        player2.set_opponent(player1)
        return [player1, player2]

    def run(self):

        for r in range(self.R):
            players = self.setup()
            round = Round(players)
            self.results[round.run()] += 1

    def print_results(self):
        print(self.results)


if __name__ == "__main__":
    run = Run(R=10000)
    run.run()
    run.print_results()
