import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# আপনার টপআপ লিস্ট
TOPUP_PACKS = {
    "100_diamond": {"name": "100 Diamond - 120 TK", "price": 120},
    "200_diamond": {"name": "200 Diamond - 230 TK", "price": 230},
    "500_diamond": {"name": "500 Diamond - 550 TK", "price": 550},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, pack in TOPUP_PACKS.items():
        keyboard.append([InlineKeyboardButton(pack["name"], callback_data=key)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔥 Welcome to TopUp Bot!\n\nআপনার প্যাক সিলেক্ট করুন:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    pack_key = query.data
    pack = TOPUP_PACKS.get(pack_key)
    if pack:
        await query.message.reply_text(
            f"✅ আপনি সিলেক্ট করেছেন: {pack['name']}\n\n"
            f"💰 পেমেন্ট করতে bKash/Nagad এ টাকা পাঠান।\n"
            f"তারপর আপনার Game UID দিন।\n\n"
            f"এডমিন শীঘ্রই আপনার সাথে যোগাযোগ করবে।"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
