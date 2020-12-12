from random import randrange


class Fighter:
    def __init__(self, n):
        self.hp = 100
        self.dmg = 20
        self.name = n

    def attack(self, f2):
        print(self.name, 'Attack', f2.name)
        f2.get_dmg(self.dmg)

    def random_attack(self, arr_f):
        arr_f.remove(self)
        self.attack(arr_f[randrange(len(arr_f))])
        arr_f.append(self)

    def get_dmg(self, dmg):
        if self.hp <= 0:
            print(self.name, 'Умер')
        else:
            self.hp = self.hp - dmg
            print(self.name, f'Осталось: {self.hp} хп')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fighters = [Fighter('guard_' + str(i)) for i in range(1, 4)]
    for i in range(1, 10):
        for item in fighters:
            item.random_attack(fighters)

