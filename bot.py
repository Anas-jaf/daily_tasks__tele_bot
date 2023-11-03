import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from code_for_the_tasks.daily_dairy.utils import *
from io import BytesIO
from PIL import Image
from api import *
import os

# ضع المتغيرات هنا رجاءا
MAX_WIDTH = 800
MAX_HEIGHT = 800

text_responses = [
    "تم",
    "تمام",
    "ساسجل هذا في المذكرات",
    "تم يا القلب",
    "تم التسجيل في المذكرات"
]

image_responses = [
    "اوك",
    "تم",
    "ممتاز",
    "تمت اضافة الصورة"
]

document_file = './daily_diary_document/مذكرات.docx'

def process_image(update, context):
    image = update.message.photo[-1]
    image_file = image.get_file()
    insert_image_to_docx(image_file , document_file)
    update.message.reply_text(random.choice(image_responses))

def start(update, context):
    update.message.reply_text("ارسل ملف و سوف احفظه في ملف")

def save_text(update, context):
    user_input = update.message.text
    add_content_to_existing_docx(document_file ,user_input , write_time_heading=True)
    update.message.reply_text(random.choice(text_responses))

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
