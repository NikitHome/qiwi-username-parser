from aiogram.utils import executor
from create_bot import dp
from handlers.user_handlers import register_user_handlers


if __name__ == '__main__':
    register_user_handlers(dp)
    
    # запуск бота
    try:    
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(e)