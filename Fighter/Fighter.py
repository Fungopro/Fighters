import functools
import random
from random import randrange

from Armor.Armor import Armor
from State.Cold import Cold
from State.Fire import Fire
from Weapon.LongBow.Bow import LongBow
from Weapon.Swords.Sword import Sword

# Получить оружие с макс уроном с противника(метод)
# Вместо оружия появляется массив оружия
# У врага при смерти забираем самое мощное оружие
# Состояние у персонажей
# Реализовать состояния в качестве массива, в начале каждого хода они будут обрабатываться отдельным методом(холод, огонь, кислота)
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
        for i in range(0, random.randint(0, 2)):
            ran = random.randint(0, 4)
            print(ran)
            effect = ['Fire'] if ran == 1 else ['Cold'] if ran == 2 else [] if ran == 3 else ['Fire', 'Cold']
            sword = Sword('hell sword', random.randint(10, 15), effect)
            bow = LongBow('jungle bow', random.randint(15, 18), random.randint(70, 90) / 100., effect)
            if sword >= bow:
                print(self.name, ' get hell sword: ', sword)
                arr.append(sword)
            else:
                print(self.name, 'get jungle bow: ', bow)
                arr.append(bow)
        return arr

    def get_armor(self):
        ran = random.randint(0, 4)
        print(ran)
        effect = ['Fire'] if ran == 1 else ['Cold'] if ran == 2 else [] if ran == 3 else ['Fire', 'Cold']
        armor = Armor(random.randint(50, 100), effect)
        return armor

    def get_best_weapon_dmg(self):
        self.weapon = sorted(self.weapon, reverse=True)
        print('WEAPON: ', self.name, [str(i) for i in self.weapon])
        if len(self.weapon) > 0:
            return self.weapon[0].dmg_deal()
        else:
            return [5, []]

    def get_effect(self):
        arr = []
        for item in self.state:
            if item.durability < 0:
                self.state.remove(item)
            else:
                arr.append(item.get_state())
        return arr

    def attack(self, f2, arr_f):
        effect = self.get_effect()
        fire = sum([i if i > 1 else 0 for i in effect])
        if fire > 0:
            self.hp -= fire
            print(self.name, 'горит в адском пламени, получая ', fire, 'урона')

        if f2.hp <= 0:
            arr_f.remove(f2)
            del f2
        else:
            cold = True in effect
            if cold:
                print(self.name, 'Замерз, ему нужно твое тепло')
            else:
                f2.get_dmg(self.get_best_weapon_dmg(), arr_f)
                if f2.hp < 0:
                    print(self.name, ' Убил ', f2.name)
                    if len(f2.weapon) > 0:
                        self.weapon.append(f2.weapon[0])

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
        print(dmg[0])
        damage = dmg[0]
        if self.armor.get_hp() > 0:
            self.armor.get_dmg(damage)
            if self.armor.get_hp() < 0:
                self.hp = self.hp - abs(self.armor.get_hp())
                print('Броня сломана у ', self.name)
        else:
            self.hp = self.hp - dmg[0]
        print(self.name, f'Осталось: {self.hp} хп и {self.armor.get_hp()} брони')
        eff = dmg[1]
        if len(eff) > 0 and len(self.armor.atr) > 0:
            for item in eff:
                if str(item) in self.armor.atr and random.randint(0, 100) < 80:
                    eff.remove(item)
                    print('Заблокирован эффект ', str(item))
        if len(eff) > 0:
            print(f' На {self.name} были повешены эффекты {[str(i) for i in eff]}')
        self.state = self.state + eff
        if self.hp <= 0:
            arr_f.remove(self)
            self.__del__()

    def get_info(self):
        print(self.name, self.hp)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self

