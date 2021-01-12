from random import randrange


class Fighter:
    def __init__(self, n, h=100, d=20):
        self.hp = h
        self.dmg = d
        self.name = n

    def attack(self, f2, arr_f):
        if f2.hp <= 0:
            arr_f.remove(f2)
            del f2
            self.random_attack(arr_f)
        else:
            print(self.name, '->', f2.name)
            f2.get_dmg(self.dmg)

    def __str__(self):
        return self.name

    def random_attack(self, arr_f):
        if self in arr_f:
            arr_f.remove(self)
        for item in arr_f:
            if item is None:
                arr_f.remove(item)
        if len(arr_f) > 0:
            self.attack(arr_f[randrange(len(arr_f))], arr_f)
        arr_f.append(self)
        return arr_f

    def get_dmg(self, dmg):
        self.hp = self.hp - dmg
        print(self.name, f'Осталось: {self.hp} хп')

    def get_info(self):
        print(self.name, self.hp, self.dmg)

    def __del__(self):
        print(f"Valhalla, {self.name} is coming")
        del self


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fighter1 = Fighter('guard_1')
    fighter2 = Fighter('guard_2')
    fighter3 = Fighter('guard_3')
    arr = [fighter1, fighter2, fighter3]
    while True:
        if 'fighter1' in locals() and len(arr) > 1:
            fighter1.random_attack(arr)
            if fighter1.hp == 0:
                arr.remove(fighter1)
                del fighter1
        if 'fighter2' in locals() and len(arr) > 1:
            fighter2.random_attack(arr)
            if fighter2.hp == 0:
                arr.remove(fighter2)
                del fighter2
        if 'fighter3' in locals() and len(arr) > 1:
            fighter3.random_attack(arr)
            if fighter3.hp == 0:
                arr.remove(fighter3)
                del fighter3
        for item in arr:
            if item is not None:
                item.get_info()
        if len(arr) == 1:
            print(arr[0], 'is winner!')
            break

