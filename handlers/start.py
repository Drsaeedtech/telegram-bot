from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 به Math Legend Bot خوش آمدی!\n"
        "هر عبارت ریاضی بفرستی محاسبه می‌کنم."
    )

start_handler = CommandHandler("start", start)

