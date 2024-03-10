import uuid
from typing import Optional


class Drive:
    def __init__(self, name: Optional[str]= None, capacity: int=-1, id: str=str(uuid.uuid4())):
        self.name = name
        self.capacity = capacity
        self._id = id

    def get_drive_id(self):
        return self._id

    def copy(self):
        return Drive(self.name, self.capacity, self._id)
    
    def __eq__(self, other: object):
        if not isinstance(other, Drive):
            return False
        return self._id == other._id
