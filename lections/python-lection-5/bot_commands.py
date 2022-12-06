from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/summ')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')

async def summ_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')