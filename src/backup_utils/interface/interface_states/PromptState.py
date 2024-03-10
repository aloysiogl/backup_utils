from typing import Callable
from ..InterfaceState import InterfaceState, NextStateWithMessage
from ...LocalDatabaseList import LocalDatabaseList

class PromptState(InterfaceState):
    def __init__(self, database_list: LocalDatabaseList, executor: Callable[[str], NextStateWithMessage]):
        super().__init__(database_list)
        self._executor = executor

    def execute_command(self, command: str) -> NextStateWithMessage:
        return self._executor(command)
    