from State.State import State


class Cold(State):
    def __init__(self, d):
        super().__init__(d)

    def get_state(self):
        self.durability -= 1
        if self.durability == 0:
            print('Холод ушел')
        return True if self.durability >= 0 else False

    def __del__(self):
        del self

    def __str__(self):
        return 'Cold'