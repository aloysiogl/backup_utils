from ..InterfaceState import InterfaceState

class PromptState(InterfaceState):
    def __init__(self, database_list, executor, next_state):
        super().__init__(database_list)
        self._executor = executor
        self._next_state = next_state

    def execute_command(self, command: str) -> ('InterfaceState', str):
        output_str = self._executor(command)
        return self._next_state, output_str
    
