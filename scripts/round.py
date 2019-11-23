import random


class Round:

    def __init__(self, players):
        self.players = players

    def run(self):

        # TODO: Copy players to allow for easy reruns. Need to investigate deep copies of objects

        # Select first player based
        if len(self.players[0].minions) > len(self.players[1].minions):
            current_player = 0
        elif len(self.players[0].minions) < len(self.players[1].minions):
            current_player = 1
        else:
            if random.random() < 0.5:
                current_player = 0
            else:
                current_player = 1

        while self.players[0].check_alive() and self.players[1].check_alive():
            self.players[current_player].do_attack()
            current_player = 1 - current_player

        if self.players[0].check_alive():
            # print("Player 1 has won!")
            result = 0
        elif self.players[1].check_alive():
            # print("Player 2 has won!")
            result = 1
        else:
            # print("It was a draw!")
            result = 2

        return result


if __name__ == "__main__":
    from scripts.player import Player
    from scripts.minion import Minion

    player1 = Player()
    player1.add_minion(Minion(player1, 2, 4))
    player1.add_minion(Minion(player1, 3, 5))

    player2 = Player()
    player2.add_minion(Minion(player2, 3, 9))

    player1.set_opponent(player2)
    player2.set_opponent(player1)

    round = Round([player1, player2])
    print(round.run())
