from aiogram import types
from bot import dp, bot
import sqlite3
from config.config import BOT_LINK


@dp.callback_query_handler(lambda c: c.data == "referral")
async def process_callback(callback_query: types.CallbackQuery):
    
    user_id = callback_query.from_user.id
    
    referral_link = f"https://t.me/{BOT_LINK}?start={user_id}"
    
    await bot.send_message(callback_query.from_user.id, f"Your referral link: {referral_link}")
    
    