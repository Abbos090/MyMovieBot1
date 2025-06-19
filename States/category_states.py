from aiogram.fsm.state import State, StatesGroup

class AdminSerialState(StatesGroup):
    id = State()
    name = State()
    fasl = State()
    qism = State()
    year = State()
    Category = State()
    language = State()
    video = State()

class AdminKinoState(StatesGroup):
    id = State()
    name = State()
    qism = State()
    year = State()
    Category = State()
    language = State()
    video = State()
