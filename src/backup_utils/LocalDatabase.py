import os
import copy
import pickle
from typing import List

from .Drive import Drive
from .BackupFolder import BackupFolder


class LocalDatabase:
    """This class manages the data locally stored in a directory"""

    def __init__(self, directory_path: str):
        self._local_database_path = f'{directory_path}/.backup_info.pickle'
        self._drive = Drive()
        self._known_drives = [self._drive]
        self._known_folders: List[BackupFolder] = []

    def update_drive_info(self, name: str, capacity: int):
        self._drive.name = name
        self._drive.capacity = capacity

    def get_folders(self) -> List[BackupFolder]:
        return self._known_folders

    def get_known_drives(self) -> List[Drive]:
        return self._known_drives

    def update_drive_name(self, name: str):
        self._drive.name = name

    def get_drive_name(self):
        return self._drive.name

    def get_drive_capacity(self):
        return self._drive.capacity

    def get_drive_id(self):
        return self._drive.get_drive_id()

    def add_folder(self, folder: BackupFolder):
        self._known_folders.append(folder)

    # TODO: implement full merge (also for folders)
    def merge_drive_list(self, other: 'LocalDatabase'):
        # TODO: will need some changes if there are updates to the drive and if drives are removed as well
        for drive in other._known_drives:
            if drive not in self._known_drives:
                self._known_drives.append(drive.copy())

    def load(directory_path: str):
        # TODO convert from pickle to a real database or something that I can change over time
        local_database_path = f'{directory_path}/.backup_info.pickle'

        if not os.path.exists(local_database_path):
            return None
        with open(local_database_path, 'rb') as file:
            return pickle.load(file)

    def save(self):
        with open(self._local_database_path, 'wb') as file:
            pickle.dump(self, file)
