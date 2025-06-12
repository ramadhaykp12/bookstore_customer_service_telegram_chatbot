from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from llm import answer_question

# Ganti dengan token bot kamu
TOKEN = "Telegram Bot Father Token"

# Fungsi saat ada /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Selamat datang di Toko Buku Dhany, ada yang bisa saya bantu ?.
""")


# Fungsi untuk menangani pesan teks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text("Tunggu Sebentar, saya sedang berpikir... ")

    try:
        response = answer_question(user_input)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {e}")

# Jalankan aplikasi bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot sedang berjalan...")
    app.run_polling()