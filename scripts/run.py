import os
import click
from pathlib import Path
from backup_utils.interface.Interface import Interface


@click.command()
@click.option('--load-current-path', is_flag=True, default=False, help='Load current path')
def main(load_current_path: bool):
    interface = Interface()
    if load_current_path:
        current_path = os.getcwd() 
        interface = Interface(Path(current_path))
    interface.run()

if __name__ == '__main__':
    main()
