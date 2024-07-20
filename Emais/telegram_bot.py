import datetime
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from secrets import secret_t
from Emais.patient.models import User  # Предполагается, что у вас есть модель User

TELEGRAM_TOKEN = secret_t

bot = Bot(token=TELEGRAM_TOKEN)

def send_notification(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте! Введите свой username, чтобы связать ваш аккаунт с ботом.")

async def link_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    chat_id = update.message.chat_id
    
    try:
        user = User.objects.get(username=username)
        user.chat_id = chat_id  # Предполагается, что у вас есть поле chat_id в модели User
        user.save()
        await update.message.reply_text("Ваш аккаунт успешно связан с ботом.")
    except User.DoesNotExist:
        await update.message.reply_text("Пользователь с таким username не найден.")

application = Application.builder().token(TELEGRAM_TOKEN).build()

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

username_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), link_username)
application.add_handler(username_handler)

application.run_polling()