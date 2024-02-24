import os
from ..InterfaceState import InterfaceState
from ..InterfaceCommand import InterfaceCommand
from ...LocalDatabaseList import LocalDatabaseList
from .GetDrivePathState import GetDrivePathState


class DefaultInterfaceState(InterfaceState):
    def __init__(self, databases_list = LocalDatabaseList()):
        super().__init__()
        self.available_commands = [
            InterfaceCommand.ADD_DRIVE,
            InterfaceCommand.LIST_DRIVES,
            InterfaceCommand.QUIT
        ]
        self._databases_list = databases_list


    def execute_command(self, command: str):
        command = InterfaceCommand.from_str(command)
        command_output = ''
        if command == InterfaceCommand.QUIT:
            exit()
        elif command == InterfaceCommand.LIST_DRIVES:
            command_output = str(self._databases_list)
        elif command == InterfaceCommand.ADD_DRIVE:
            next_state = GetDrivePathState(self._databases_list)
            return next_state, ''
        else:
            self.command_output = 'Invalid command'

        return DefaultInterfaceState(self._databases_list), command_output
