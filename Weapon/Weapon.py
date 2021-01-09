

class Weapon:
    def __init__(self, n, dmg):
        self.name = n
        self.dmg = dmg

    def get_dmg(self):
        raise Exception(' Метод нереализован')

    def dmg_deal(self):
        raise Exception(' Метод нереализован')

    def __le__(self, other):
        return self.dmg_deal() <= other.dmg_deal()
