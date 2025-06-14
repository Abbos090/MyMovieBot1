from aiogram import Router, F
from aiogram.types import Message

from Database.load_database import read_vide_db

router = Router()

@router.message(F.text.isdigit())
async def send_video_handler(message: Message):
    id = message.text
    video_id = read_vide_db(id)

    if video_id:  # agar topilgan bo‘lsa
        try:
            await message.answer_video(video=video_id)
        except Exception as e:
            await message.answer(f"Xatolik yuz berdi: {e}")
    else:
        await message.answer("Bunday ID topilmadi.")
