from typing import List, Dict, Tuple
from datetime import datetime
from .Drive import DriveId
import copy

BackupRecord = Tuple[DriveId, datetime]

class BackupFolder:
    def __init__(self, folder_name: str, master_drive_id: DriveId) -> None:
        self._folder_name = folder_name
        self._master_drive_id = master_drive_id
        self._backup_drive_ids = [master_drive_id]
        self._update_date_history: Dict[str, List[BackupRecord]] = {}

    def add_slave_drive(self, drive_id: DriveId) -> None:
        self._backup_drive_ids.append(drive_id)

    def get_master_drive_id(self) -> str:
        return self._master_drive_id

    def get_slave_drive_ids(self) -> List[DriveId]:
        return self._backup_drive_ids

    @property
    def name(self) -> str:
        return self._folder_name

    @staticmethod
    def compare_update_histories(h1: List[BackupRecord], h2: List[BackupRecord]) -> bool:
        # TODO: should check if every date is the same other than the length
        # Returns if h1 is greater or equal than h2
        return len(h1) >= len(h2)
    
    def __ge__(self, other: 'BackupFolder') -> bool:
        if self._folder_name != other._folder_name:
            raise ValueError(f"You are comparing two different folders {self._folder_name} and {other._folder_name}")
        if self._master_drive_id != other._master_drive_id:
            raise ValueError(f"Folders with the same name have different master drives {self._master_drive_id} and {other._master_drive_id}")
        greater_or_equal = True
        for drive_id in other._update_date_history:
            if drive_id not in self._backup_drive_ids:
                greater_or_equal = False
        inconsistent = False
        for drive_id in self._update_date_history:
            if drive_id not in other._backup_drive_ids and not greater_or_equal:
                inconsistent = True
                break
            if BackupFolder.compare_update_histories(self._update_date_history[drive_id], other._update_date_history[drive_id]) and not greater_or_equal:
                inconsistent = True
                break
            elif not BackupFolder.compare_update_histories(self._update_date_history[drive_id], other._update_date_history[drive_id]):
                greater_or_equal = False
        if inconsistent:
            raise ValueError(f"Update histories are inconsistent with regards to what should be allowed")
        return greater_or_equal


    @staticmethod
    def merge_backup_folder_lists(backup_folder_list: List['BackupFolder']):
        name_to_most_recent_folder: Dict[str, 'BackupFolder'] = {}
        for backup_folder in backup_folder_list:
            if backup_folder.name not in name_to_most_recent_folder:
                name_to_most_recent_folder[backup_folder.name] = copy.deepcopy(backup_folder)
            else:
                if backup_folder >= name_to_most_recent_folder[backup_folder.name]:
                    name_to_most_recent_folder[backup_folder.name] = copy.deepcopy(backup_folder)
        return list(name_to_most_recent_folder.values())
