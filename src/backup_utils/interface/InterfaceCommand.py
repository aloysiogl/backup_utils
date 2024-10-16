from typing import Union
from enum import Enum

class InterfaceCommandPrompt:
    def __init__(self, prompt: str):
        self.prompt = prompt
    
    def __str__(self):
        return self.prompt

class InterfaceCommandEnum(Enum):
    QUIT = ('q', 'quit')
    LIST_DRIVES = ('ld', 'lists known drives')
    LIST_FOLDERS = ('lf', 'lists known folders')
    ADD_DRIVE = ('ad', 'adds path to a drive')
    ADD_FOLDER = ('af', 'adds folder name')
    ADD_FOLDER_SLAVE = ('afs', 'adds folder slave drive')
    PROMPT = ('', 'prompt')
    INVALID = (None, 'Invalid command')

    @staticmethod
    def from_str(command_str: str) -> 'InterfaceCommandEnum':
        for command in InterfaceCommandEnum:
            if command.value[0] == command_str:
                return command
        return InterfaceCommandEnum.INVALID

    def __str__(self):
        return f"{self.value[0]}, {self.value[1]}"


InterfaceCommand = Union[InterfaceCommandPrompt, InterfaceCommandEnum]
