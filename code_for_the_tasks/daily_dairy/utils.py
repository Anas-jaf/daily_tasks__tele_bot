import locale
from docx import Document
from datetime import datetime

def format_arabic_date_with_day_name():
    # Set the locale to Arabic
    locale.setlocale(locale.LC_TIME, 'ar_AE.UTF-8')  # Change 'ar_AE' to your desired Arabic locale

    # Get the current date and time
    current_date = datetime.now()

    # Format the date to include the day name in Arabic
    formatted_date = current_date.strftime("%A، %Y/%m/%d")

    return formatted_date

def add_content_to_existing_docx(file_path , text ,style='LO-heading' ):
    # Open the existing Document
    doc = Document(file_path)

    # Add paragraph with style
    doc.add_paragraph(text , style=style )
    doc.add_paragraph(style='LO-normal' )

    # Save the modified document back to the same file
    doc.save(file_path)

    print(f"Content added to {file_path}")

# Specify the path to the existing document
existing_docx_file = './daily_diary.docx'
arabic_date = format_arabic_date_with_day_name()

# Call the function to add content to the existing document
add_content_to_existing_docx(existing_docx_file , arabic_date)
