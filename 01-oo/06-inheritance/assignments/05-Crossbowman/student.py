class Human:
    def __init__(self, name):
        self._name = name  # Eén underscore om name mangling te voorkomen

    def get_name(self):
        return self._name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self._num_arrows = num_arrows  # Eén underscore

    def get_num_arrows(self):
        return self._num_arrows

    def use_arrows(self, num):
        if num > self._num_arrows:
            raise ValueError("Not enough arrows")
        self._num_arrows -= num


class Crossbowman(Archer, Human):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)  # Gebruik de bestaande methode
        return f"{target} was shot by 3 crossbow bolts"
