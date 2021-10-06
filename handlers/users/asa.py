import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.default import gogo, check_payment
from keyboards.inline.callback_data import buy_callback
from keyboards.inline.key_inline import inline_buttons, drugaya_key
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=gogo)


# @dp.message_handler(Command('gogo'))
# async def bot_start(message: types.Message):
#     await message.answer(f"gogo, {message.from_user.full_name}!", reply_markup=gogo)


@dp.message_handler(text='Rashod')
async def answer_first(message: types.Message):
    logging.info('вы нажали первую кнопку-{}'.format(message))
    await message.answer('вы нажали первую кнопку', reply_markup=check_payment)


@dp.message_handler(text='Back')
async def answer_first(message: types.Message):
    logging.info('вы нажали Back-{}'.format(message))
    await message.answer('вы нажали первую кнопку', reply_markup=gogo)


@dp.message_handler(Text(equals=['Prihod']))
async def answer_second(message: types.Message):
    await message.answer('FUCK_OFF - {}'.format(message.text), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command('inline'))
async def inline_button(messasge: types.Message):
    await messasge.answer(text='Выбери что тебе нужно :\n'
                          'вот варианты: \n', reply_markup=inline_buttons)


@dp.callback_query_handler(buy_callback.filter(item='1_first_inline'))
async def ff(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info('*** i tak callback - {}'.format(call.data))
    logging.info('*** i tak callback_dict - {}'.format(callback_data))
    await call.message.answer('your chose - {}'.format(callback_data.get('name')),
                              reply_markup=drugaya_key)


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('отмена', show_alert=True)
    await call.message.edit_reply_markup()

