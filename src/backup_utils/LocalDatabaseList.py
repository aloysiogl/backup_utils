import os
import copy
from typing import List, Dict, Set
from pathlib import Path

from .LocalDatabase import LocalDatabase
from .Drive import Drive, DriveId
from .BackupFolder import BackupFolder


class LocalDatabaseList:
    def __init__(self):
        self._database_list: List[LocalDatabase] = []
        self._path_to_database: Dict[str, LocalDatabase] = {}

    def get_folders_without_master(self):
        root_paths = self._path_to_database.keys()
        toplevel_paths: Set[str] = set()
        folders_with_master = list(
            map(lambda folder: folder.name, self.get_merged_folder_list()))
        for path in root_paths:
            def filter_func(x: str):
                return os.path.isdir(os.path.join(path, x)) and x not in folders_with_master
            dirs = filter(filter_func, os.listdir(path))
            toplevel_paths.update(dirs)
        return toplevel_paths

    def update_local_databases(self):
        merged_folders = self.get_merged_folder_list()
        merged_drives = self.get_merged_drive_list()
        for database in self._database_list:
            database.set_known_folders(copy.deepcopy(merged_folders))
            database.set_known_drives(copy.deepcopy(merged_drives))

    def get_merged_folder_list(self):
        folders_lists: List[List[BackupFolder]] = []
        for database in self._database_list:
            folders_lists.append(database.get_folders())
        return BackupFolder.merge_backup_folder_lists(folders_lists)

    def get_merged_drive_list(self):
        drives_lists = [database.get_known_drives()
                        for database in self._database_list]
        return Drive.merge_drive_lists(drives_lists)

    def get_drive_ids_for_folder(self, folder_name: str):
        root_paths = self._path_to_database.keys()
        ids: List[DriveId] = []
        for path in root_paths:
            if folder_name in filter(os.path.isdir, os.listdir(path)):
                ids.append(self._path_to_database[path].get_drive_id())
        return ids

    def get_drive_name_from_id(self, drive_id: DriveId):
        for database in self._database_list:
            if database.get_drive_id() == drive_id:
                return database.get_drive_name()

        raise ValueError(
            f"Trying to get drive with id {drive_id}, but not found")

    def add_folder(self, folder: BackupFolder) -> bool:
        folders = self.get_merged_folder_list()
        if folder in folders:
            raise ValueError(
                f"Trying to add folder {folder.name} but already exists")
        for database in self._database_list:
            database.add_folder(folder)
        self.save_all()
        return True

    def add_database(self, database: LocalDatabase, loaded_path: Path) -> bool:
        drive_ids = [db.get_drive_id() for db in self._database_list]
        if database.get_drive_id() not in drive_ids:
            self._database_list.append(database)
            self._path_to_database[str(loaded_path)] = database
            self.save_all()
            return True
        raise ValueError(
            f"Trying to add database with drive id {database.get_drive_id()} but already exists")

    def save_all(self):
        self.update_local_databases()
        for database in self._database_list:
            database.save()

    def get_folder_info_str(self) -> str:
        folders_list = self.get_merged_folder_list()
        drives_list = self.get_merged_drive_list()
        res = ''
        for folder in folders_list:
            master_drive = Drive.get_drive_from_id(
                folder.get_master_drive_id(), drives_list)
            res += f"{folder.name:10s}\n"
            name = master_drive.name if master_drive else "Unknown"
            res += f"  Master: {name:10s}\n"
        return res

    def get_drive_info_str(self) -> str:
        res = ''
        for drive in self.get_merged_drive_list():
            res += f"{drive.name:10s} {drive.capacity:10d}\n"
        return res
