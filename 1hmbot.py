from aiogram import Bot, Dispatcher, types, executor
import random 
from config import token

bot = Bot(token = token)
dp = Dispatcher(bot)

name = random.randint(1,3)
@dp.message_handler(commands="start")
async def start (message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте")

@dp.message_handler(text= "1")
async def start (message:types.Message):
    if name == 1: 
        await message.reply("правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")

    elif name !=1:
        await message.reply("не правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
@dp.message_handler(text= "2")
async def start (message:types.Message):
    if name == 2: 
        await message.reply("правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")

    elif name !=2:
        await message.reply("не правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
@dp.message_handler(text= "3")
async def start (message:types.Message):
    if name == 3: 
        await message.reply("правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")

    elif name !=3:
        await message.reply("не правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
executor.start_polling(dp)

