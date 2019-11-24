import random


class Round:

    def __init__(self, players):
        self.players = players
        self.current_player = 0
        self.result = -1
        self.set_players_as_opponents()

    def set_players_as_opponents(self):
        self.players[0].set_opponent(self.players[1])
        self.players[1].set_opponent(self.players[0])

    def select_first_player(self):
        # Select first player based on minion count
        if len(self.players[0].minions) > len(self.players[1].minions):
            self.current_player = 0
        elif len(self.players[0].minions) < len(self.players[1].minions):
            self.current_player = 1
        else:
            if random.random() < 0.5:
                self.current_player = 0
            else:
                self.current_player = 1

    def find_result(self):
        if self.players[0].check_alive():
            # print("Player 1 has won!")
            self.result = 0
        elif self.players[1].check_alive():
            # print("Player 2 has won!")
            self.result = 1
        else:
            # print("It was a draw!")
            self.result = 2
        return self.result

    def run(self):

        # TODO: Copy players to allow for easy reruns. Need to investigate deep copies of objects

        self.select_first_player()

        while self.players[0].check_alive() and self.players[1].check_alive():
            self.players[self.current_player].do_attack()
            self.current_player = 1 - self.current_player

        return self.find_result()


if __name__ == "__main__":
    from scripts.player import Player
    from scripts.minion import Minion

    player1 = Player()
    player1.add_minion(Minion(player1, 2, 4))
    player1.add_minion(Minion(player1, 3, 5))

    player2 = Player()
    player2.add_minion(Minion(player2, 3, 9))

    round = Round([player1, player2])
    print(round.run())
