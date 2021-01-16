

class Weapon:
    def __init__(self, n, dmg, e):
        self.name = n
        self.dmg = dmg
        self.effect = e

    def get_dmg(self):
        raise Exception(' Метод нереализован')

    def dmg_deal(self):
        raise Exception(' Метод нереализован')

    def get_effect(self):
        raise Exception(' Метод нереализован')

    def __le__(self, other):
        return self.get_dmg() <= other.get_dmg()

    def __lt__(self, other):
        return self.get_dmg() < other.get_dmg()
