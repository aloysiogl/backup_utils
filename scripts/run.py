from backup_utils.interface.Interface import Interface


def main():
    interface = Interface()

    quit = False

    interface.clear_screen()
    interface.render()

    while not quit:
        user_input = input('>')
        interface.process_user_input(user_input)
        interface.clear_screen()
        interface.render()


if __name__ == '__main__':
    main()
