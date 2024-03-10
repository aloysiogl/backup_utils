from ..LocalDatabaseList import LocalDatabaseList
from .InterfaceState import InterfaceState


class PartialState(InterfaceState):
    def __init__(self, database_list: LocalDatabaseList):
        super().__init__(database_list)

    @property
    def is_partial(self):
        return True
    