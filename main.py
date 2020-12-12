from random import randrange


class Fighter:
    def __init__(self, n, h=100, d=20):
        self.hp = h
        self.dmg = d
        self.name = n

    def attack(self, f2, arr_f):
        print(self.name, 'Attack', f2.name)
        if f2.hp <= 0:
            arr_f.remove(f2)
            f2.__del__()
            self.random_attack(arr_f)
        else:
            f2.get_dmg(self.dmg)

    def random_attack(self, arr_f):
        if len(arr_f) == 1:
            print(f'win {self.name}')
            self.get_info()
            exit()
        arr_f.remove(self)
        self.attack(arr_f[randrange(len(arr_f))], arr_f)
        arr_f.append(self)

    def get_dmg(self, dmg):
        if self.hp <= 0:
            print(self.name, 'Умер')
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
    for i in range(1, 15):
        for item in fighters:
            item.random_attack(fighters)

