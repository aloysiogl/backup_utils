from enum import Enum


class InterfaceCommand(Enum):
    QUIT = ('q', 'quit')
    LIST_DRIVES = ('l', 'list drives')
    ADD_DRIVE = ('a', 'add drive')

    @staticmethod
    def from_str(command_str) -> 'InterfaceCommand':
        for command in InterfaceCommand:
            if command.value[0] == command_str:
                return command
        raise ValueError(f'Invalid command: {command_str}')

    def __str__(self):
        return f"{self.value[0]}, {self.value[1]}"
