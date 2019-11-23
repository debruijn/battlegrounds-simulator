from scripts.player import Player
from scripts.minion import Minion


if __name__ == "__main__":

    R = 10000
    win1 = 0
    win2 = 0
    draw = 0
    for r in range(R):

        player1 = Player()
        player1.add_minion(Minion(player1, 2, 3, "Minion 1.1"))
        player1.add_minion(Minion(player1, 3, 5, "Minion 1.2"))
        player1.add_minion(Minion(player1, 1, 15, "Minion 1.3"))
        player1.add_minion(Minion(player1, 2, 10, "Minion 1.4"))
        player1.add_minion(Minion(player1, 5, 2, "Minion 1.5"))

        player2 = Player()
        player2.add_minion(Minion(player2, 1, 12, "Minion 2.1"))
        player2.add_minion(Minion(player2, 2, 11, "Minion 2.2"))
        player2.add_minion(Minion(player2, 1, 15, "Minion 2.3"))
        player2.add_minion(Minion(player2, 1, 6, "Minion 2.4"))

        player1.set_opponent(player2)
        player2.set_opponent(player1)

        while player1.check_alive() and player2.check_alive():
            if player1.check_alive() and player2.check_alive():
                player1.do_attack()
            if player1.check_alive() and player2.check_alive():
                player2.do_attack()

        if player1.check_alive():
            #print("Player 1 has won!")
            win1 += 1
        elif player2.check_alive():
            #print("Player 2 has won!")
            win2 += 1
        else:
            #print("It was a draw!")
            draw += 1
    print(f"Results: {win1}; {win2}; {draw}")
