import asyncio
import re

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN
from keyboards import menu
import content

from gemini_ai import ask_gemini

bot = Bot(
    token=TOKEN
)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):

    await message.answer(
        "Привет! Это мое портфолио. Что бы узнать больше можешь ввести свой вопрос или просто нажать на любую кнопку🚀",
        reply_markup=menu
    )


@dp.message(Command("about"))
async def about_command(message: types.Message):
    await message.answer(content.about)

@dp.message(Command("goal"))
async def goal_command(message: types.Message):
    await message.answer(content.goal)

@dp.message(Command("history"))
async def history_command(message: types.Message):
    await message.answer(content.story)

@dp.message(Command("mentor"))
async def mentor_command(message: types.Message):
    await message.answer(content.mentor)

@dp.message(Command("progress"))
async def progress_command(message: types.Message):
    await message.answer(content.progress)

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