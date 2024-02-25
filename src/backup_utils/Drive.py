import uuid


class Drive:
    def __init__(self, name=None, capacity=-1, id=None):
        self.name = name
        self.capacity = capacity
        self._id = id

    def get_drive_id(self):
        return self._id
    
    def __eq__(self, other: "Drive"):
        return self._id == other._id
