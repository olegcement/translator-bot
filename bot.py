import telebot
import json
from config import BOT_TOKEN, PASSWORD
from translator import translate
from datetime import datetime
def log(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{time} - {text} \n")

bot = telebot.TeleBot(BOT_TOKEN)
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
user_texts = {}
AUTH_FILE = "authorized.json"
def load_authorized():
    try:
        with open(AUTH_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()
def save_authorized():
    with open(AUTH_FILE, "w") as f:
        json.dump(list(authorized), f)
authorized = load_authorized()
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Кодовое слово, не угадал = лох:")
@bot.message_handler(func=lambda m: m.text == PASSWORD)
def auth(message):
    authorized.add(message.chat.id)
    save_authorized()
    log(f"новый пользователь авторизован: {message.chat.id}")
    bot.send_message(message.chat.id, "Вы не пидор!")
@bot.message_handler(content_types=['text'])
def ask_language(message):
    if message.chat.id not in authorized:
        log(f"неверный пароль от {message.chat.id}: {message.text}")
        bot.send_message(message.chat.id, "Пошел нахуй чертила. Напиши /start")
        return
    log(f"запрос перевода от {message.chat.id}: {message.text}")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🇷🇺 Русский", callback_data="ru"))
    keyboard.add(InlineKeyboardButton("🇵🇱 Польский", callback_data="pl"))
    keyboard.add(InlineKeyboardButton("🇬🇧 Английский", callback_data="en"))
    user_texts[message.chat.id] = message.text
    bot.send_message(message.chat.id, "Выбери язык:", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    text = user_texts.get(call.message.chat.id)
    language = {"ru": "русский", "pl": "польский", "en": "английский"}[call.data]
    try:
        result = translate(text, language)
        bot.send_message(call.message.chat.id, f"`{result}`", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(call.message.chat.id, "Ошибка перевода, попробуй еще раз")
        log(f"Ошибка: {e}")
    log(f"перевод запрошен")
bot.polling()