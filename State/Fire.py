from State.State import State


class Fire(State):
    def __init__(self, d, dmg):
        super().__init__(d)
        self.dmg = dmg

    def get_state(self):
        self.durability -= 1
        if self.durability >= 0:
            print('Огонь ушел')
        return self.dmg if self.durability >= 0 else 0

    def __del__(self):
        del self

    def __str__(self):
        return 'Fire'