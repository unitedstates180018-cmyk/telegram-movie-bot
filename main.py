from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.environ.get 8579949777:AAEY2a8lK85hfhgwfF634OaYXux_xO3POys

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Movie Download Bot\n\n"
        "Movie name লিখুন 👇"
    )

async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text
    await update.message.reply_text(
        f"🔍 You searched: {movie}\n\n"
        f"⬇ Download link:\n"
        f"https://example.com"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

app.run_polling()
