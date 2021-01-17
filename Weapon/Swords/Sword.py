import random

from State.Cold import Cold
from State.Fire import Fire
from Weapon.Weapon import Weapon


class Sword(Weapon):
    def __init__(self, n, dmg, e):
        super().__init__(n, dmg, e)
        self.hp = 1.

    def get_dmg(self):
        print(self.dmg, self.hp)
        return self.dmg * self.hp if self.hp > 0 else 0

    def dmg_deal(self):
        if random.randint(0, 100) > 50 and self.hp > 0:
            self.hp -= .1
            return [self.get_dmg(), self.get_effect()]
        elif self.hp > 0:
            return [self.get_dmg(), self.get_effect()]
        else:
            return [5, []]

    def get_effect(self):
        arr = []
        for item in self.effect:
            if random.randint(0, 100) < 80:
                if item == 'Fire':
                    arr.append(Cold(2))
                else:
                    arr.append(Fire(10, 5))
        return arr

    def __str__(self):
        return self.name + '   ' + str(self.dmg) + '    ' + str(self.hp) + '    ' + str([str(i) for i in self.effect])

