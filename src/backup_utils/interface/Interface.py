from pathlib import Path
from typing import List, Optional
from ..Drive import Drive
from .interface_states.DefaultInterfaceState import DefaultInterfaceState
from .InterfaceState import InterfaceState
from ..LocalDatabaseList import LocalDatabaseList
from ..LocalDatabase import LocalDatabase


class Interface:
    def __init__(self, init_path: Optional[Path] = None):
        starting_database_list = LocalDatabaseList()
        if init_path is not None:
            loaded_database = LocalDatabase.load(init_path)
            if loaded_database is not None:
                starting_database_list.add_database(loaded_database, init_path)

        self._current_state: InterfaceState = DefaultInterfaceState(starting_database_list)
        self._command_output = ''
        

    def drives_list_str(self, drives: List[Drive]):
        return_str = ''
        for drive in drives:
            return_str += f'{drive.name} {drive.capacity}\n'
        if return_str == '':
            return_str = 'No drives found'
        return return_str

    def render(self, command_output: str = ''):
        self.print_available_commands()
        print(self._command_output)
        self._command_output = ''

    def print_available_commands(self):
        print('Available commands: -----------------')
        print(self._current_state.get_available_commands())
        print('-------------------------------------')

    def process_user_input(self, user_input: str):
        self._current_state, self._command_output = self._current_state.execute_command(
            user_input)

    def run(self):
        self.clear_screen()
        self.render()

        while True:
            if not (hasattr(self._current_state, "is_partial") and self._current_state.is_partial):
                user_input = input('>')
                self.process_user_input(user_input)
            else:
                self._current_state, self._command_output = self._current_state.get_next_state()
            self.clear_screen()
            self.render()


    def clear_screen(self):
        print(chr(27) + "[2J")
