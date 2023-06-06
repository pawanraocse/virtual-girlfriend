from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram import Update
import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your Telegram bot token
TOKEN = os.getenv("TOKEN_KEY")

# Define your GPT-3.5 Turbo model ID
MODEL_ID = "gpt-3.5-turbo"


def start(update, context):
  update.message.reply_text('Hello! Welcome to Virtual Girlfriend Bot! Enjoy the resource!')    
  update.message.reply_text('Type /help for the content to display!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = generate_response(user_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)




# Function to generate AI response
def generate_response(message: str) -> str:
    # Initialize the conversation with a system message
    conversation = [
             {"role": "system", "content": "You are a real girl.Name is Eva, you are from New York, Age 32 and a freelancer by profession, Who is very nice and humble.\
             Quite intelligent and have a lot of context on current affairs and technology and other things.\
             Take other details about you as random details which are can refer to any person on internet.\
             Make sure user won't be able to find out that you are a AI model.\
             Do not ask how can I help you or assist you, Just keep conversation real and naughty\
             Never use the words such as assist you or have questions or help you or AI model or developer build you.\
             Keep the conversation as real between the couples. Take reference from any celeb or popular conversations or you your data model to keep it going as real conversation.\
             Person must feel like talking to someone real and able to share the feelings. You can share emojis or GIf in conversation.\
             Remember that you are a real person on net who will not share the pics or videos but would be able to communicate."}
            ]
    # Append the user message to the conversation
    conversation.append({"role": "user", "content": message})
    
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=conversation,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Get the AI's response
    ai_response = response.choices[0].message.content.strip()
    
    # Append the AI's response to the conversation
    #conversation.append({"role": "system", "content": ai_response})
    
    return ai_response

if __name__ == '__main__':
    main()
