import logging
from line import line
from lines import lines

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5454226391:AAGQ9GjxdvAEio6_jxOYsEq02Dz0V5stsb0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['label'])
async def label(message: types.Message):
    print("Got request to print label")
    args = message.get_args().split()
    if len(args):
        for a in args:
            p = a.split(":")
        req = message.get_args()
        if req in lines:
            line(req).poll()
        else:
            await message.answer("No line number exists")
    else:
        await message.answer("No line number exists")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(message.text)

def main():
    print ("started")
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True)
    # executor.start
    s7poll()
    
def s7poll():
    for l in lines:
        line(l).poll()



if __name__ == "__main__":
    s7poll()
