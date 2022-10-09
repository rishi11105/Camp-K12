from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Hello, World')
updater = Updater(token='5461049902:AAGajjbzu9jxQ3xRmKtUSpH1aCClL1Zlruk', use_context=True)
dispatcher = updater.dispatcher
hello_handler = CommandHandler('hello',hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()
