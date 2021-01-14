import random
from random import randrange

from Weapon.LongBow.Bow import LongBow
from Weapon.Swords.Sword import Sword


class Fighter:
    def __init__(self, n, h=100):
        self.hp = h
        self.name = n
        self.weapon = self.get_weapon()

    def get_weapon(self):
        sword = Sword('hell sword', random.randint(20, 26))
        bow = LongBow('jungle bow', random.randint(15, 26), random.randint(70, 90)/100.)
        if sword >= bow:
            print(self.name, ' get hell sword')
            return sword
        else:
            print(self.name, 'jungle bow')
            return bow

    def attack(self, f2):
        print(self.name, '->', f2.name)
        f2.get_dmg(self.weapon.dmg_deal())

    def __str__(self):
        return self.name

    def random_attack(self, arr_f):
        if self in arr_f:
            arr_f.remove(self)
        for item in arr_f:
            if item is None:
                arr_f.remove(item)
        self.attack(arr_f[randrange(len(arr_f))])
        arr_f.append(self)
        return arr_f

    def get_dmg(self, dmg):
            self.hp = self.hp - dmg
            print(self.name, f'Осталось: {self.hp} хп')

    def get_info(self):
        print(self.name, self.hp, self.weapon.dmg_deal())

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self
