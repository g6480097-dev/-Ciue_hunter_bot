import os
import threading
import telebot
from flask import Flask

# 👇 ВСТАВЬ СВОЙ ТОКЕН ОТ @BotFather
BOT_TOKEN = "8926494159:AAHDEBZ3Smqrt-yCY19t8d6r-SJ3RE_H8h0"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я работаю на бесплатном сервере 24/7!")

def run_bot():
    print("Бот запущен и работает...")
    bot.infinity_polling()

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

if __name__ == "__main__":
    # Запускаем бота в фоне
    thread = threading.Thread(target=run_bot)
    thread.start()
    # Запускаем веб-сервер для Render
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
