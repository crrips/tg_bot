from bot import dp, executor
import sqlite3


if __name__ == '__main__':
    from handlers import register_handlers
    register_handlers()
    
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER UNIQUE NOT NULL,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        language_code TEXT,
        chosen_language TEXT DEFAULT 'en',
        spins INTEGER DEFAULT 3
    )
    ''')

    conn.commit()
    conn.close()
    
    executor.start_polling(dp, skip_updates=True)