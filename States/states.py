from aiogram.fsm.state import State, StatesGroup

class AdminState(StatesGroup):
    admin = State()
    id = State()
    name = State()
    Category = State()
    video = State()

class AdminRemoveState(StatesGroup):
    id = State()