class Subject:
    """
    Defines the subjects used within the simulation
        - Kind 0 = Dove
        - Kind 1 = Hawk
    """

    subject_count = 0  # total number of subjects

    def __init__(self, kind=0, food=0):
        self.type = kind
        self.energy = food
        Subject.subject_count += 1