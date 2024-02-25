from enum import Enum


class InterfaceCommand(Enum):
    QUIT = ('q', 'quit')
    LIST_DRIVES = ('ld', 'lists known drives')
    LIST_FOLDERS = ('lf', 'lists known folders')
    ADD_DRIVE = ('ad', 'adds path to a drive')
    ADD_FOLDER = ('af', 'adds folder name')
    INVALID = (None, 'Invalid command')

    @staticmethod
    def from_str(command_str) -> 'InterfaceCommand':
        for command in InterfaceCommand:
            if command.value[0] == command_str:
                return command
        return InterfaceCommand.INVALID

    def __str__(self):
        return f"{self.value[0]}, {self.value[1]}"
