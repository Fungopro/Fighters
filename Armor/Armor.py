

class Armor:
    def __init__(self, hp, atr):
        self.hp = hp
        self.atr = atr

    def get_dmg(self, hp):
        self.hp -= hp
        if self.hp >= 0:
            return 0
        else:
            return abs(self.hp)

    def dmg_deal(self):
        raise Exception(' Метод нереализован')

    def __le__(self, other):
        return self.dmg_deal() < other.dmg_deal()
