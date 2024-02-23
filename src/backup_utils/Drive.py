

class Drive:
    def __init__(self, name, capacity, id=None):
        self.name = name
        self.capacity = capacity
        id = id if id else 0  # if id is None, set it to a new random id
