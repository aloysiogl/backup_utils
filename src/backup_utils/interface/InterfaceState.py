import abc
from typing import NamedTuple, List
from ..LocalDatabaseList import LocalDatabaseList
from .InterfaceCommand import InterfaceCommand

class NextStateWithMessage(NamedTuple):
    state: 'InterfaceState'
    message: str


class InterfaceState:
    def __init__(self, databases_list: LocalDatabaseList):
        self.available_commands: List[InterfaceCommand] = []
        self._databases_list = databases_list
        self._is_partial = False
    
    @property
    def is_partial(self):
        return self._is_partial

    @abc.abstractmethod
    def execute_command(self, command: str) -> NextStateWithMessage:
        pass

    def get_available_commands(self) -> str:
        return '; '.join([str(command) for command in self.available_commands])

    def get_next_state(self) -> NextStateWithMessage:
        raise NotImplementedError
