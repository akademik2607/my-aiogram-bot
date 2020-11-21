import os

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
print(BOT_TOKEN)
admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")