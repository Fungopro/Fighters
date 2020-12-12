from random import randrange


class Fighter:
    def __init__(self, n, h=100, d=20):
        self.hp = h
        self.dmg = d
        self.name = n

    def attack(self, f2, arr_f):
        if f2.hp <= 0:
            arr_f.remove(f2)
            f2.__del__()
            self.random_attack(arr_f)
        else:
            print(self.name, 'Attack', f2.name)
            f2.get_dmg(self.dmg, arr_f)

    def __str__(self):
        return self.name

    def random_attack(self, arr_f):
        if len(arr_f) == 1:
            print(arr_f)
            print(f'win {self.name}')
            self.get_info()
            exit()
        arr_f.remove(self)
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
        print(self.name, self.hp, self.dmg)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fighters = [Fighter('guard_' + str(i)) for i in range(1, 4)]
    print(len(fighters))
    while len(fighters) > 1:
        fighters = fighters[randrange(1, 3)].random_attack(fighters)
    for item in fighters:
        item.get_info()

