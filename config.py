from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_KEY = os.getenv('OPENWEATHER_API_KEY')

