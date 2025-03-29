from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить геолакацию 📍', request_location=True)],
    [KeyboardButton(text='/help 🚀'), KeyboardButton(text='/news')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)