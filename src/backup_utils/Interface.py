from .Drive import Drive


class Interface:
    def __init__(self):
        self.start_available_commands = [
            "q - quit",
            "l - list drives",
            "a - add drive",
        ]
        self.current_screen = ''
        self.command_output = ''
        self.drives_list = []

    def drives_list_str(self, drives):
        return_str = ''
        for drive in drives:
            return_str += f'{drive.name} {drive.capacity}\n'
        if return_str == '':
            return_str = 'No drives found'
        return return_str

    def render(self):
        print(self.current_screen)
        self.print_available_commands()
        print(self.command_output)
        self.current_screen = ''
        self.command_output = ''

    def print_available_commands(self):
        print('Available commands: -----------------')
        for command in self.start_available_commands:
            print(command)
        print('-------------------------------------')

    def process_user_input(self, user_input):
        self.clear_screen()
        if user_input == 'q':
            exit()
        elif user_input == 'l':
            self.command_output = self.drives_list_str(self.drives_list)
        elif user_input == 'a':
            raise NotImplementedError
        else:
            self.command_output = 'Invalid command'

    def clear_screen(self):
        print(chr(27) + "[2J")
