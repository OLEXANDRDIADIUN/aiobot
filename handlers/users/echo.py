from aiogram import types
from aiogram.dispatcher import FSMContext
# from filters import IsPrivate
from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(content_types=types.ContentTypes.STICKER | types.ContentTypes.ANIMATION)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")
    await message.reply('Текст принят')
#
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(IsPrivate(), state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
