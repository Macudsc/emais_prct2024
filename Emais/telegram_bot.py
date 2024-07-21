from sensetiv import tokenn
import datetime
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from core.models import User  # Предполагается, что у вас есть модель User

TELEGRAM_TOKEN = tokenn
