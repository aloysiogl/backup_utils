from pathlib import Path
from ...LocalDatabase import LocalDatabase
from ...LocalDatabaseList import LocalDatabaseList
import backup_utils.interface.interface_states.DefaultInterfaceState as DefaultInterfaceState
from ..InterfaceState import InterfaceState, NextStateWithMessage
from ..InterfaceCommand import InterfaceCommandPrompt


class CraeteNewDatabaseState(InterfaceState):
    def __init__(self, database_list: LocalDatabaseList, new_database_path: Path):
        super().__init__(database_list)
        self._new_database_path = new_database_path
        self.available_commands = [
                InterfaceCommandPrompt("Enter the name for the new drive:")
        ]

    def execute_command(self, command: str) -> NextStateWithMessage:
        local_database = LocalDatabase(self._new_database_path)
        local_database.update_drive_name(command)
        local_database.save()
        if not self._databases_list.add_database(local_database, self._new_database_path):
            raise ValueError(f'Drive {command} already exists')
        return NextStateWithMessage(DefaultInterfaceState.DefaultInterfaceState(self._databases_list), f'New drive {command} created successfully!')

