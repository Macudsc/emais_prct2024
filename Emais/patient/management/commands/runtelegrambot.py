#тг-боту надо:
#Emais/patient/views.py new_appointment
#Emais/patient/models.py Appointment
#Emais/telegram_bot.py

#python manage.py makemigrations
#python manage.py migrate

#python manage.py runtelegrambot

from sensetiv import tokenn
import datetime
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import User
from patient.models import Appointment, TelegramUser
from apscheduler.schedulers.background import BackgroundScheduler
from asgiref.sync import sync_to_async, async_to_sync

TELEGRAM_TOKEN = tokenn

class Command(BaseCommand):
    help = 'Run Telegram Bot'

    def handle(self, *args, **kwargs):
        application = Application.builder().token(TELEGRAM_TOKEN).build()

        application.add_handler(CommandHandler('start', start))
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), register))
        application.add_handler(CallbackQueryHandler(button))

        application.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user = await sync_to_async(TelegramUser.objects.filter(chat_id=chat_id).first)()
    
    if user:
        await update.message.reply_text('Вы уже зарегистрированы. Чтобы изменить username, отпишитесь от уведомлений.', reply_markup=unsubscribe_markup())
    else:
        await update.message.reply_text('Привет! Введите свой username для регистрации.', reply_markup=start_markup())

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    existing_user = await sync_to_async(TelegramUser.objects.filter(chat_id=chat_id).first)()
    
    if existing_user:
        await update.message.reply_text('Вы уже зарегистрированы. Чтобы изменить username, отпишитесь от уведомлений.', reply_markup=unsubscribe_markup())
        return

    username = update.message.text
    user = await sync_to_async(User.objects.filter(username=username).first)()
    
    if user:
        telegram_user, created = await sync_to_async(TelegramUser.objects.get_or_create)(
            user=user, defaults={'chat_id': chat_id, 'username': username}
        )
        if not created:
            telegram_user.chat_id = chat_id
            await sync_to_async(telegram_user.save)()
        await update.message.reply_text(f'Регистрация прошла успешно! {username}', reply_markup=start_markup())
    else:
        await update.message.reply_text('Пользователь с таким username не найден.', reply_markup=start_markup())

def start_markup():
    keyboard = [[KeyboardButton("/start")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def unsubscribe_markup():
    keyboard = [[InlineKeyboardButton("Отписаться", callback_data='unsubscribe')]]
    return InlineKeyboardMarkup(keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'unsubscribe':
        chat_id = query.message.chat_id
        user = await sync_to_async(TelegramUser.objects.filter(chat_id=chat_id).first)()
        if user:
            await sync_to_async(user.delete)()
            await query.edit_message_text(text="Вы успешно отписались от уведомлений. Теперь вы можете ввести новый username.")
        else:
            await query.edit_message_text(text="Вы не зарегистрированы.")
    elif query.data == 'start':
        await query.edit_message_text(text="Введите свой username для регистрации.")

scheduler = BackgroundScheduler()
scheduler.start()

async def send_notification(chat_id, message):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message)

def schedule_appointment_notifications(appointment):
    message = f'Вы записаны на приём {appointment.date} в {appointment.time} к доктору {appointment.doctor.first_name} {appointment.doctor.last_name}'
    async_to_sync(send_notification)(appointment.patient.telegramuser.chat_id, message)

    appointment_datetime = timezone.make_aware(datetime.datetime.combine(appointment.date, appointment.time), timezone.get_current_timezone())
    
    one_day_before = appointment_datetime - datetime.timedelta(days=1)
    if one_day_before > timezone.now():
        scheduler.add_job(async_to_sync(send_notification), 'date', run_date=one_day_before, args=[appointment.patient.telegramuser.chat_id, f'Напоминание: Вы записаны на приём завтра в {appointment.time}'])

    one_hour_before = appointment_datetime - datetime.timedelta(hours=1)
    if one_hour_before > timezone.now():
        scheduler.add_job(async_to_sync(send_notification), 'date', run_date=one_hour_before, args=[appointment.patient.telegramuser.chat_id, f'Напоминание: Вы записаны на приём через час в {appointment.time}'])

    if appointment_datetime > timezone.now():
        scheduler.add_job(async_to_sync(send_notification), 'date', run_date=appointment_datetime, args=[appointment.patient.telegramuser.chat_id, f'Напоминание: Ваш приём сейчас {appointment.time}'])

    completion_time = appointment_datetime + datetime.timedelta(hours=1)
    if completion_time > timezone.now():
        scheduler.add_job(async_to_sync(send_notification), 'date', run_date=completion_time, args=[appointment.patient.telegramuser.chat_id, f'Ваш приём завершён {appointment.time}'])