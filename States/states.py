from aiogram.fsm.state import State, StatesGroup

class AdminState(StatesGroup):
    admin = State()
    typ = State()


class AdminRemoveState(StatesGroup):
    id = State()