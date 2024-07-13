from aiogram import Bot, Dispatcher, types, executor
from logging  import basicConfig, INFO
from config import token 
bot = Bot(token = token)
dp = Dispatcher(bot)
basicConfig(level=INFO)
start_buttons = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Курсы"),
    types.KeyboardButton("Адрес"),
    types.KeyboardButton("контакты"),
]
start_keyboard = types.ReplyKeyboardMarkup().add(*start_buttons)


@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer(f"здравствуйте,{message.from_user.full_name}!", reply_markup=start_keyboard)
@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.reply("Geeks - это айти курсы")
@dp.message_handler(text="Адрес")
async def send_location(message:types.Message):
    await message.reply("наш адрес город Ош мырзалы аматов бц")
    await message.reply_location(40.51931846586533, 72.80297788183063)
@dp.message_handler(text="контакты")
async def contact(message:types.Message):
    await message.answer(f"{message.from_user.full_name}, вот наши контакты:")
    await message.answer_contact(+9976878778, "Islam")
    await message.answer_contact(+9977568589, "syimuk")
courses = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("UX Designer"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("Child programming"),
    types.KeyboardButton("Main programming"),
    types.KeyboardButton("оставить заявку"),
    types.KeyboardButton("назад")
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboards = True).add(*courses)
@dp.message_handler(text="Курсы")
async def all_courses(message:types.Message):
    await message.answer("вот наши курсы:", reply_markup=courses_keyboard)


@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.reply("сервер")

@dp.message_handler(text="Frontend")
async def front(message:types.Message):
    await message.reply("лицо")

@dp.message_handler(text="UX Designer")
async def design(message:types.Message):
    await message.reply("дизайт")


@dp.message_handler(text="Android")
async def android(message:types.Message):
    await message.reply("типа игры")

@dp.message_handler(text="Child programming")
async def chilish(message:types.Message):
    await message.reply("что то детское")

@dp.message_handler(text="Main programming")
async def main(message:types.Message):
    await message.reply("попробуйте себя во всех направлениях")


executor.start_polling(dp, skip_updates=True)
