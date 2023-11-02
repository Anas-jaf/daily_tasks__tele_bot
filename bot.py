from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from code_for_the_tasks.daily_dairy.utils import *
from io import BytesIO
from PIL import Image
from api import *
import os

# Create a state for conversation
MAX_WIDTH = 800
MAX_HEIGHT = 800

def resize_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        image.thumbnail((max_width, max_height))
    return image

def process_image(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username

    image = update.message.photo[-1]
    image_file = image.get_file()

    insert_image_to_docx(image_file , './daily_diary.docx')
    update.message.reply_text("Image received and saved in a DOCX file.")

def start(update, context):
    update.message.reply_text("Send me a text, and I will save it to a file.")

def save_text(update, context):
    user_input = update.message.text

    add_content_to_existing_docx('./daily_diary.docx',user_input , write_time_heading=True)
    # # Save the user input to a file
    # with open("user_input.txt", "a") as file:
    #     file.write(user_input + "\n")

    update.message.reply_text("Text saved to file.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = production_api
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Handle all text messages with the save_text function
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, save_text))
    dispatcher.add_handler(MessageHandler(Filters.photo, process_image))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
