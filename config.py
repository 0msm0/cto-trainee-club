# config.py
import os

# Load environment variables (optional)
from dotenv import load_dotenv

load_dotenv()

# Add your bot token here
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "6289185362:AAEC3Abjxop8UnjWQFVf6Bhp3-DNxmGLAVU")
print(TELEGRAM_BOT_TOKEN)
