import os
from pathlib import Path


from .CreateNewDatabaseState import CraeteNewDatabaseState
from ...LocalDatabase import LocalDatabase
from ...LocalDatabaseList import LocalDatabaseList
from ..InterfaceState import InterfaceState, NextStateWithMessage
from ..InterfaceCommand import InterfaceCommandPrompt
import backup_utils.interface.interface_states.DefaultInterfaceState as DefaultInterfaceState


class GetDrivePathState(InterfaceState):
    def __init__(self, database_list: LocalDatabaseList):
        super().__init__(database_list)
        self.available_commands = [
            InterfaceCommandPrompt("Enter path (if none is given, current path is used):")
        ]

    def execute_command(self, command: str) -> NextStateWithMessage:
        command_output = ''
        if command == '':
            command = os.getcwd()
            command_output = f'Path not given, defalt to {command}'
        path = Path(command)
        local_database = LocalDatabase.load(path)
        if local_database is None:
            return NextStateWithMessage(CraeteNewDatabaseState(self._databases_list, path), command_output)
        if not self._databases_list.add_database(local_database, path):
            raise ValueError(f'Drive {local_database.get_drive_name()} already exists')
        return NextStateWithMessage(DefaultInterfaceState.DefaultInterfaceState(self._databases_list), f'Loaded successfully the drive: {local_database.get_drive_name()}')
