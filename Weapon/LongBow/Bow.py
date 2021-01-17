import random

from State.Cold import Cold
from State.Fire import Fire
from Weapon.Weapon import Weapon


class LongBow(Weapon):
    def __init__(self, n, dmg, chance, e):
        super().__init__(n, dmg, e)
        self.chance = chance

    def dmg_deal(self):
        chnc = random.randint(0, 100)/100
        if chnc < self.chance:
            return [self.get_dmg(), self.get_effect()]
        else:
            print('Промах!')
            return [0, self.get_effect()]

    def get_dmg(self):
        return self.chance*self.dmg

    def get_effect(self):
        arr = []
        for item in self.effect:
            if random.randint(0, 100) < 90:
                if item == 'Fire':
                    arr.append(Cold(2))
                else:
                    arr.append(Fire(2, 5))
        return arr

    def __str__(self):
        return self.name + '   ' + str(self.dmg) + '    ' + str(self.chance) + ' ' + str(self.effect)
