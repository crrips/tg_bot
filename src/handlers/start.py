from aiogram import types
from bot import dp, bot, inline_keyboard, main_menu
import sqlite3


@dp.message_handler(commands=['start'])
async def send_welcome(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    user_username = callback_query.from_user.username
    user_first_name = callback_query.from_user.first_name
    user_last_name = callback_query.from_user.last_name
    user_language_code = callback_query.from_user.language_code

    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, language_code)
            VALUES (?, ?, ?, ?, ?)
            ''', (user_id, user_username, user_first_name, user_last_name, user_language_code))
    
    conn.commit()
    conn.close()
    
    await bot.send_message(user_id, "Welcome to bot!", reply_markup=main_menu)
    
    
@dp.message_handler(lambda message: message.text == "Menu")
async def send_welcome(message: types.Message):
    
    await bot.send_message(message.from_user.id, "Main Menu", reply_markup=inline_keyboard)
    