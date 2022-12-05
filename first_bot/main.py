from aiogram import Bot, Dispatcher, executor, types
import first_bot.config as config
import time

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start' , 'go'])
async def start(message : types.Message):
    with open('users.txt', 'a+', encoding='utf-8') as users:
        users.write(f"{message.from_user.full_name} {message.from_user.id} {time.ctime()}\n")
    await message.answer(f'Привет, {message.from_user.full_name} \n Я первый бот компании "ASN" \n У меня пока доступны только функции /start, /help и могу ответить на "Привет" приветом в любое время суток ')

@dp.message_handler(commands=['help'])
async def help(message : types.Message):
    await message.reply("напишите в DIRECT \nмой аккаунт: https://instagram.com/_abdykadyrov_s?igshid=YmMyMTA2M2Y= ")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("я вас не понял введите /help")

executor.start_polling(dp)
