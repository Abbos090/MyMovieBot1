from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from Keyboards.languages import languages
from States.category_states import AdminKinoState
from Database.write_database import write_db

router = Router()

@router.message(AdminKinoState.id)
async def add_id_handler(message: Message, state: FSMContext):
    id = message.text
    if id.isdigit():
        await message.answer("Id qabul qilindi")
        await message.answer("Kino nomini kiriting")
        await state.update_data(id=id)
        await state.set_state(AdminKinoState.name)
    else:
        await message.answer("Id son bo'lsin / (12)")

@router.message(AdminKinoState.name)
async def add_name_handler(message: Message, state: FSMContext):
    name = message.text
    await message.answer("Kino nomi qabul qilindi")
    await message.answer("Kino qismini kiriting")
    await state.update_data(name=name)
    await state.set_state(AdminKinoState.qism)

@router.message(AdminKinoState.qism)
async def add_qism_handler(message: Message, state: FSMContext):
    qism = message.text
    await message.answer("Qism qabul qilindi")
    await message.answer("Kino ishlab chiqarilgan yilni kiriting")
    await state.update_data(qism=qism)
    await state.set_state(AdminKinoState.year)

@router.message(AdminKinoState.year)
async def add_year_handler(message: Message, state: FSMContext):
    year = message.text
    if year.isdigit():
        await message.answer("Yil qabul qilindi")
        await message.answer("Kino janrini kiriting")
        await state.update_data(year=year)
        await state.set_state(AdminKinoState.Category)
    else:
        await message.answer("Iltimos yil kiriting !")


@router.message(AdminKinoState.Category)
async def add_Category_handler(message: Message, state: FSMContext):
    category = message.text
    await message.answer("category qabul qilindi")
    await message.answer("Video tilini kiriting", reply_markup=languages)
    await state.update_data(category=category)
    await state.set_state(AdminKinoState.language)

@router.message(AdminKinoState.language)
async def add_language_handler(message: Message, state: FSMContext):
    language = message.text
    await message.answer("Til qabul qilindi", reply_markup=ReplyKeyboardRemove())
    await message.answer("Video jo'nating")
    await state.update_data(language=language)
    await state.set_state(AdminKinoState.video)


@router.message(AdminKinoState.video)
async def add_video_handler(message: Message, state: FSMContext):
    video = message.video
    if video:
        await message.answer("Video qabul qilindi!")
        duration_sec = message.video.duration
        await state.update_data(sec=duration_sec)
        await state.update_data(video_id=video.file_id)
        data = await state.get_data()
        write_db(data)
        await state.clear()
        await message.answer("Successfully")


    else:
        await message.answer("Video jo'nating")
