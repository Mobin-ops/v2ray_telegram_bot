from telegram import ReplyKeyboardMarkup
from utils import create_service

def buy(update, context):
    keyboard = [["🧪 Test (1d/0.5GB)"], ["💰 Paid (5d/5GB)"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text("Choose a service type:", reply_markup=reply_markup)

def handle_buy_choice(update, context):
    text = update.message.text
    if "Test" in text:
        result = create_service(0.5, 1, test=1)
        update.message.reply_text(f"✅ Test service created:\n{result}")
    elif "Paid" in text:
        update.message.reply_text("💳 Please pay 50,000 Toman to:\n6037-9915-1234-5678\nThen send the receipt photo here.")
        context.user_data["waiting_for_payment"] = True
