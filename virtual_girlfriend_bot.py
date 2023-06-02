from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram import Update



def start(update, context):
  update.message.reply_text('Hello! Welcome to anandsdata BOT! Enjoy the resource!')    
  update.message.reply_text('Type /help for the content to display!')
  update.message.reply_text('Happy Learning!')

def main():
    updater = Updater("6238420815:AAE7Ajvmvom0WFX94PhzQ3zUE-bZa8Ak6lo")
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()
    


def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = generate_response(user_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def generate_response(user_message):
    # Add your logic here to generate a response based on the user's message
    # For example, you can use conditionals, random selection, or even machine learning techniques

    # Return a sample response for now
    return "I'm still learning. Can we talk about something else?"



if __name__ == '__main__':
    main()
