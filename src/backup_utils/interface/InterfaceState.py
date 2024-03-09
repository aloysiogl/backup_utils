import abc
from ..LocalDatabaseList import LocalDatabaseList


class InterfaceState:
    def __init__(self, databases_list = LocalDatabaseList):
        self.available_commands = []
        self._databases_list = databases_list

    @abc.abstractmethod
    def execute_command(self, commnd: str) -> ('InterfaceState', str):
        pass

    def get_available_commands(self) -> str:
        return '; '.join([str(command) for command in self.available_commands])

    def get_next_state(self) -> ('InterfaceState', str):
        raise NotImplementedError
