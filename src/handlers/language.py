from aiogram import types
from bot import dp, bot, language_keyboard
import sqlite3


@dp.callback_query_handler(lambda c: c.data == "lang")
async def process_callback(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Choose the language", reply_markup=language_keyboard)
    
    
@dp.callback_query_handler(lambda c: c.data == "lang_en")
async def process_callback(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users
            SET chosen_language = 'en'
            WHERE user_id = ?
            ''', (user_id,))
    
    conn.commit()
    conn.close()
    
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    
    
@dp.callback_query_handler(lambda c: c.data == "lang_ua")
async def process_callback(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users
            SET chosen_language = 'ua'
            WHERE user_id = ?
            ''', (user_id,))
    
    conn.commit()
    conn.close()
    
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)