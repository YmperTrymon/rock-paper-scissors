from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, PhotoSize, ReplyKeyboardMarkup, KeyboardButton


from config import load_config
from keyboards import wanna_play_keyboard

from random import choice


dp = Dispatcher()


def roll_the_dice(player: str) -> (str, str):
    print('dice')
    computer = choice(['Камень', 'Ножницы', 'Бумага'])
    won = (computer, 'Вы победили')
    lose = (computer, 'Вы проиграли')
    draw = (computer, 'Ничья')
    if player == computer:
        return draw
    elif player == 'Камень' and computer == 'Ножницы':
        return won
    elif player == 'Ножницы' and computer == 'Бумага':
        return won
    elif player == 'Бумага' and computer == 'Камень':
        return won
    return lose


@dp.message(CommandStart())
async def start_handler(message: Message):
    print('start')
    await message.reply(
        text='Привет! Сыграем в "Камень, ножницы, бумага"?',
        reply_markup=wanna_play_keyboard
    )


@dp.message(F.text == 'Правила')
@dp.message(Command(commands=['help']))
async def help_handler(message: Message):
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Rock-paper-scissors.svg/langru-1024px-Rock-paper-scissors.svg.png',
        reply_markup=wanna_play_keyboard
    )


@dp.message(F.text == 'Давай')
async def lets_play_handler(message: Message):
    await message.reply(
        text='Отлично! Делай свой выбор!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Камень'), KeyboardButton(text='Ножницы'), KeyboardButton(text='Бумага')],
                [KeyboardButton(text='Правила')]
            ],
            resize_keyboard=True
        )
    )


@dp.message(F.text == 'Не хочу')
async def dont_want_handler(message: Message):
    await message.answer(
        text='Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай"',
    )


@dp.message(F.text == 'Камень')
@dp.message(F.text == 'Ножницы')
@dp.message(F.text == 'Бумага')
async def roll_the_dice_handler(message: Message):
    computer, result = roll_the_dice(player=message.text)
    await message.reply(text=f'{computer}\n{result}')
    await message.answer(text='Хотите сыграть ещё раз?',
                         reply_markup=wanna_play_keyboard)


@dp.message()
async def send_echo(message: Message):
    await message.answer(message.text)


if __name__ == '__main__':
    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token)
    print('running')
    dp.run_polling(bot)