import random

from Weapon.Weapon import Weapon


class LongBow(Weapon):
    def __init__(self, n, dmg, chance):
        super().__init__(n, dmg)
        self.chance = chance

    def dmg_deal(self):
        chnc = random.randint(0, 100)/100
        if chnc < self.chance:
            return self.dmg_deal()
        else:
            print('Промах!')
            return 0

    def get_dmg(self):
        return self.chance*self.dmg

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __str__(self):
        return self.name + '   ' + str(self.dmg) + '    ' + str(self.chance)
