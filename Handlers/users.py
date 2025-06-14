from aiogram import Router, F
from aiogram.types import Message


from Database.load_database import read_vide_db

router = Router()

@router.message(F.text.isdigit())
async def send_video_handler(message: Message):
    id = message.text
    data = read_vide_db(id)

    if data:
        try:
            name = data['name']
            category = data['category']
            video_id = data['video_id']
            captions = (
                f"🎬 {name}\n"
                f"💎 {category}\n"
            )
            await message.answer_video(video=video_id, caption=captions)
        except Exception as e:
            await message.answer(f"Xatolik yuz berdi: {e}")
    else:
        await message.answer("Bunday ID topilmadi.")
