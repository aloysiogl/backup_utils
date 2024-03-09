from backup_utils.interface.InterfaceState import InterfaceState
from ..PartialState import PartialState

class ExecutorState(PartialState):
    def __init__(self, database_list, executor_func, next_state):
        super().__init__(database_list)
        self._executor_func = executor_func
        self._next_state = next_state

    def get_next_state(self) -> ('InterfaceState', str):
        execution_output = self._executor_func()
        return self._next_state, execution_output

    