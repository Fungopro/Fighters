import functools
import random
from random import randrange

from Weapon.LongBow.Bow import LongBow
from Weapon.Swords.Sword import Sword

# Получить оружие с макс уроном с противника(метод)
# Вместо оружия появляется массив оружия
# У врага при смерти забираем самое мощное оружие
# Состояние у персонажей
# Реализовать состояния в качестве паттерна, в начале каждого хода они будут обрабатываться отдельным методом(холод, огонь, кислота)
# Реализовать класс батлграунд, где будет запуск и сам бой персонажей
# Добавить рукопашный бой
# Добавить броню и атрибуты для нее


class Fighter:
    def __init__(self, n, h=100):
        self.hp = h
        self.name = n
        self.weapon = self.get_weapon()
        self.armor = self.get_armor()
        self.state = []

    def get_weapon(self):
        arr = []
        for i in range(0, 2):
            sword = Sword('hell sword', random.randint(20, 30))
            bow = LongBow('jungle bow', random.randint(15, 25), random.randint(70, 90) / 100.)
            if sword >= bow:
                print(self.name, ' get hell sword: ', sword)
                arr.append(sword)
            else:
                print(self.name, 'get jungle bow: ', bow)
                arr.append(bow)
        return arr

    def get_best_weapon_dmg(self):
        self.weapon = functools.total_ordering(self.weapon)
        print('WEAPON: ', [str(i) for i in self.weapon])
        return self.weapon[0].dmg_deal()

    def attack(self, f2, arr_f):
        if f2.hp <= 0:
            arr_f.remove(f2)
            del f2
        else:
            print(self.name, '->', f2.name)
            f2.get_dmg(self.get_best_weapon_dmg(), arr_f)

    def __str__(self):
        return self.name

    def random_attack(self, arr_f):
        if self in arr_f:
            arr_f.remove(self)
        for item in arr_f:
            if item is None:
                arr_f.remove(item)
        self.attack(arr_f[randrange(len(arr_f))], arr_f)
        arr_f.append(self)
        return arr_f

    def get_dmg(self, dmg, arr_f):
        if self.hp <= 0:
            print(self.name, 'Умер')
            arr_f.remove(self)
            self.__del__()
        else:
            self.hp = self.hp - dmg
            print(self.name, f'Осталось: {self.hp} хп')

    def get_info(self):
        print(self.name, self.hp)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self

    def get_armor(self):
        pass
