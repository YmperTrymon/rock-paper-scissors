from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


wanna_play_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Давай'), KeyboardButton(text='Не хочу')],
                [KeyboardButton(text='Правила')]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
)

