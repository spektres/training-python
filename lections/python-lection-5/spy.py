from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a', encoding="utf-8")
    file.write(f'{update.effective_user.first_name}, {update._effective_user.id}, {update.message.text}\n')
    file.close()