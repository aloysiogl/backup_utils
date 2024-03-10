from typing import Callable

from backup_utils.interface.InterfaceState import InterfaceState, NextStateWithMessage
from backup_utils.interface.PartialState import PartialState
from ...LocalDatabaseList import LocalDatabaseList
from ..PartialState import PartialState


class ExecutorState(PartialState):
    def __init__(self, database_list: LocalDatabaseList, executor_func: Callable[[], str], next_state: InterfaceState):
        super().__init__(database_list)
        self._executor_func = executor_func
        self._next_state = next_state

    def get_next_state(self) -> NextStateWithMessage:
        execution_output = self._executor_func()
        return NextStateWithMessage(self._next_state, execution_output)
