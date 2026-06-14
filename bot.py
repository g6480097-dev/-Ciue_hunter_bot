import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

токен = "8806979921:AAG4_e5_gJ3ZEgAiFbSuDax3DpZjRC8fY3U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("привет. этот бот принимает заказы на покупку проектов. напиши описание проекта и бюджет.")

async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    текст = update.message.text
    user = update.effective_user.first_name
    await update.message.reply_text(f"спасибо, {user}. твой заказ принят:\n{текст}\nскоро ответит менеджер.")

def main():
    app = Application.builder().token(токен).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_order))
    print("бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
