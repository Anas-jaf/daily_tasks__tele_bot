from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from code_for_the_tasks.daily_dairy.utils import *
from io import BytesIO
from PIL import Image
from api import *
import os

# Create a state for conversation

def process_image(update, context):
    # user_id = update.message.from_user.id
    # user_name = update.message.from_user.username

    image = update.message.photo[-1]
    image_file = image.get_file()

    # # Create a new PIL Image from the image byte stream
    # with BytesIO() as image_buffer:
    #     image_file.download(out=image_buffer)
    #     image_buffer.seek(0)
    #     img = Image.open(image_buffer)
        
    #     # Resize the image using the resize_image function
    #     img = resize_image(img)         

    #     # Create a new DOCX document
    #     doc = Document()

    #     # Add the resized image to the DOCX file
    #     img_bytes = BytesIO()
    #     img.save(img_bytes, format='JPEG')
    #     p = doc.add_paragraph()
    #     run = p.add_run()
    #     run.add_picture(img)
    #     # Align the paragraph to the right
    #     p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    #     doc.add_paragraph(style='LO-normal' )
        
    #     # doc.add_picture(img_bytes)
        
    #     # Save the DOCX document with a unique filename
    #     docx_filename = f"image_docx_{update.message.message_id}.docx"
    #     doc.save(docx_filename)
    #     update.message.reply_text("Image received and saved in a DOCX file.")

    insert_image_to_docx(image_file , './daily_diary.docx')
    

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
