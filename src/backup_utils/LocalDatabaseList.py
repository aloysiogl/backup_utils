

class LocalDatabaseList:
    def __init__(self):
        self.database_list = []

    def add_database(self, database) -> bool:
        drive_ids = [db.get_drive_id() for db in self.database_list]
        if database.get_drive_id() not in drive_ids:
            self.database_list.append(database)
            return True
        return False

    def __str__(self) -> str:
        return '\n'.join([f"{database.get_drive_name():10s} {database.get_drive_capacity():10d}" for database in self.database_list])