from ..InterfaceState import InterfaceState

class PromptState(InterfaceState):
    def __init__(self, database_list, executor):
        super().__init__(database_list)
        self._executor = executor

    def execute_command(self, command: str) -> ('InterfaceState', str):
        next_state, output_str = self._executor(command)
        return next_state, output_str
    
