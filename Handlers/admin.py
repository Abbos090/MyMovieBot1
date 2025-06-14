from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import ADMINS
from Keyboards.add_remove import admin_key
from States.states import AdminState, AdminRemoveState
from Database.write_database import write_db

router = Router()

@router.message(CommandStart())
async def admin_start_handler(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Xush kelibsiz admin", reply_markup=admin_key)
        await state.set_state(AdminState.admin)
    else:
        await message.answer(f"Xush kelibsiz {message.from_user.full_name}")
        await message.answer("Kino kodini kiriting :")

@router.message(AdminState.admin)
async def add_remove_handler(message: Message, state: FSMContext):
    if message.text == "add_movie":
        await state.set_state(AdminState.id)
        await message.answer("Id kiriting :")
    elif message.text == "remove_movie":
        await state.set_state(AdminRemoveState.id)
        await message.answer("O'chirmoqchi bo'lgan kinoyingiz id sini kiriting")

@router.message(AdminState.id)
async def add_id_handler(message: Message, state: FSMContext):
    id = message.text
    if id.isdigit():
        await message.answer("Id qabul qilindi")
        await message.answer("Kino nomini kiriting")
        await state.update_data(id=id)
        await state.set_state(AdminState.name)
    else:
        await message.answer("Id son bo'lsin / (12)")

@router.message(AdminState.name)
async def add_name_handler(message: Message, state: FSMContext):
    name = message.text
    await message.answer("Name qabul qilindi")
    await message.answer("Kino janrini kiriting")
    await state.update_data(name=name)
    await state.set_state(AdminState.Category)


@router.message(AdminState.Category)
async def add_Category_handler(message: Message, state: FSMContext):
    category = message.text
    await message.answer("category qabul qilindi")
    await message.answer("Video jo'nating")
    await state.update_data(category=category)
    await state.set_state(AdminState.video)


@router.message(AdminState.video)
async def add_video_handler(message: Message, state: FSMContext):
    video = message.video
    if video:
        await message.answer("Video qabul qilindi!")
        await state.update_data(video_id=video.file_id)
        data = await state.get_data()
        write_db(data)
        await state.clear()
        await message.answer("Successfully")


    else:
        await message.answer("Video jo'nating")