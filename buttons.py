from aiogram import types

def back():
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    return keyboard
