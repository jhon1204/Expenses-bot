from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Application.builder().token(TOKEN).build()

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Welcome to the FastAPI Chatbot.')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Send /start to start the bot.')

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help_command)
bot.add_handler(start_handler)
bot.add_handler(help_handler)