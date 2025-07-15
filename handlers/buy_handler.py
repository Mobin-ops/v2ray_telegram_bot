from telegram import ReplyKeyboardMarkup
from utils import create_service

def buy_command(update, context):
    keyboard = [["🧪 Test (1d/0.5GB)"], ["💰 Paid (5d/5GB)"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("Please choose the type of service:", reply_markup=reply_markup)

def handle_buy_selection(update, context):
    selection = update.message.text
    if "Test" in selection:
        result = create_service(gig=0.5, day=1, test=1)
        if result.get("ok"):
            update.message.reply_text("✅ Test service created successfully!")
        else:
            update.message.reply_text(f"❌ Failed to create test service:\n{result}")
    elif "Paid" in selection:
        update.message.reply_text(
            "💳 To purchase a paid VPN service (5 days / 5GB):\n"
            "➡ Please transfer 50,000 Toman to:\n"
            "`6037-9915-1234-5678`\n\n"
            "Then send the payment receipt here."
        )
        context.user_data["awaiting_payment"] = True
