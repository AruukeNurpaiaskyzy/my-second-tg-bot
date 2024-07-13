import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import Command
from config import token
from database import Database
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage )
dp = Database("sql.db")
dp.create_table()

class Form(StatesGroup):
    username = State()
@dp.message(Command("start"))
async def start(message:Message, state:FSMContext):
    await state.set_state(Form.username)
    await message.reply("Привет! Как тебя зовут")
@dp.message(Form.username)
async def process_username(message:Message, state:FSMContext):
    username = message.text
    db.add_user(message.from_user.id, username)
    await state.clear()
