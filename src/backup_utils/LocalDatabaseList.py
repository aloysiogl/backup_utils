from .BackupFolder import BackupFolder

class LocalDatabaseList:
    def __init__(self):
        self._database_list = []
        self._path_to_database = {}

    def add_database(self, database, loaded_path) -> bool:
        drive_ids = [db.get_drive_id() for db in self._database_list]
        if database.get_drive_id() not in drive_ids:
            self._database_list.append(database)
            self._path_to_database[loaded_path] = database
            return True
        return False

    def get_folder_info_str(self) -> str:
        folders_list = []
        for database in self._database_list:
            folders_list += database.get_folders()
        folders_list = BackupFolder.merge_backup_folder_lists(folders_list)
        res = '' 
        for folder in folders_list:
            res += f"{folder.name:10s} {folder.get_master_drive_id():10s}\n"
        return res

    def get_drive_info_str(self) -> str:
        known_drives = {}
        for database in self._database_list:
            for drive in database.get_known_drives():
                known_drives[drive.get_drive_id()] = drive
        res = ''
        for drive in known_drives.values():
            res += f"{drive.name:10s} {drive.capacity:10d}\n"

        return res