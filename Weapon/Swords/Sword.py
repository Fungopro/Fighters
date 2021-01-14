import random

from Weapon.Weapon import Weapon


class Sword(Weapon):
    def __init__(self, n, dmg):
        super().__init__(n, dmg)
        self.hp = 1.

    def get_dmg(self):
        print(self.dmg, self.hp)
        return self.dmg * self.hp if self.hp > 0 else 0

    def dmg_deal(self):
        if random.randint(0, 100) > 50 and self.hp > 0:
            self.hp -= .1
            return self.get_dmg()
        elif self.hp > 0:
            return self.get_dmg()
        else:
            return 5

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __str__(self):
        return self.name + '   ' + str(self.dmg) + '    ' + str(self.hp)