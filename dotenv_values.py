import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

telegram_bot_token = os.environ.get("telegram_bot_token")
