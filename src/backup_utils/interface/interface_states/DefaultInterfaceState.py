from ..InterfaceState import InterfaceState, NextStateWithMessage
from ..InterfaceCommand import InterfaceCommandEnum
from ...LocalDatabaseList import LocalDatabaseList
from .GetDrivePathState import GetDrivePathState
from .AddFolderState import AddFolderState


class DefaultInterfaceState(InterfaceState):
    def __init__(self, databases_list: LocalDatabaseList = LocalDatabaseList()):
        super().__init__(databases_list)
        self.available_commands = [
            InterfaceCommandEnum.ADD_DRIVE,
            InterfaceCommandEnum.ADD_FOLDER,
            InterfaceCommandEnum.LIST_DRIVES,
            InterfaceCommandEnum.LIST_FOLDERS,
            InterfaceCommandEnum.QUIT
        ]
        
    def execute_command(self, command: str) -> NextStateWithMessage:
        parsed_command = InterfaceCommandEnum.from_str(command)
        command_output = ''
        if parsed_command == InterfaceCommandEnum.QUIT:
            exit()
        elif parsed_command == InterfaceCommandEnum.LIST_DRIVES:
            command_output = self._databases_list.get_drive_info_str()
        elif parsed_command == InterfaceCommandEnum.ADD_DRIVE:
            next_state = GetDrivePathState(self._databases_list)
            return NextStateWithMessage(next_state, '')
        elif parsed_command == InterfaceCommandEnum.LIST_FOLDERS:
            command_output = self._databases_list.get_folder_info_str()
        elif parsed_command == InterfaceCommandEnum.ADD_FOLDER:
            return NextStateWithMessage(AddFolderState(self._databases_list), '')
        elif parsed_command == InterfaceCommandEnum.INVALID:
            command_output = 'Invalid command'

        return NextStateWithMessage(DefaultInterfaceState(self._databases_list), command_output)

