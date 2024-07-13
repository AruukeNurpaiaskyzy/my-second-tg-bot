from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = '7461698787:AAHsplWaxz-cyFcvnyEsCJH77WHhSg1zHNI'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    username = State()
    age = State()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Form.username.set()
    await message.reply("Привет! Как тебя зовут?")

@dp.message_handler(state=Form.username)
async def process_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await Form.next()
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Назад", callback_data="back_to_username"))
    await message.reply("Сколько тебе лет?", reply_markup=keyboard)
    print("Wl1")


@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    await message.reply(f"Привет, {user_data['username']}! Тебе {user_data['age']} лет.")
    await state.finish()

@dp.message_handler(commands='me')
async def cmd_me(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if 'username' in user_data and 'age' in user_data:
        response = f"Твое имя: {user_data['username']}\nТвой возраст: {user_data['age']}"
    else:
        response = "Я пока не знаю информации о тебе."
    
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Назад", callback_data="back_to_username"))
    print("Wl")
    await message.reply(response, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'back_to_username')
async def process_back(callback_query: types.CallbackQuery, state: FSMContext):
    print("er")
    await Form.username.set()
    await bot.send_message(callback_query.from_user.id, "Привет! Как тебя зовут?")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

