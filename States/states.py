from aiogram.fsm.state import State, StatesGroup

class AdminState(StatesGroup):
    admin = State()
    id = State()
    name = State()
    qism = State()
    year = State()
    Category = State()
    language = State()
    video = State()

class AdminRemoveState(StatesGroup):
    id = State()