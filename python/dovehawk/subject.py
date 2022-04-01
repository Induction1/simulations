class Subject:
    """
    Defines the subjects used within the simulation
        - Kind 0 = Dove
        - Kind 1 = Hawk
    """

    def __init__(self, food=0):
        self.energy = food


class Dove(Subject):
    def __init__(self, food=0):
        super().__init__()
        self.kind = 0

    def interact(self, other):
        if other is not None:
            


class Hawk(Subject):
    def __init__(self, food=0):
        super().__init__()
        self.kind = 1
