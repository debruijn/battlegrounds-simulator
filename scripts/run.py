from scripts.player import Player
from scripts.minion import Minion
from scripts.round import Round
from scripts.minion_catalogue import MountedRaptor, SelflessHero, Alleycat, HarvestGolem


class Run:

    def __init__(self, R=1):
        self.R = R
        self.results = [0, 0, 0]

    def setup_alt(self):
        player1 = Player()
        MountedRaptor(player1)

        player2 = Player()
        SelflessHero(player2)
        Alleycat(player2)

        return [player1, player2]

    def setup(self):
        player1 = Player()
        SelflessHero(player1)
        MountedRaptor(player1)
        MountedRaptor(player1)
        HarvestGolem(player1)

        player2 = Player()
        HarvestGolem(player2)
        HarvestGolem(player2)
        MountedRaptor(player2)
        MountedRaptor(player2)

        return [player1, player2]

    def run(self):

        for r in range(self.R):
            players = self.setup()
            round = Round(players)
            self.results[round.run()] += 1

    def print_results(self):
        print(self.results)


if __name__ == "__main__":
    run = Run(R=100000)
    run.run()
    run.print_results()
