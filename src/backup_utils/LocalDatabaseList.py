import os
from typing import List, Dict, Set
from pathlib import Path

from .LocalDatabase import LocalDatabase
from .Drive import Drive
from .BackupFolder import BackupFolder

class LocalDatabaseList:
    def __init__(self):
        self._database_list: List[LocalDatabase] = []
        self._path_to_database: Dict[str, LocalDatabase] = {}

    def get_folders_without_master(self):
        root_paths = self._path_to_database.keys()
        toplevel_paths: Set[str] = set()
        folders_with_master = list(map(lambda folder: folder.name, self.get_merged_folder_list()))
        for path in root_paths:
            def filter_func(x: str):
                return os.path.isdir(os.path.join(path, x)) and x not in folders_with_master
            dirs = filter(filter_func, os.listdir(path)) 
            toplevel_paths.update(dirs)
        return toplevel_paths
    
    def get_drive_ids_for_folder(self, folder_name: str):
        root_paths = self._path_to_database.keys()
        ids: List[str] = []
        for path in root_paths:
            if folder_name in filter(os.path.isdir, os.listdir(path)):
                ids.append(self._path_to_database[path].get_drive_id())
        return ids

    def get_drive_name_from_id(self, drive_id: str):
        for database in self._database_list:
            if database.get_drive_id() == drive_id:
                return database.get_drive_name()

        raise ValueError(f"Trying to get drive with id {drive_id}, but not found")

    def add_folder(self, folder: BackupFolder) -> bool:
        for database in self._database_list:
            database.add_folder(folder)
        return True

    def add_database(self, database: LocalDatabase, loaded_path: Path) -> bool:
        drive_ids = [db.get_drive_id() for db in self._database_list]
        if database.get_drive_id() not in drive_ids:
            self._database_list.append(database)
            self._path_to_database[str(loaded_path)] = database
            return True
        return False

    def get_merged_folder_list(self):
        folders_list: List[BackupFolder] = []
        for database in self._database_list:
            folders_list += database.get_folders()
        return BackupFolder.merge_backup_folder_lists(folders_list)

    def get_folder_info_str(self) -> str:
        folders_list = self.get_merged_folder_list()
        res = '' 
        for folder in folders_list:
            res += f"{folder.name:10s} {folder.get_master_drive_id():10s}\n"
        return res

    def get_drive_info_str(self) -> str:
        known_drives: Dict[str, Drive] = {}
        for database in self._database_list:
            for drive in database.get_known_drives():
                known_drives[drive.get_drive_id()] = drive
        res = ''
        for drive in known_drives.values():
            res += f"{drive.name:10s} {drive.capacity:10d}\n"

        return res