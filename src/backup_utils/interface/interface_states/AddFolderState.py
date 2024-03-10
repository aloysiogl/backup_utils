from ..PartialState import PartialState
from ..InterfaceState import NextStateWithMessage
from .PromptState import PromptState
from ...BackupFolder import BackupFolder
from ...LocalDatabaseList import LocalDatabaseList
import backup_utils.interface.interface_states.DefaultInterfaceState as DefaultInterfaceState


class AddFolderState(PartialState):
    def __init__(self, database_list: LocalDatabaseList):
        super().__init__(database_list)

    def get_next_state(self) -> NextStateWithMessage:
        first_prompt_head = "Enter the name of the folder to add (list of non tracked folders):\n"
        possible_folder_names = self._databases_list.get_folders_without_master()
        first_prompt = f"{first_prompt_head}\n{str(possible_folder_names)}"

        def process_folder_name(folder_name: str):
            if folder_name not in possible_folder_names:
                return NextStateWithMessage(AddFolderState(self._databases_list), "")
            second_prompt = f"Enter the name of the drive to add the folder to (list of drives):\n"
            possible_drive_ids = self._databases_list.get_drive_ids_for_folder(folder_name)
            names_to_ids = {self._databases_list.get_drive_name_from_id(id): id for id in possible_drive_ids}
            second_prompt += f"{str(names_to_ids)}"

            def process_drive_name(drive_name: str):
                if drive_name not in names_to_ids:
                    return NextStateWithMessage(AddFolderState(self._databases_list), "")
                new_folder = BackupFolder(folder_name, names_to_ids[drive_name])
                print(names_to_ids)
                self._databases_list.add_folder(new_folder)
                final_message = f"Successfully added folder {folder_name} with master {drive_name}"
                return NextStateWithMessage(DefaultInterfaceState.DefaultInterfaceState(self._databases_list), final_message)

            return NextStateWithMessage(PromptState(self._databases_list, process_drive_name), second_prompt)


        return NextStateWithMessage(PromptState(self._databases_list, process_folder_name), first_prompt)
