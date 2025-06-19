from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from States.category_states import AdminSerialState
from Keyboards.languages import languages
from Database.write_database import write_db

router = Router()

@router.message(AdminSerialState.id)
async def add_id_handler(message: Message, state: FSMContext):
    id = message.text
    if id.isdigit():
        await message.answer("Id qabul qilindi")
        await message.answer("Serial nomini kiriting")
        await state.update_data(id=id)
        await state.set_state(AdminSerialState.name)
    else:
        await message.answer("Id son bo'lsin / (12)")
        
@router.message(AdminSerialState.name)
async def add_name_handler(message: Message, state: FSMContext):
    name = message.text
    await message.answer("Name qabul qilindi")
    await message.answer("Serialni faslini kiriting")
    await state.update_data(name=name)
    await state.set_state(AdminSerialState.fasl)


@router.message(AdminSerialState.fasl)
async def add_qism_handler(message: Message, state: FSMContext):
    fasl = message.text
    await message.answer("Fasl qabul qilindi")
    await message.answer("Serialni qismini kiriting")
    await state.update_data(fasl=fasl)
    await state.set_state(AdminSerialState.qism)

@router.message(AdminSerialState.qism)
async def add_qism_handler(message: Message, state: FSMContext):
    qism = message.text
    if qism.isdigit():
        await message.answer("Qism qabul qilindi")
        await message.answer("Serial ishlab chiqarilgan yilni kiriting")
        await state.update_data(qism=qism)
        await state.set_state(AdminSerialState.year)
    else:
        await message.answer("Iltimos son kiriting!")

@router.message(AdminSerialState.year)
async def add_year_handler(message: Message, state: FSMContext):
    year = message.text
    if year.isdigit():
        await message.answer("Yil qabul qilindi")
        await message.answer("Serial janrini kiriting")
        await state.update_data(year=year)
        await state.set_state(AdminSerialState.Category)
    else:
        await message.answer("Iltimos yil kiriting !")


@router.message(AdminSerialState.Category)
async def add_Category_handler(message: Message, state: FSMContext):
    category = message.text
    await message.answer("category qabul qilindi")
    await message.answer("Video tilini jo'nating", reply_markup=languages)
    await state.update_data(category=category)
    await state.set_state(AdminSerialState.language)

@router.message(AdminSerialState.language)
async def add_language_handler(message: Message, state: FSMContext):
    language = message.text
    await message.answer("Til qabul qilindi", reply_markup=ReplyKeyboardRemove())
    await message.answer("Video jo'nating")
    await state.update_data(language=language)
    await state.set_state(AdminSerialState.video)


@router.message(AdminSerialState.video)
async def add_video_handler(message: Message, state: FSMContext):
    while message.text != "Tayyor":
        video = message.video
        if video:
            await message.answer("Video qabul qilindi!")
            duration_sec = message.video.duration
            await state.update_data(sec=duration_sec)
            await state.update_data(video_id=video.file_id)
            data = await state.get_data()
            write_db(data)
            await message.answer("Successfully")
            await message.answer(f"Keyingi qismni jo'nating")
            await state.set_state(AdminSerialState.id)
        else:
            await message.answer("Video jo'nating")

    await state.clear()
