import os
import pickle

from .Drive import Drive


class LocalDatabase:
    """This class manages the data locally stored in a directory"""

    def __init__(self, directory_path: str):
        self._local_database_path = f'{directory_path}/.backup_info.pickle'
        self._drive = Drive()

    def update_drive_info(self, name: str, capacity: int):
        self._drive.name = name
        self._drive.capacity = capacity

    def update_drive_name(self, name: str):
        self._drive.name = name

    def get_drive_name(self):
        return self._drive.name

    def get_drive_capacity(self):
        return self._drive.capacity

    def get_drive_id(self):
        return self._drive.get_drive_id()

    def load(directory_path: str):
        local_database_path = f'{directory_path}/.backup_info.pickle'

        if not os.path.exists(local_database_path):
            return None
        with open(local_database_path, 'rb') as file:
            return pickle.load(file)

    def save(self):
        with open(self._local_database_path, 'wb') as file:
            pickle.dump(self, file)
