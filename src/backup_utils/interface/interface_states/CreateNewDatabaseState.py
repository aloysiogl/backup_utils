from ...LocalDatabase import LocalDatabase
import backup_utils.interface.interface_states.DefaultInterfaceState as DefaultInterfaceState
from ..InterfaceState import InterfaceState


class CraeteNewDatabaseState(InterfaceState):
    def __init__(self, database_list, new_database_path):
        super().__init__(database_list)
        self._new_database_path = new_database_path
        self.available_commands = [
                "Enter the name for the new drive:",
        ]

    def execute_command(self, command: str) -> ('InterfaceState', str):
        local_database = LocalDatabase(self._new_database_path)
        local_database.update_drive_name(command)
        local_database.save()
        if not self._databases_list.add_database(local_database, self._new_database_path):
            raise ValueError(f'Drive {command} already exists')
        return DefaultInterfaceState.DefaultInterfaceState(self._databases_list), f'New drive {command} created successfully!'

