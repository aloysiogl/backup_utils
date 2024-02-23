from backup_utils.Interface import Interface
from backup_utils.Drive import Drive


def main():
    interface = Interface()

    quit = False

    interface.clear_screen()

    while not quit:
        user_input = input('>')
        interface.process_user_input(user_input)
        interface.render()

if __name__ == '__main__':
    main()
