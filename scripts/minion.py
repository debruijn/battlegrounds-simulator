
class Minion:

    def __init__(self, player, attack=1, health=1):
        self.attack = attack
        self.health = health
        self.player = player

    def find_target(self):
        return self.player.get_opponent().get_defender()  # TODO: make it randomly generate 1

    def do_attack(self, minion):
        self.health -= minion.attack
        minion.health -= self.attack
        print(f'This minion has {self.health} health remaining. Opponent has {minion.health} health remaining.')

    def combat(self):
        target = self.find_target()
        self.do_attack(target)


if __name__ == "__main__":
    m1 = Minion(4, 3)
    m2 = Minion(1, 5)
    m1.do_attack(m2)
