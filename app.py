from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers.start_handler import start_command
from handlers.buy_handler import buy_command, handle_buy_selection

app = Flask(__name__)
bot = Bot(BOT_TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("buy", buy_command))
dispatcher.add_handler(MessageHandler(Filters.regex("^(🧪 Test|💰 Paid)$"), handle_buy_selection))

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "V2Ray Telegram Bot is running."
