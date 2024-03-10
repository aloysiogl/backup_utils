import uuid
from functools import reduce
from enum import Enum
from typing import Optional, List, Dict

class DriveId(str):
    pass

class UpdateAction(Enum):
    RENAME = 1
    RESIZE = 2

class Drive:
    def __init__(self, name: Optional[str]= None, capacity: int=-1, id: DriveId=DriveId(str(uuid.uuid4()))):
        self._name = name
        self._capacity = capacity
        self._id = id
        self.update_history: List[UpdateAction] = []

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def capacity(self):
        return self._capacity

    def copy(self):
        return Drive(self._name, self._capacity, self._id)
    
    def __eq__(self, other: object):
        if not isinstance(other, Drive):
            return False
        return self._id == other._id
 
    @staticmethod
    def merge_drive_lists(drive_lists: List[List['Drive']]):
        flattened_list = [drive for drive_list in drive_lists for drive in drive_list]

        # group by id
        drive_id_to_drives: Dict[DriveId, List['Drive']] = {}
        for drive in flattened_list:
            if drive.id not in drive_id_to_drives:
                drive_id_to_drives[drive.id] = [drive]
            else:
                drive_id_to_drives[drive.id].append(drive)

        def reduce_drives(d1: 'Drive', d2: 'Drive'):
            if d1.id != d2.id:
                raise ValueError(f"Trying to merge drives with different ids {d1.id} and {d2.id}")
            if len(d1.update_history) > len(d2.update_history):
                return d1
            elif len(d1.update_history) < len(d2.update_history):
                return d2
            else:
                same_name = d1._name == d2._name
                same_capacity = d1._capacity == d2._capacity
                same_lists = d1.update_history == d2.update_history
                if not all([same_name, same_capacity, same_lists]):
                    raise ValueError(f"Trying to merge drives with different information but same history sizes {d1} and {d2}")
                return d1

        return [reduce(reduce_drives, drive_id_to_drives[id]) for id in drive_id_to_drives.keys()]

