from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove

from config import ADMINS
from Keyboards.add_remove import admin_key
from Keyboards.languages import languages
from Keyboards.typ_kb import typ_kb
from States.states import AdminState, AdminRemoveState
from States.category_states import AdminSerialState, AdminKinoState
from Database.write_database import write_db
from Database.delete_database import delete_db

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
        await state.set_state(AdminState.typ)
        await message.answer("Qaysi categoriyani tanlaysiz ?", reply_markup=typ_kb)
    elif message.text == "remove_movie":
        await state.set_state(AdminRemoveState.id)
        await message.answer("O'chirmoqchi bo'lgan kinoyingiz id sini kiriting")

@router.message(AdminState.typ)
async def add_typ_handler(message: Message, state: FSMContext):
    if message.text == "Serial":
        await state.set_state(AdminSerialState.id)
        await message.answer("Serialning id sini kiriting")
    elif message.text == "Kino":
        await state.set_state(AdminKinoState.id)
        await message.answer("Kinoning id sini kiriting")
    else:
        await message.answer("Bunday category yo'q!")



@router.message(AdminRemoveState.id)
async def remove_all_handler(message:Message):
    id = message.text
    if id.isdigit():
        delete_db(id)
        await message.answer("Muvaffaqiyatli o'chirildi!")
    else:
        await message.answer("Video idsini kiriting / (123)")


# @router.message(AdminSerialState.id)
# async def add_id_handler(message: Message, state: FSMContext):
#     id = message.text
#     if id.isdigit():
#         await message.answer("Id qabul qilindi")
#         await message.answer("Serial nomini kiriting")
#         await state.update_data(id=id)
#         await state.set_state(AdminSerialState.name)
#     else:
#         await message.answer("Id son bo'lsin / (12)")
#
#
# @router.message(AdminSerialState.name)
# async def add_name_handler(message: Message, state: FSMContext):
#     name = message.text
#     await message.answer("Name qabul qilindi")
#     await message.answer("Serialni faslini kiriting")
#     await state.update_data(name=name)
#     await state.set_state(AdminSerialState.qism)
#
#
# @router.message(AdminSerialState.qism)
# async def add_qism_handler(message: Message, state: FSMContext):
#     fasl = message.text
#     await message.answer("Qism qabul qilindi")
#     await message.answer("Serial ishlab chiqarilgan yilni kiriting")
#     await state.update_data(fasl=fasl)
#     await state.set_state(AdminSerialState.year)
#
#
# @router.message(AdminSerialState.year)
# async def add_year_handler(message: Message, state: FSMContext):
#     year = message.text
#     if year.isdigit():
#         await message.answer("Yil qabul qilindi")
#         await message.answer("Serial janrini kiriting")
#         await state.update_data(year=year)
#         await state.set_state(AdminSerialState.Category)
#     else:
#         await message.answer("Iltimos yil kiriting !")
#
#
# @router.message(AdminSerialState.Category)
# async def add_Category_handler(message: Message, state: FSMContext):
#     category = message.text
#     await message.answer("category qabul qilindi")
#     await message.answer("Video tilini jo'nating", reply_markup=languages)
#     await state.update_data(category=category)
#     await state.set_state(AdminSerialState.language)
#
#
# @router.message(AdminSerialState.language)
# async def add_language_handler(message: Message, state: FSMContext):
#     language = message.text
#     await message.answer("Til qabul qilindi", reply_markup=ReplyKeyboardRemove())
#     await message.answer("Video jo'nating")
#     await state.update_data(language=language)
#     await state.set_state(AdminSerialState.video)
#
#
# @router.message(AdminSerialState.video)
# async def add_video_handler(message: Message, state: FSMContext):
#     qism = 1
#     while message.text != "Tayyor":
#         qism += 1
#         video = message.video
#         if video:
#             await message.answer("Video qabul qilindi!")
#             duration_sec = message.video.duration
#             await state.update_data(sec=duration_sec)
#             await state.update_data(video_id=video.file_id)
#             data = await state.get_data()
#             write_db(data)
#             await message.answer("Successfully")
#             await message.answer(f"Serialning {qism}-qismini jo'nating")
#         else:
#             await message.answer("Video jo'nating")
#
#     await state.clear()
