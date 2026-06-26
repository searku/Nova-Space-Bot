import asyncio
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN
from keyboards import menu
import content

from gemini_ai import ask_gemini


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):

    await message.answer(
        "Привет! Это мое портфолио 🚀",
        reply_markup=menu
    )


@dp.message(Command("about"))
async def about_command(message: types.Message):
    await message.answer(content.about)
    sticker_id = "CAACAgIAAxkBAAFNeoxqPkRJn7cDAAF4KteQdCvP1HyvJ1cAAuaWAAJWorBJFW77JusTOO08BA"

    bot.send_sticker(message.chat.id,sticker_id)

@dp.message(Command("goal"))
async def goal_command(message: types.Message):
    await message.answer(content.goal)
    sticker_id = "CAACAgIAAxkBAAFNeppqPkUmYxZoQ6du2UM2SUXXXekz0wAC6oQAAlfRuEmJR64qnLwXFDwE"

    bot.send_sticker(message.chat.id,sticker_id)

@dp.message(Command("history"))
async def history_command(message: types.Message):
    await message.answer(content.story)

@dp.message(Command("mentor"))
async def mentor_command(message: types.Message):
    await message.answer(content.mentor)
    sticker_id = "CAACAgIAAxkBAAFNeqFqPkVEbBWM2aH_gZhuwxvhQJcc_AACZoYAAuuSuUnvq90XFTqG1DwE"

    bot.send_sticker(message.chat.id,sticker_id)

@dp.message(Command("progress"))
async def progress_command(message: types.Message):
    await message.answer(content.progress)
    sticker_id = "CAACAgIAAxkBAAFNeo9qPkRX8Re0wZrs7kvjeNzzqb65JAACBogAAvk-uElTGS2vVSlUBDwE"

    bot.send_sticker(message.chat.id,sticker_id)

@dp.message(Command("hobby"))
async def hobby_command(message: types.Message):
    await message.answer(content.hobbies)

@dp.message(Command("works"))
async def works_command(message: types.Message):

    await message.answer(
        "\n".join(content.works)
    )


@dp.message(Command("github"))
async def github_command(message: types.Message):

    await message.answer(content.github)
    sticker_id = "CAACAgIAAxkBAAFNep9qPkU9IqA6a7i2L8Q4bpFYCJW56gAC8pEAAl90uUmMWhnxTSGMsDwE"

    bot.send_sticker(message.chat.id,sticker_id)


@dp.message()
async def messages(message: types.Message):

    text = message.text.lower()


    if "о себе" in text:
        await message.answer(content.about)

    elif "цель" in text:
        await message.answer(content.goal)

    elif "история" in text:
        await message.answer(content.story)

    elif "ментор" in text:
        await message.answer(content.mentor)

    elif "прогресс" in text:
        await message.answer(content.progress)

    elif "хобби" in text:
        await message.answer(content.hobbies)

    elif "работы" in text:
        await message.answer(
            "\n".join(content.works)
        )

    elif "github" in text:
        await message.answer(content.github)

    else:

        answer = await ask_gemini(
            message.text
        )

        await message.answer(answer)



async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())