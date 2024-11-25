from aiogram import types
from bot import dp, bot
import sqlite3


@dp.callback_query_handler(lambda c: c.data == "spin")
async def process_callback(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    spins = cursor.execute('''
                           SELECT spins
                             FROM users
                             WHERE user_id = ?
                             ''', (user_id,)).fetchone()[0]
    
    if spins == 0:
        await bot.send_message(callback_query.from_user.id, "You have no spins left!")
        return
    
    cursor.execute('''
                   UPDATE users
                     SET spins = spins - 1
                     WHERE user_id = ?
                     ''', (user_id,))
    
    spins = cursor.execute('''
                           SELECT spins
                             FROM users
                             WHERE user_id = ?
                             ''', (user_id,)).fetchone()[0]
    
    conn.commit()
    conn.close()
    
    await bot.send_message(callback_query.from_user.id, "😵‍💫")
    await bot.send_message(callback_query.from_user.id, f"You have {spins} spins left!")
    
    
@dp.callback_query_handler(lambda c: c.data == "spin+")
async def process_callback(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                     UPDATE users
                        SET spins = spins + 1
                        WHERE user_id = ?
                        ''', (user_id,))
    
    spins = cursor.execute('''
                            SELECT spins
                              FROM users
                              WHERE user_id = ?
                              ''', (user_id,)).fetchone()[0]
    
    conn.commit()
    conn.close()
    
    await bot.send_message(callback_query.from_user.id, f"You have {spins} spins now!")
