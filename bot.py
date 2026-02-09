from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مهندس شندیدم غلومی میزنی!!😎😎😎")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()
