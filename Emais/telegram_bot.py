from telegram import Bot
from telegram.ext import Application, CommandHandler

TELEGRAM_TOKEN = '7179831637:AAGjKGzE8rYbTccp9ywAFGhkaFZhSR6Xlx0'

bot = Bot(token=TELEGRAM_TOKEN)

def send_notification(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your healthcare assistant bot.")

application = Application.builder().token(TELEGRAM_TOKEN).build()

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

application.run_polling()