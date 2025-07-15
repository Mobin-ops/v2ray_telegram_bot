from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers.start_handler import start_command
from handlers.buy_handler import buy_command, handle_buy_selection
import os

# Create Flask application
app = Flask(__name__)

# Set up bot and Dispatcher
bot = Bot(BOT_TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

# Define handlers
dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("buy", buy_command))
dispatcher.add_handler(MessageHandler(Filters.regex("^(🧪 Test|💰 Paid)$"), handle_buy_selection))

# Webhook route
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Index route for status check
@app.route("/", methods=["GET"])
def index():
    return "V2Ray Telegram Bot is running."

# Set webhook and run application
if __name__ == "__main__":
    # Set webhook with Render URL if available
    render_url = os.environ.get("RENDER_EXTERNAL_URL")
    if render_url:
        webhook_url = f"https://{render_url}/{BOT_TOKEN}"
        bot.setWebhook(webhook_url)
    # Run application with dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
