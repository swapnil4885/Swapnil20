from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google_sheet import connect_sheet
from config import BOT_TOKEN

sheet = connect_sheet()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi Swapnil! Rendar Bot is live 🔥")

def echo(update: Update, context: CallbackContext):
    msg = update.message.text
    user = update.message.from_user.username or update.message.from_user.first_name
    sheet.append_row([str(update.message.date), user, msg, "Logged"])
    update.message.reply_text("✅ Message saved to Google Sheet!")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
