import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Bot token
ADMINS = os.getenv("ADMINS").split(',') # adminlar ro'yxati

# WEB_HOST = '0.0.0.0'
# WEB_PORT = int(os.getenv('PORT'))

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
