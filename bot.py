import logging
import requests
from aiogram import Bot, types,  Dispatcher, executor



bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

#запрос курса доллара
data = requests.get('https://openexchangerates.org/api/latest.json?app_id=f5a5bef7a19245b5a669d399bc96369c&base=USD&symbols=RUB').json()
p = data['rates']['RUB']


#команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    kb = types.InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(types.InlineKeyboardButton(text="Что я умею", callback_data="info"))
    kb.add(types.InlineKeyboardButton(text="Курс доллара", callback_data="USD_exchange_rate"))
    await  message.answer('Привет! Выберите то, что вам нужно.', reply_markup=kb)

#кнопка "Курс доллара"
@dp.callback_query_handler(text='USD_exchange_rate')
async def send_random_value(call: types.CallbackQuery):
    await  call.message.answer(f'Курс доллара: {p}.')

#кнопка  "Что я умею"
@dp.callback_query_handler(text='info')
async def send_random_value(call: types.CallbackQuery):
    await  call.message.answer('Этот бот выводит курс доллара.')

#кнопка на случай, если будет отправлено непредусмотренное сообщение
@dp.message_handler()
async def text_input(message: types.Message):
    await  message.answer('Я не понимаю о чём вы ')

#запуск бота
executor.start_polling(dp, skip_updates=True)
