from aiogram.utils import executor
from onboard_bot_class import OnboardBot

if __name__ == "__main__":
    onboard_bot: OnboardBot = OnboardBot()
    executor.start_polling(onboard_bot.get_dp(), skip_updates=True)
