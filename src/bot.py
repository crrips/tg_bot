from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inline_keyboard = InlineKeyboardMarkup()
inline_keyboard.add(InlineKeyboardButton("Spin", callback_data="spin"))
inline_keyboard.add(InlineKeyboardButton("Receive a spin", callback_data="spin+"))
inline_keyboard.add(InlineKeyboardButton("Choose the language", callback_data="lang"))
inline_keyboard.add(InlineKeyboardButton("Referral link", callback_data="referral"))


language_keyboard = InlineKeyboardMarkup()
language_keyboard.add(InlineKeyboardButton("English", callback_data="lang_en"))
language_keyboard.add(InlineKeyboardButton("Ukrainian", callback_data="lang_ua"))


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Menu"))

