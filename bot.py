import requests as rq
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token="6360288615:AAHUzh7jqmlKqibNXb1jsp_a7kLx3RnzL3M")
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id, 'Чтобы получить ответы пришли вариант КИМ kompege')

@dp.message_handler(content_types=["text"])
async def echo_message(message):
        data = rq.get(f"https://kompege.ru/api/v1/variant/kim/{message.text}").json()["tasks"]
        for i, task in enumerate(data):
           if ("\n" in task["key"]):
                print('123123123')
                task["key"] = str(task["key"]).replace("\n", " ")
           await bot.send_message(message.chat.id, f"№ {i+1}, Ответ {task['key']}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)