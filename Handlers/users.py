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
            year = data['year']
            qism = data['qism']
            sec = int(data['sec'])
            category = data['category']
            language = data['language']
            video_id = data['video_id']


            minute = sec // 60
            second = sec % 60
            hour = minute // 60
            minute %= 60

            qism_ls = qism.split()
            fasl = 0
            qism = 0
            if len(qism_ls) > 1:
                fasl = qism_ls[0]
                qism = qism_ls[1]
            elif len(qism_ls) == 1:
                fasl = "1"
                qism = qism_ls[0]

            captions = (
                f"🎬 {name}\n"
                f"{fasl}-fasl, {qism}-qism\n\n"
                f"📆 {year}\n"
                f"🕜 {hour} soat {minute} daqiqa, {second} soniya\n"
                f"💎 {category}\n"
                f"👅 {language}\n"
            )
            await message.answer_video(video=video_id, caption=captions)
        except Exception as e:
            await message.answer(f"Xatolik yuz berdi: {e}")
    else:
        await message.answer("Bunday ID topilmadi.")
