class Subject:
    """
    Defines the subjects used within the simulation
        - Kind 0 = Dove
        - Kind 1 = Hawk
    """

    def __init__(self, kind=0, food=0):
        self.type = kind
        self.energy = food


# class Dove(Subject):
#     def __init__(self, food=0):
#         super().__init__()
#         self.kind = 0
#
#
# class Hawk(Subject):
#     def __init__(self, food=0):
#         super().__init__()
#         self.kind = 1
