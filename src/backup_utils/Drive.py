import uuid


class Drive:
    def __init__(self, name=None, capacity=-1, id=str(uuid.uuid4())):
        self.name = name
        self.capacity = capacity
        self._id = id

    def get_drive_id(self):
        return self._id
    
    def __eq__(self, other: "Drive"):
        return self._id == other._id
