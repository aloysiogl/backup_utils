from .InterfaceState import InterfaceState


class PartialState(InterfaceState):
    def __init__(self, database_list):
        super().__init__(database_list)

    def is_partial(self):
        return True
    