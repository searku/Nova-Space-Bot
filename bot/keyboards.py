from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 О себе"), KeyboardButton(text="🎯 Цель")],
        [KeyboardButton(text="📚 История"), KeyboardButton(text="👩‍💻 Ментор")],
        [KeyboardButton(text="📈 Прогресс"), KeyboardButton(text="🎨 Хобби")],
        [KeyboardButton(text="💼 Работы"), KeyboardButton(text="💻 GitHub")]
    ],
    resize_keyboard=True
)